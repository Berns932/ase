# Se añaden las bibliotecas que se usarán probalemente
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

died = pd.read_csv(r'C:\Users\berja\iCloudDrive\Ibero\4° Semestre\Ciencia De Datos\ASE\Datos proyecto ASE\Defunciones.csv')       #Número de defunciones por año
deaths = pd.read_csv(r'C:\Users\berja\iCloudDrive\Ibero\4° Semestre\Ciencia De Datos\ASE\Datos proyecto ASE\Mortalidad_08.csv')   #Número de homicidios dolosos
pob = pd.read_csv(r"C:\Users\berja\iCloudDrive\Ibero\4° Semestre\Ciencia De Datos\ASE\Datos proyecto ASE\Población2020.csv")      #Población total al fin de las décadas
gStudies=pd.read_csv(r"C:\Users\berja\iCloudDrive\Ibero\4° Semestre\Ciencia De Datos\ASE\Datos proyecto ASE\Educacion_05(1).csv")   #grado Promedio estudios
muestraS=pd.read_csv(r"C:\Users\berja\iCloudDrive\Ibero\4° Semestre\Ciencia De Datos\ASE\Datos proyecto ASE\AñosEstudiosMuestra.csv")   #grado Promedio estudios muestra
muestraD=pd.read_csv(r"C:\Users\berja\iCloudDrive\Ibero\4° Semestre\Ciencia De Datos\ASE\Datos proyecto ASE\HomicidiosMuestra.csv")
muestraTH=pd.read_csv(r"C:\Users\berja\iCloudDrive\Desktop\HomsMuestraTot.csv")   #Número de homicidios dolosos muestra
deathsAge=pd.read_csv(r"C:\Users\berja\iCloudDrive\Ibero\4° Semestre\Ciencia De Datos\ASE\Datos proyecto ASE\DefuncionesPorEdades.csv")   #tasa de crimen
CDMX_HM=pd.read_csv(r"C:\Users\berja\iCloudDrive\Desktop\HvsM_CDMX.csv")
CHIH_HM= pd.read_csv(r"C:\Users\berja\iCloudDrive\Desktop\HvsM_CHIH.csv")
GTO_HM = pd.read_csv(r"C:\Users\berja\iCloudDrive\Desktop\HvsM_GTO.csv")
MEX_HM = pd.read_csv(r"C:\Users\berja\iCloudDrive\Desktop\HvsM_MÉX.csv")
Income = pd.read_csv(r"C:\Users\berja\iCloudDrive\Ibero\4° Semestre\Ciencia De Datos\ASE\Datos proyecto ASE\IngresosMuestra.csv")
NAC_HM = pd.read_csv(r"C:\Users\berja\iCloudDrive\Desktop\HvsM_Nac.csv")

print(died)
print(pob)
print(deaths)
print(deathsAge)

print ("\nDescripción muestras.")
mTHT=muestraTH.T
mDT=muestraD.T
mST=muestraS.T
mTHT = mTHT.drop(['Año'], axis=0)
mDT = mDT.drop(['Año'], axis=0)
mST = mST.drop(['Año'], axis=0)

print('\n\nAnálisis inicial Homicidios')
print(mTHT)
print('\nDescripción dataframe')
print(mTHT.describe())
print('\nInformación relevante para el manejo de los datos')
print(muestraTH.info())

print('\n\nAnálisis inicial defunciones')
print (mDT)
print('\nDescripción dataframe')
print(mDT.describe())
print('\nInformación relevante para el manejo de los datos')
print(muestraD.info())

print('\n\nAnálisis inicial de los años de estudios promedio')
print(mST)
print('\nDescripción dataframe')
print(mST.describe())
print('\nInformación relevante para el manejo de los datos')
print(muestraS.info())

