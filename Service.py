from domain import DTO
from Repository import FileRepoImo
class ImoService:
    def __init__(self,repo):
        self.__repo=repo

    def transaction(self,id,price):
        try:
            ob=self.__repo.cautare_dupa_id(id)
            adr=ob.get_adresa()
            util=DTO(id,adr,price)
            util.set_comision(ob.get_tip())
            return util
        except Exception as ex:
            raise Exception(ex)
    def media(self,tip):
        if tip not in ["vanzare","inchiriere"]:
            raise Exception("tipul trebuie sa fie vamzare sau inchiriere"+"\n"+"tip gresit!")
        try:
            lista=self.__repo.get_all()
            nrt=0
            prettot=0
            for obj in lista:
                if obj.get_tip()==tip:
                    nrt+=1
                    prettot+=obj.get_pret()
            if nrt!=0:
                media=prettot/nrt
                return media
            else:
                raise Exception("nu exista tranzactii de tipul cerut")
        except Exception as ex:
            raise Exception(ex)

def test_media():
    repo=FileRepoImo("D:\\trimestrul 4 2023\\UBB\\lab uri python\\Simulare_pregatiri\\simulare_DOMINO\\test.txt")
    serv=ImoService(repo)
    media=serv.media("vanzare")
    assert media==35000
test_media()
