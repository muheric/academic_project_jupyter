import pandas as pd
from matplotlib import pyplot as plt
%matplotlib inline
from datetime import date
#pour creer les noms des figures que tu vas generer
#J'utilise la date pour reference, et le nom tu peux le changer a ta preference
today=date.today()
today=today.strftime("%b-%D-%Y")
graphique_name=f"change_mon_nom_pour_sauvegarde.{today}"
#lecture du fichier excel et creation du data frame avec pandas pour avoir un object a utiliser
data=pd.read_excel('New_Data_Aristide.xlsx')
df=pd.DataFrame(data)
#ici le No. me gener bcp, j'ai renommer les titre du fichier excel, seulement No. change en Numero, le reste ne change pas
df = df.rename(columns={'No.': 'Numero', 'M': 'M', 'BFD':'BFD','RFF':'RFF','MBFD':'MBFD','FFD':'FFD','GWOVMP':'GWOVMP'})
# je cree le graphique

fig = plt.figure(figsize=(12, 10))
df.plot(x='M',y=["BFD","RFF","MBFD","FFD","GWOVMP"],kind='bar',marker='o')
plt.title("Representation des MVs placees dans PMs infonuagique")#titre du graphique en general
plt.xlabel("Nombre de machines virtueles")#abscice
plt.ylabel("Nombre de PMs actives")#ordonnees
fig.savefig(graphique_name,dpi=200)#sauvegarder le graphique