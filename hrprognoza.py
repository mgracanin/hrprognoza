import requests
import xmltodict
from datetime import datetime

def aktualna_prognoza():
    '''
    Funkcija koja vraća aktualne vremenske podatke s Vrijeme.hr (meteo.hr)
    Vraća riječnik oblika {Grad: {Temperatura, Vlaga, Tlak, Smjer vjetra, Brzina vjetra, Vrijeme},...}
    '''
    try:
        url_prognoza = "https://vrijeme.hr/hrvatska1_n.xmla"
        prognoza = xmltodict.parse(requests.get(url=url_prognoza).content) ## preuzimamo i konvertiramo XML u dict

        return { ## vraćamo rječnik s podacima
                grad["GradIme"] : {
                        "Temperatura" : grad["Podatci"]["Temp"],
                        "Vlaga": grad["Podatci"]["Vlaga"],
                        "Tlak" : grad["Podatci"]["Tlak"],
                        "Smjer vjetra" : grad["Podatci"]["VjetarSmjer"],
                        "Brzina vjetra" : grad["Podatci"]["VjetarBrzina"],
                        "Vrijeme": grad["Podatci"]["Vrijeme"],
                        "Datum": datetime.now().timestamp()
                        #"Datum": datetime.now().strftime("%d. %m. %Y. %H:%M:%S")
                        } for grad in prognoza["Hrvatska"]["Grad"]
                }
    except Exception as e:
          return {"Greška" : {e}}


if __name__ == "__main__":
        
        ## Primjeri korištenja...
        prognoze = aktualna_prognoza()

        for grad in aktualna_prognoza().keys():
                print(f"{grad} : {prognoze[grad]}")

        lista_gradova = list(aktualna_prognoza().keys())
        print(lista_gradova)
