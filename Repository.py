from domain import Imobiliare

class RepoImo:
    def __init__(self):
        self._imobile={}

    def cautare_elem(self,id):
        for key in list(self._imobile.keys()):
            if self._imobile[key].get_id()==id:
                return 1
        return 0

    """def cautare_dupa_id(self,id):
        if self.cautare_elem(id)==1:
            for id in list(self._imobile.keys()):
                if self._imobile[id].get_id()==id:
                    return self._imobile[id]
        else:
            raise Exception("nu exista id!")"""
    def cautare_dupa_id(self,id):
        if id not in self._imobile.keys():
            raise Exception("nu exista id\n")
        else:
            return self._imobile[id]

    def get_all(self):
        return [self._imobile[id] for id in self._imobile.keys()]

    def __len__(self):
        return len(self._imobile)



class FileRepoImo(RepoImo):
    def __init__(self,calef):
        RepoImo.__init__(self)
        self.__calef=calef

    def __read_all_imo_from_file(self):
        with open(self.__calef,"r") as f:
            self._imobile.clear()
            lines=f.readlines()
            for line in lines:
                if line!="":
                    parts=line.strip().split(",")
                    id=int(parts[0])
                    adresa=parts[1]
                    pret=int(parts[2])
                    tip=parts[3]

                    imo=Imobiliare(id,adresa,pret,tip)
                    self._imobile[id]=imo

    def __write_all_imo_to_file(self):
        with open(self.__calef,"w") as f:
            for id in self._imobile.keys():
                f.write(str(self._imobile[id])+"\n")

    def cautare_dupa_id(self,id):
        self.__read_all_imo_from_file()
        return RepoImo.cautare_dupa_id(self,id)

    def get_all(self):
        self.__read_all_imo_from_file()
        return RepoImo.get_all(self)


def test_cautare():
    repo=FileRepoImo("D:\\trimestrul 4 2023\\UBB\\lab uri python\\Simulare_pregatiri\\simulare_DOMINO\\test.txt")
    obj=repo.cautare_dupa_id(23)
    assert obj.get_id()==23
    other=Imobiliare(23,"str.Cernei nr.10 Cluj-Napoca",50000,"vanzare")
    assert  obj==other
def test_get_all():
    repo=FileRepoImo("D:\\trimestrul 4 2023\\UBB\lab uri python\\Simulare_pregatiri\\simulare_DOMINO\\test.txt")
    lista=repo.get_all()
    other1=Imobiliare(23,"str.Cernei nr.10 Cluj-Napoca",50000,"vanzare")
    other2=Imobiliare(24,"str.av nr.2 Cluj-Napoca",20000,"vanzare")
    assert lista==[other1,other2]
test_get_all()
test_cautare()
