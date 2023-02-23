import json
with open("Clientes.json") as fichero:
    datos = json.load(fichero)

#print(datos)
def menu():
    print("Menú")
    print("----------------------------------------------------")
    print("1. Mostrar todos los clientes que han comprado kiwi.")
    print("2. Contar la cantidad de kiwi vendido.")
    print("3. Mostrar el nombre y el DNI de los clientes que empiezan por una subcadena")
    print("6. Salir")
    print("----------------------------------------------------")
    opcion = int(input("Introduce tu opcion: "))
    return(opcion)

def mostrarkiwi():
   for i in datos:
      #print(i["Orders"])
      for x in i["Orders"]:
         #print(x["Item"])
          if x["Item"] == "kiwi":
               print(i["FirstName"],i["LastName"])

def cantidadkiwi():
    cantidad = 0
    for i in datos:
        #print(i["Orders"])
        for x in i["Orders"]:
            #print(x["Item"])
            if x["Item"] == "kiwi":
                cantidad = cantidad + x["Quantity"]
    print("Se han comprado",cantidad,"kg de kiwi")

def subcadena():
    sub = input("Introduce la subcadena por la que empeiza el nombre: ")
    for i in datos:
        if i["FirstName"].capitalize().startswith(sub.capitalize()):
            print("Nombre:",i["FirstName"],"- Apellido:",i["LastName"],"- DNI:",i["CartId"])