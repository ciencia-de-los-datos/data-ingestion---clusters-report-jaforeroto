"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re



def ingest_data():

    #Se crea el objeto con el archivo de texto llamada "datos"
    datos = "clusters_report.txt"
    hd1 = []
    texto = []

    #Se abre el archivo y se leen las 2 primeras líneas para encabezado agregándolas a una lista
    textnoformat = open(datos, mode='r')
    hd1.append(textnoformat.readline())
    hd1.append(textnoformat.readline())

    #Cada línea es separada como una lista de ancho fijo y se reemplazan los valores de hd1
    for ind, i in enumerate(hd1):
        hd1[ind] = ([i[:9], i[9:25].replace("\n",''), i[25:41].replace("\n",''), i[41:].replace("\n",'')])

    #Son juntados las filas 0 y 1 para formar encabezado compuesto
    hd1[0] = list(zip(hd1[0], hd1[1]))

    #Se procede a eliminar la fila 1 que se junto con la fila 0
    hd1.pop(1)

    #Se juntan las tuplas de cada columna como cadena de texto para titulo de columna. Se limpian espacios en blanco múltiples con split() y join reemplazandolos por '_'. Se hace lowercase
    for ind, x in enumerate(hd1[0]):
        hd1[0][ind] = '_'.join(''.join(x).split()).lower()

    #Se leen 2 líneas 'sobrantes'
    textnoformat.readline()
    textnoformat.readline()

    #Se lee y se cierra el resto del archivo
    cra = textnoformat.read()
    textnoformat.close()

    #Se reemplazan multiples espacios en blanco por uno solo
    cra = ' '.join(''.join(cra).split())

    #Separa el texto en elementos de lista, partiendo por el caracter '.'
    cra = cra.split('.')

    #Se elimina la última debido a que no es necesaria
    cra.pop()

    #Se crean variables para solventar problema de filas 6 y 7 que no se separan por no tener punto al final del 6
    aux1 = []
    aux2 = []

    aux1 = re.split('([o][l][ ])+',cra[5])[0] + re.split('([o][l][ ])+',cra[5])[1]
    aux2 = re.split('([o][l][ ])+',cra[5])[2]

    cra[5] = aux1
    cra.insert(6, aux2)

    #Se llena la lista con listas de cada fila del archivo, partidas por el caracter '%'
    for i in cra:
        texto.append(i.split('%')[0].replace(',','.').split()+[i.split('%')[1].strip()])

    #Se crea el DataFrame a partir de la lista de listas y con nombres de columnas
    df = pd.DataFrame(texto)
    df.columns = hd1[0]
    df['cluster'] = pd.to_numeric(df['cluster'])
    df['cantidad_de_palabras_clave'] = pd.to_numeric(df['cantidad_de_palabras_clave'])
    df['porcentaje_de_palabras_clave'] = pd.to_numeric(df['porcentaje_de_palabras_clave'])

    return df
