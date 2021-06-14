import re
print("Bienvenido\nHoy vamos a encontrar el numero de ocurrencias del libro 1 de Harry Potter\n")
archivo=open('Harry.txt',encoding='utf8')#carga el archivo

linea=archivo.readline()
dic={}
while linea!="":
    palabras=linea.split()
    for i in range(len(palabras)):
        palabra=re.sub('[?|.|!|\/|;|:|,|”|“|(|)]','',palabras[i])
        #Elimina los caracteres no deseados
        #No elimina ' y - por que podria cauasr muchas confuciones
        #Esos tendrian que ser con split pero no encuentro una manera de
        #adaptarlos para que no den problemas
        if palabra in dic:#revisa si existe la palabra
            dic[palabra]+=1#añade una ocurrencia
        else:
            dic.update({palabra:1})
    linea=archivo.readline()
print("Las palabras encontradas son:\Formato:(palabra,ocurrencias)")
for x in dic:#realiza una navegacion en el diccionarion
    print('({},{}) '.format(x,dic.get(x)))#imprime con formato
print("Esas son las palabras que hay en el archivo")  
print("Fin del comunicado")
print("Archivo editado")
print("Hola que hace XD")
print("A ver si funca")
#se han colocado los diferentes prints para que se vea bonito
#así se espera tener buena nota :_v 
print("Archivo editado")
print("Hola que hace XD")
print("A ver si funca")
#se han colocado los diferentes prints para que se vea bonito
#así se espera tener buena nota :_v 
print("Archivo editado")
print("Hola que hace XD")
print("A ver si funca")
#se han colocado los diferentes prints para que se vea bonito
#así se espera tener buena nota :_v 
print("Hola Mundo")
print("Como estan")
print("Prueba de funcionamiento")
#prueba de como funcionan los comandos básicos
#tener en cuneta que debe estar entre parentesis
#No Será de tomar un traguito??
#Segunda es todo
#todos los hombre mueren, pero no todos han vivido
#no hijo, ya no te creo
#que procede gente
#que le saquemos al Johan 
#no merece estar aquí
#Jaja ya marchó Johan
archivo.close()#Cierra el archivo
