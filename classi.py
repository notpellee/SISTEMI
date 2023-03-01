import math

class IPAddress():
    #non esiste la denominazione privata o pubblica
    def __init__(self, ip_string):
        self.ip_notazione_dec = ip_string
        self.ip_notazione_bin = None
        self.ip_binario = None      #Senza i punti
    
    def toList(self, ip):
        lista_valori = ip.split(".")
        return [int(numero) for numero in lista_valori]

    def dec2bin(self, ip):
        lista_valori = self.toList(ip)
        s = ""
        for numero in lista_valori:
            temp = bin(numero)[2:]
            temp = "0" * (8 - len(temp)) + temp
            s += temp + "."
        self.ip_notazione_bin = s[:-1]
        return self.ip_notazione_bin

    def dec2binario(self, ip):
        lista_valori = self.toList(ip)
        self.ip_binario = ""
        for numero in lista_valori:
            temp = bin(numero)[2:]
            temp = "0" * (8 - len(temp)) + temp
            self.ip_binario = self.ip_binario + temp
        return self.ip_binario
    
    def bin2dec(self, ip):
        lista_ip = ip.split(".")
        dec = ""
        for num in lista_ip:
            temp = int(num, 2)
            dec += str(temp) + "."
        return dec[:-1]

    def ipbroadcast(self, subnetmask, ip):      #subnetmask -> str = "/n", deve stampare l'ip di broadcast in notazione decimale puntata
        num = int(subnetmask[1:])
        broadcast_bin = self.dec2binario(ip)[:num] + "1" * (32 - num)
        broadcast_bin_puntato = broadcast_bin[:8] + "." + broadcast_bin[8:16] + "." + broadcast_bin[16:24] + "." + broadcast_bin[24:]
        return self.bin2dec(broadcast_bin_puntato)

    def iprete(self, subnetmask, ip):      #subnetmask -> str = "/n", deve stampare l'ip di broadcast in notazione decimale puntata
        num = int(subnetmask[1:])
        rete_bin = self.dec2binario(ip)[:num] + "0" * (32 - num)
        rete_bin_puntato = rete_bin[:8] + "." + rete_bin[8:16] + "." + rete_bin[16:24] + "." + rete_bin[24:]
        return self.bin2dec(rete_bin_puntato)
    
    def subnet_mask_control(self, subnetmask, ip):
        if subnetmask[0] == "/":
            return subnetmask
        else:
            ip = IPAddress(subnetmask)
            temp = ip.dec2binario(ip)     #Subnet mask convertita in binario senza punti
            count = 0
            for c in temp:
                if c == "1":
                    count += 1
            subnet_mask = "/" + str(count)
            return subnet_mask
    
    def primoIndirizzo(self, subnetmask, ip):
        num = int(subnetmask[1:])
        primo_bin = self.dec2binario(ip)[:num] + "0" * (32 - num - 1) + "1"
        primo_bin_puntato = primo_bin[:8] + "." + primo_bin[8:16] + "." + primo_bin[16:24] + "." + primo_bin[24:]
        return self.bin2dec(primo_bin_puntato)
    
    def ultimoIndirizzo(self, subnetmask, ip):
        num = int(subnetmask[1:])
        primo_bin = self.dec2binario(ip)[:num] + "1" * (32 - num - 1) + "0"
        primo_bin_puntato = primo_bin[:8] + "." + primo_bin[8:16] + "." + primo_bin[16:24] + "." + primo_bin[24:]
        return self.bin2dec(primo_bin_puntato)

    def subnet_mask_sottorete(self, subnetmask, n_sottoreti):
        diff = math.ceil(math.log(n_sottoreti, 2))
        new_subnet_mask_int = int(subnetmask[1:]) + diff
        new_subnet_mask = "/" + str(new_subnet_mask_int)
        return new_subnet_mask
    
    def combinazioni_subnetting(self, n_sottoreti):
        return math.ceil(math.log(n_sottoreti, 2))


    def subnetting(self, subnetmask, n_sottoreti, ip):
        n_combinazioni = self.combinazioni_subnetting(n_sottoreti)
        new_subnetmask = self.subnet_mask_sottorete(subnetmask, n_sottoreti)

        for comb in range (n_sottoreti):
            temp = str(bin(comb)[2:])
            temp = "0" * (n_combinazioni - len(temp)) + temp

            ip_bin = self.dec2binario(ip)[:int(subnetmask[1:])] + temp + self.dec2binario(ip)[int(new_subnetmask[1:]):]
            ip_bin_puntato = ip_bin[:8] + "." + ip_bin[8:16] + "." + ip_bin[16:24] + "." + ip_bin[24:]
            ip = self.bin2dec(ip_bin_puntato)

            print(f"L'indirizzo di rete e': {self.iprete(new_subnetmask, ip)}")
            print(f"l'indirizzo di broadcast e': {self.ipbroadcast(new_subnetmask, ip)}\n")


def main():
    indirizzo_ip = input("Inserire l'indirizzo IP: ")
    subnetmask_davalidare = input("Inserire la subnet mask: ")
    n_sottoreti = int(input("Inserire il numero di sottoreti: "))

    indirizzoIP = IPAddress(indirizzo_ip)
    subnetmask = indirizzoIP.subnet_mask_control(subnetmask_davalidare, indirizzo_ip)
    indirizzoIP.subnet_mask_sottorete(subnetmask, n_sottoreti)
    """
    print(f"l'indirizzo di broadcast e': {indirizzoIP.ipbroadcast(subnetmask, indirizzo_ip)}")
    print(f"L'indirizzo di rete e': {indirizzoIP.iprete(subnetmask, indirizzo_ip)}")
    print(f"Il primo indirizzo utilizzabile e': {indirizzoIP.primoIndirizzo(subnetmask, indirizzo_ip)}")
    print(f"L'ultimo indirizzo utilizzabile e': {indirizzoIP.ultimoIndirizzo(subnetmask, indirizzo_ip)}")

    """
    indirizzoIP.subnetting(subnetmask, n_sottoreti, indirizzo_ip)
    

if __name__ == "__main__":
    main()