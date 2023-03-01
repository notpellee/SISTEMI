from pathlib import Path   #GESTISCE PERCORSI DEL FILESYSTEM
from logzero import logger, logfile #PERMETTE DI SCRIVERE SUL CONSOLE E/O FILE <DELLE STRINGHE
from sense_hat import SenseHat  #PERMETTE DI CONTROLLARE I SENSORI DEL RASPBERRY
from picamera import PiCamera   #PERMETTE DI FARE ANALISI SU IMMAGINI IN PYTHON
from orbit import ISS  #GESTISCE DATI SULL'ORBITA
from time import sleep
from datetime import datetime, timedelta #PERMETTE DI MANIPOLARE DATE E TEMPI
import csv

def create_csv_file(data_file):
    """Create a new CSV file and add the header row"""
    with open(data_file, 'w') as f:  #CHIUDE IL FILE APPENA TERMINATO IL CICLO
        writer = csv.writer(f)  
        header = ("Counter", "Date/time", "Latitude", "Longitude", "Temperature", "Humidity")
        writer.writerow(header) #SCRIVE SULL' HEAD DEL FILE

def add_csv_data(data_file, data):
    """Add a row of data to the data_file CSV"""
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def convert(angle):
    """
    Convert a `skyfield` Angle to an EXIF-appropriate
    representation (rationals)
    e.g. 98° 34' 58.7 to "98/1,34/1,587/10"

    Return a tuple containing a boolean and the converted angle,
    with the boolean indicating if the angle is negative.
    """
    sign, degrees, minutes, seconds = angle.signed_dms() #RITORNA UN BOOLENAO 
    exif_angle = f'{degrees:.0f}/1,{minutes:.0f}/1,{seconds*10:.0f}/10'
    return sign < 0, exif_angle

def capture(camera, image):
    """Use `camera` to capture an `image` file with lat/long EXIF data."""
    location = ISS.coordinates()

    # Convert the latitude and longitude to EXIF-appropriate representations
    south, exif_latitude = convert(location.latitude)       #exif = dati inerenti alla latitudine e longitudine dell ISS 
    west, exif_longitude = convert(location.longitude)

    # Set the EXIF tags specifying the current location
    camera.exif_tags['GPS.GPSLatitude'] = exif_latitude             
    camera.exif_tags['GPS.GPSLatitudeRef'] = "S" if south else "N"
    camera.exif_tags['GPS.GPSLongitude'] = exif_longitude
    camera.exif_tags['GPS.GPSLongitudeRef'] = "W" if west else "E"

    # Capture the image
    camera.capture(image) #cattura e salva l'immagine in image


base_folder = Path(__file__).parent.resolve()  #salva la directory in cui salvo il programma

# Set a logfile name
logfile(base_folder/"events.log") #crea un file chiamato events.log

# Set up Sense Hat
sense = SenseHat()

# Set up camera
cam = PiCamera() #oggetto cam
cam.resolution = (1296, 972)  #swt della risoluzione in pixel

# Initialise the CSV file
data_file = base_folder/"data.csv"
create_csv_file(data_file)

# Initialise the photo counter
counter = 1
# Record the start and current time
start_time = datetime.now()
now_time = datetime.now()
# Run a loop for (almost) three hours
while (now_time < start_time + timedelta(minutes=178)):
    try:
        humidity = round(sense.humidity, 4)
        temperature = round(sense.temperature, 4)  #misura di temperatura 
        # Get coordinates of location on Earth below the ISS
        location = ISS.coordinates()
        # Save the data to the file
        data = (
            counter,
            datetime.now(),
            location.latitude.degrees,
            location.longitude.degrees,
            temperature,
            humidity,
        )
        add_csv_data(data_file, data)
        # Capture image
        image_file = f"{base_folder}/photo_{counter:03d}.jpg" 
        capture(cam, image_file)
        # Log event
        logger.info(f"iteration {counter}")
        counter += 1
        sleep(30)
        # Update the current time
        now_time = datetime.now()
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e}')