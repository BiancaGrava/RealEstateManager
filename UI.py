class Consola:
    def __init__(self,serv):
        self.__service=serv
        self.__comenzi={
            "media":self.__ui_media,
            "tranzactie":self.__ui_transaction
            }
    def __ui_media(self,params):
        if len(params)!=1:
            print("nr parametrii incorect!")
        else:
            try:
                tip=params[0].strip()
                media=self.__service.media(tip)
                print("media ceruta este: ")
                print(media)
            except Exception as ex:
                print(ex)
    def __ui_transaction(self,params):
        if len(params)!=2:
            print("nr parametrii incorect")
        else:
            try:
                id=int(params[0].strip())
                price=int(params[1].strip())
                obj=self.__service.transaction(id,price)
                print(obj)
            except Exception as ex:
                print(ex)
    def run(self):
        while True:
            input_initial=input("dati o comanda: ")
            if input_initial=="exit":
                return
            else:
                partile_comenzii=input_initial.strip().split(">")
                numele_comenzii=partile_comenzii[0]
                if len(partile_comenzii)==1:
                    params=[]
                else:
                    params=partile_comenzii[1].strip().split(",")
                if numele_comenzii in self.__comenzi:
                    try:
                        self.__comenzi[numele_comenzii](params)
                    except Exception as ex:
                        print(ex)
                else:
                    print("numele comenzii este incorect")