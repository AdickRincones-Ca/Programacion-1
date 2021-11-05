texto="Bnos. tardes Estimados Estudiantes. No olviden el uso del hashtag#teleprgm1 en el asunto de los correos en esta materia. Las consultas, por el grupo de whatsapp o exclusivamente al correo con el hashtag:#teleprgm1_cnslt. Por favor, no omitan esta práctica, de lo contrario, corremos el riesgo de que sus comunicaciones se pierdan. Agradecido por la comprensión"
lista=["a","e","i","o","u","A","E","I","O","U","á","é","í","ó","ú","Á","É","Í","Ó","Ú"]
a=0

#función del total de cada vocal en el texto
def icont(texto, lista):
    b=0
    for vl in lista:
        for vt in texto:
            if vl==vt:
                b+=1
        print(vl, "=", b)
        b=0

#función del total de vocales en el texto
def contador(texto,a):
    for cont in texto:
        if cont in "aeiouAEIOUáéíóú":
            a+=1
    return(a)

#función de cada vocal en el texto
def caracter(texto):
    for caracter in texto:
        if caracter in "aeiouAEIOUáéíóú":
            print(caracter)

#llamado de funciones
icont(texto, lista)
print("el total de vocales =", contador(texto,a))
caracter(texto)