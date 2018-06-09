import numpy as np
import matplotlib.pyplot as pl

data = np.loadtxt(r"c:\Users\User\Documents\data.txt", dtype=[("saat", np.int),("Basvuru",np.int),("Olumsuz",np.int)])

#LINE CHART
pl.plot(data["saat"],data["Basvuru"],label="Başvurular")
pl.plot(data["saat"],data["Olumsuz"], label="Olumsuzlar")
pl.title("24 Saatlik Başvurular")
pl.legend(loc=2)
pl.xlabel("Saat")
pl.ylabel("Sonuç")
pl.show()

#BAR CHART
pl.bar(data["saat"],data["Basvuru"])
pl.xlabel("Saat")
pl.ylabel("Sonuç")

#PIE CHART
colors = ["red","green","blue","orange"]
labels = ["1","2","3","4","5","6"]
total=sum(data["Olumsuz"])
pl.pie(data["Olumsuz"], colors=colors, labels=labels,shadow=True,autopct=lambda p: '{:.0f}'.format(p * total / 100))
pl.show()
