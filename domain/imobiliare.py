class Imobiliare:
    def __init__(self,id,adresa,pret,tip):
        self.__id=id
        self.__adresa=adresa
        self.__pret=pret
        self.__tip=tip

    def get_id(self):
        return self.__id
    def get_adresa(self):
        return self.__adresa
    def get_pret(self):
        return self.__pret
    def get_tip(self):
        return self.__tip

    def __eq__(self, other):
        return self.__id==other.get_id()

    def __str__(self):
        return f"{self.__id},{self.__adresa},{self.__pret},{self.__tip}"

def test_create():
    other = Imobiliare(23, "str.Cernei nr.10 Cluj-Napoca", 50000, "vanzare")
    assert other.get_id()==23

test_create()
