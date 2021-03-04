import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Euro Verisi
series1 = "TP.DK.EUR.S.YTL"
series_name1 = "Euro_Kuru"
startDate1 = "01-01-2021"
endDate1 = "01-02-2021"
typee1 = "csv"
key1 = "rHYQAEabPJ"
aggregaitonTypes1 = "avg"
formulas1 = "0"
frequency1 = "2"

url1 = 'https://evds2.tcmb.gov.tr/service/evds/series={}&' \
       'startDate={}&endDate={}&type={}&key={}&' \
       'aggregationTypes={}&formulas={}&frequency={}'.format(series1, startDate1, endDate1, typee1,
                                                             key1, aggregaitonTypes1, formulas1, frequency1)
euro = pd.read_csv(url1)
euro.drop("UNIXTIME", axis = 1, inplace = True)
euro.set_index("Tarih", inplace = True)
euro.rename(columns= {series1.replace(".", "_"): series_name1}, inplace = True)
euro.dropna(how = "any", inplace = True)
euro = round(euro, 2)
print(euro.head())

#Euro Grafik

plt.figure(figsize=(16,8))

sns.set_style("whitegrid")
p1 = sns.pointplot(x=euro.index, y=euro[series_name1], color='#22b2da', alpha=0.5)

for line in range(0,euro.shape[0]):
     p1.text(line, euro[series_name1].iloc[line]+0.03, euro[series_name1].iloc[line],
             horizontalalignment='left', size='medium', color='black', weight='semibold')

plt.xticks(rotation= 90)

plt.xlabel('\nTarih',fontsize = 15)
plt.ylabel(series_name1+"\n",fontsize = 15)

plt.title(series_name1+"\n",fontsize = 20, weight='semibold')

resimadi= "Euro Kuru.png".format(series_name1, euro.iloc[euro.shape[0]-1].name)
plt.savefig(resimadi,dpi=200)
plt.show()
