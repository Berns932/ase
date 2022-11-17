# Se añaden las bibliotecas que se usarán probalemente
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from scipy import stats

# hOLA!

an=0.40     #Ancho para gráficas

# Se carga el dataframe
died = pd.read_csv(r'C:\Users\berja\Desktop\Defunciones.csv')       #Número de defunciones por año
deaths = pd.read_csv(r'C:\Users\berja\Desktop\Mortalidad_08.csv')   #Número de homicidios dolosos
pob = pd.read_csv(r"C:\Users\berja\Desktop\Población2020.csv")      #Población total al fin de las décadas
gStudies=pd.read_csv(r"C:\Users\berja\Desktop\Educacion_05(1).csv")   #grado Promedio estudios
muestraS=pd.read_csv(r"C:\Users\berja\Desktop\AñosEstudiosMuestra.csv")   #grado Promedio estudios muestra
muestraD=pd.read_csv(r"C:\Users\berja\Desktop\HomicidiosMuestra.csv")   #Número de homicidios dolosos muestra
deathsAge=pd.read_csv(r"C:\Users\berja\Desktop\DefuncionesPorEdades.csv")   #tasa de crimen
CDMX_HM=pd.read_csv(r"C:\Users\berja\Desktop\HvsM_CDMX.csv")
CHIH_HM= pd.read_csv(r"C:\Users\berja\Desktop\HvsM_CHIH.csv")
GTO_HM = pd.read_csv(r"C:\Users\berja\Desktop\HvsM_GTO.csv")
MEX_HM = pd.read_csv(r"C:\Users\berja\Desktop\HvsM_MÉX.csv")
Income = pd.read_csv(r"C:\Users\berja\Desktop\IngresosMuestra.csv")

#Se eliminan las filas que no son necesarias
died=died.drop([0,33], axis=0)
deaths=deaths.drop([0], axis=0)
pob=pob.drop([0],axis=0)
gStudies.drop([0],axis=0, inplace= True)
gStudies=gStudies.drop(gStudies.index[32:], axis=0)

