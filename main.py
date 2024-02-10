from Repository import FileRepoImo
from Service import ImoService
from UI import Consola
def main():
    repo=FileRepoImo("D:\\trimestrul 4 2023\\UBB\\lab uri python\\Simulare_pregatiri\\simulare_DOMINO\\imobiliare.txt")
    service=ImoService(repo)
    cons=Consola(service)
    cons.run()
main()