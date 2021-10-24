def scrap():
    import requests
    from bs4 import BeautifulSoup
    import time

    requete = requests.get("https://www.boursorama.com/bourse/devises/taux-de-change-bitcoin-dollar-BTC-USD/")
    page = requete.content
    soup = BeautifulSoup(page, features="lxml")

    string = soup.find("span", {"class": "c-instrument c-instrument--last"})
    i=1
    for lettre in string:
        if i > 62 and i < 73:
            prix = prix + lettre
    prix = lettre

    liste_bitcoin = []
    with open(r"jet 1\bitcoin\bitcoin_liste.txt", "r") as f:
        liste_bitcoin = f.read().splitlines()

    liste_final = liste_bitcoin
    liste_final.append(prix)

    with open(r"jet 1\bitcoin\bitcoin_liste.txt", "w") as f:
        for item in liste_final:
            f.write(f'{item}\n')

    liste_date = []
    with open(r"jet 1\bitcoin\date.txt", "r") as f:
        liste_date = f.read().splitlines()

    import datetime

    date = str(datetime.datetime.now())
    i = 1
    final = ""
    for letter in date:
        if i <= 10:
            final =  final + letter
        i = i + 1

    liste_date_final = liste_date
    liste_date_final.append(final)

    with open(r"jet 1\bitcoin\date.txt", "w") as f:
        for item in liste_date_final:
            f.write(f'{item}\n')