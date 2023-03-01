class Figura:
    def __init__(self, lungh):
        self.lato = lungh
    
    def perim(self):
        perim = self.lato*4
        return f"perimetro = {perim}"

    def area(self):
        area = self.lato * self.lato
        return f"area = {area}"


def lungh(t1,t2):

    somma_punti = (t2[1][0]-t1[0][0]) + (t2[1][1]-t1[0][1])
    return (somma_punti)**0.5


def main():
    
    a = lungh((1,2),(4,5))

    print(a)

    figura = Figura(a)
    print(figura.area())
    print(figura.perim())
    

if __name__ == "__main__":
    main()