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
archivo.close()#Cierra el archivo
