import random,turtle
SPEED = 1000
MS = 3000000000
MOV=5
def bug(rob):
    rob.speed(SPEED)
    
    for _ in range(MS):
        ran = random.randint(1,4)
        angolo = 90 * ran
        rob.right(angolo)
        rob.forward(MOV)

def main():
    
    finestra = turtle.Screen()
    robot = turtle.Turtle()
    bug(robot)
    turtle.done()
    



    
if __name__ == "__main__":
    main()
    
    