"""
#Se crea una gráfica de la población en 2010 y 2020
x = np.arange(len(pob['Entidad Federativa']))
fig, ax = plt.subplots()
y1 = pob['Total 2010']
y2 = pob['Total 2020']
plt.bar(x-an/2,y1,an,color="silver",label="2010")
plt.bar(x+an/2,y2,an,color="blue",label="2020")
ax.set_xticks(x)
ax.set_xticklabels(pob["Entidad Federativa"],rotation=90)
plt.title("Población 2010-2020")
plt.xlabel("Entidades Federativas")
plt.ylabel("Cantidad")
plt.legend()
plt.show()

#Gráfica de defunciones por estado de algunos años importantes
x = np.arange(len(deaths['Entidad Federativa']))
fig, ax = plt.subplots()
plt.bar(x-an/2,died["2017"],an,color="silver",label="2017")
plt.bar(x,died["2019"],an,color="grey",label="2019")
plt.bar(x+an/2,died["2021"],an,color="blue",label="2021")
ax.set_xticks(x)
ax.set_xticklabels(deaths["Entidad Federativa"],rotation=90)
plt.title("Defunciones 2017-2021")
plt.xlabel("Entidades Federativas")
plt.ylabel("Cantidad")
plt.legend()
plt.show()

#Gráfica de homicidios dolosos por entidad federativa de algunos años importantes
x = np.arange(len(deaths['Entidad Federativa']))
y1 = deaths['Total 2021']
y2 = deaths['Total 2019']
y3 = deaths['Total 2017']
fig, ax = plt.subplots()
ax.bar(x-an/2, y3, an, color="silver", label="2017")
ax.bar(x, y2, an, color="grey", label="2019")
ax.bar(x+an/2, y1, an, color='blue',label="2021")
ax.set_xticks(x)
ax.set_xticklabels(deaths["Entidad Federativa"],rotation=90)
plt.title("Homicidios Dolosos 2017-2021")
plt.xlabel("Entidades Federativas")
plt.ylabel("Cantidad")
plt.legend()
plt.show()

#Gráfica años promedio de estudios por entidad federativa de algunos años importantes
x = np.arange(len(gStudies['Entidad Federativa']))
y1 = gStudies['Total 2020']
y2 = gStudies['Total 2015']
y3 = gStudies['Total 2010']
fig, ax = plt.subplots()
ax.bar(x-an/2, y3, an, color="silver", label="2010")
ax.bar(x, y2, an, color="grey", label="2015")
ax.bar(x+an/2, y1, an, color='blue',label="2020")
ax.set_xticks(x)
ax.set_xticklabels(gStudies["Entidad Federativa"],rotation=90)
plt.title("Años promedio estudios")
plt.xlabel("Entidades Federativas")
plt.ylabel("Cantidad")
plt.legend()
plt.show()


x = muestraD['Año']
y1 = muestraD['CHIH']
y2 = muestraS['CHIH']
# Plot Line1 (Left Y Axis)
fig, ax1 = plt.subplots(1,1,figsize=(16,9), dpi= 80)
ax1.plot(x, y1, color='tab:red')
# Plot Line2 (Right Y Axis)
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.plot(x, y2, color='tab:blue')
# Decorations graphs
# ax1 (left Y axis)
ax1.set_xlabel('Entidad Federativa', fontsize=20)
ax1.tick_params(axis='x', rotation=0, labelsize=12)
ax1.set_ylabel('#Homicidios', color='tab:red', fontsize=20)
ax1.tick_params(axis='y', rotation=0, labelcolor='tab:red' )
ax1.grid(alpha=.4)
# ax2 (right Y axis)
ax2.set_ylabel("#Años estudios)", color='tab:blue', fontsize=20)
ax2.tick_params(axis='y', labelcolor='tab:blue')
ax.set_xticks(np.arange(len(x)))
ax.set_xticklabels(x,rotation=90)
ax2.set_title("Chihuahua", fontsize=22)
fig.tight_layout()
plt.show()

x = muestraD['Año']
y1 = muestraD['CDMX']
y2 = muestraS['CDMX']
# Plot Line1 (Left Y Axis)
fig, ax1 = plt.subplots(1,1,figsize=(16,9), dpi= 80)
ax1.plot(x, y1, color='tab:red')
# Plot Line2 (Right Y Axis)
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.plot(x, y2, color='tab:blue')
# Decorations graphs
# ax1 (left Y axis)
ax1.set_xlabel('Entidad Federativa', fontsize=20)
ax1.tick_params(axis='x', rotation=0, labelsize=12)
ax1.set_ylabel('#Homicidios', color='tab:red', fontsize=20)
ax1.tick_params(axis='y', rotation=0, labelcolor='tab:red' )
ax1.grid(alpha=.4)
# ax2 (right Y axis)
ax2.set_ylabel("#Años estudios", color='tab:blue', fontsize=20)
ax2.tick_params(axis='y', labelcolor='tab:blue')
ax.set_xticks(np.arange(len(x)))
ax.set_xticklabels(x,rotation=90)
ax2.set_title("Ciudad de México", fontsize=22)
fig.tight_layout()
plt.show()

x = muestraD['Año']
y1 = muestraD['GTO']
y2 = muestraS['GTO']
# Plot Line1 (Left Y Axis)
fig, ax1 = plt.subplots(1,1,figsize=(16,9), dpi= 80)
ax1.plot(x, y1, color='tab:red')
# Plot Line2 (Right Y Axis)
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.plot(x, y2, color='tab:blue')
# Decorations graphs
# ax1 (left Y axis)
ax1.set_xlabel('Entidad Federativa', fontsize=20)
ax1.tick_params(axis='x', rotation=0, labelsize=12)
ax1.set_ylabel('#Homicidios', color='tab:red', fontsize=20)
ax1.tick_params(axis='y', rotation=0, labelcolor='tab:red' )
ax1.grid(alpha=.4)
# ax2 (right Y axis)
ax2.set_ylabel("# años estudios)", color='tab:blue', fontsize=20)
ax2.tick_params(axis='y', labelcolor='tab:blue')
ax.set_xticks(np.arange(len(x)))
ax.set_xticklabels(x,rotation=90)
ax2.set_title("Guanajuato", fontsize=22)
fig.tight_layout()
plt.show()

x = muestraD['Año']
y1 = muestraD['MÉX']
y2 = muestraS['MÉX']
# Plot Line1 (Left Y Axis)
fig, ax1 = plt.subplots(1,1,figsize=(16,9), dpi= 80)
ax1.plot(x, y1, color='tab:red')
# Plot Line2 (Right Y Axis)
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
ax2.plot(x, y2, color='tab:blue')
# Decorations graphs
# ax1 (left Y axis)
ax1.set_xlabel('Entidad Federativa', fontsize=20)
ax1.tick_params(axis='x', rotation=0, labelsize=12)
ax1.set_ylabel('#Homicidios', color='tab:red', fontsize=20)
ax1.tick_params(axis='y', rotation=0, labelcolor='tab:red' )
ax1.grid(alpha=.4)
# ax2 (right Y axis)
ax2.set_ylabel("#Años estudios)", color='tab:blue', fontsize=20)
ax2.tick_params(axis='y', labelcolor='tab:blue')
ax.set_xticks(np.arange(len(x)))
ax.set_xticklabels(x,rotation=90)
ax2.set_title("Estado de México", fontsize=22)
fig.tight_layout()
plt.show()

#Gráfica de homicidios por edades
x = deathsAge['Año']
y1= deathsAge['15-19 años']
y2= deathsAge['20-24 años']
y3= deathsAge['25-29 años']
y4= deathsAge['30-34 años']
y5= deathsAge['35-39 años']
y6= deathsAge['40-44 años']
y7= deathsAge['35-39 años']
plt.figure(figsize=(40, 10))
plt.plot(x, y1, label='15-19 años')
plt.plot(x, y2, label='20-24 años')
plt.plot(x, y3, label='25-29 años')
plt.plot(x, y4, label='30-34 años')
plt.plot(x, y5, label='35-39 años')
plt.plot(x, y6, label='40-44 años')
plt.plot(x, y7, label='45-49 años')
plt.xticks(rotation=45, horizontalalignment='right',fontweight='light', fontsize=20)
plt.xlabel('Año', fontsize=30)
plt.ylabel('#Homcidios', fontsize=30)
plt.title('Defunciones por homicidio por edades', fontsize=40)
plt.axhline(y=1985.84, color='red', linestyle='--', linewidth=3, label='Promedio a lo largo de los años')
plt.grid(True)
plt.legend()
plt.show()

data = CHIH_HM['Total']
labels = CHIH_HM['Género']
plt.pie(data, labels = labels, autopct='%.0f%%')
plt.title('Homicidios Chihuahua (CHIH)', fontsize=20)
plt.show()

data = CDMX_HM['Total']
labels = CDMX_HM['Género']
plt.pie(data, labels = labels, autopct='%.0f%%')
plt.title('Homicidios Ciudad de México (CDMX)', fontsize=20)
plt.show()

data = GTO_HM['Total']
labels = GTO_HM['Género']
plt.pie(data, labels = labels, autopct='%.0f%%')
plt.title('Homicidios Guanajuato (GTO)', fontsize=20)
plt.show()

data = MEX_HM['Total']
labels = MEX_HM['Género']
plt.pie(data, labels = labels, autopct='%.0f%%')
plt.title('Homicidios  Estado de México (MEX)', fontsize=20)
plt.show()
"""

x = np.arange(len(Income['Año']))
y1 = Income['CDMX']
y2 = Income['CHIH']
y3 = Income['GTO']
y4 = Income['MEX']
fig, ax = plt.subplots()
plt.plot(x, y1, label='CDMX')
plt.plot(x, y2, label='CHIH')
plt.plot(x, y3, label='GTO')
plt.plot(x, y4, label='MEX')
ax.set_xticks(x)
ax.set_xticklabels(Income['Año'])
plt.xlabel('Año', fontsize=15)
plt.ylabel('Ingresos (100mil mdp)', fontsize=15)
plt.title('Ingresos por año', fontsize=25)
plt.grid(True)
plt.legend()
plt.show()

y1 = Income['Total']
fig, ax = plt.subplots()
plt.plot(x,y1, label='Total')
plt.xticks()
ax.set_xticks(x)
ax.set_xticklabels(Income['Año'],rotation=90)
plt.title("Ingresos al año Nivel Nacional")
plt.xlabel("Años")
plt.ylabel("Cantidad (BdP)")
plt.legend()
plt.show()