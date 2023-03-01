PERICOLO = 100

class Robot():
    def __init__(self, nome, peso, tipo):
        self.nome = nome
        self.peso = peso
        self.tipo = tipo

    def stampa(self):
        return f"nome robot = {self.nome}"

    def verifica(self):
        if(self.peso>=PERICOLO and self.nome == "umanoide"):
            return True
        else:
            return False

        

def main():
    robot1 = Robot("alexa", 30, "umanoide")
    robot2 = Robot("siri", 130, "umanoide")

    print(robot1.stampa())
    print(robot2.stampa())
    
    if(robot1.verifica == True):
        print(f"{robot1.stampa()} può essere pericoloso")

    if(robot2.verifica):
        print(f"{robot2.stampa()} può essere pericoloso")


if __name__ == "__main__":
    main()