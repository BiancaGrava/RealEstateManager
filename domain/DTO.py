class DTO:
    def __init__(self,id,adresa,pret):
        self.__id=id
        self.__pret=pret
        self.__adresa=adresa
        self.__media=0
        self.__comision=0
    def get_id(self):
        return self.__id
    def get_adresa(self):
        return self.__adresa
    def get_pret(self):
        return self.__pret
    def get_media(self):
        return self.__media
    def get_comision(self):
        return self.__comision

    def set_comision(self,tip):
        pret=self.__pret
        if tip=="vanzare":
            self.__comision=2*pret/100
        elif tip=="inchiriere":
            self.__comision=pret/2

    def set_media(self,nr):
        self.__media=nr

    def __str__(self):
        return f"Strada imobilului: {self.__adresa}, comision aferent: {self.__comision}"