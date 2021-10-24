import matplotlib.pyplot as plt
import scrap

scrap.scrap()
liste_bitcoin = []
with open(r"jet 1\bitcoin\bitcoin_liste.txt", "r") as f:
   liste_bitcoin = f.read().splitlines()

liste_date = []
with open(r"jet 1\bitcoin\date.txt", "r") as f:
   liste_date = f.read().splitlines()

plt.title("Prix du bitcoin en fonction du temps")
plt.plot(liste_date, liste_bitcoin)
plt.xlabel('Temps')
plt.ylabel('Bitcoin (en €)')
plt.show()