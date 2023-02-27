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
    print("4. Mostrar el nombre de un comprador y la cantidad de fruta que ha comprado")
    print("5. Mostrar la cantidad maxima de fruta comprada por un cliente")
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

def compradores():
    fruta = input("Introduce una fruta ")
    for i in datos:
        for x in i["Orders"]:
          if x["Item"] == fruta:
            print(i["FullName"],":",x["Quantity"])  

def maxcantidad():
    cantidad = []
    nombre = input("Introduce un nombre ")
    for i in datos:
        if i["FirstName"] == nombre:
            for x in i["Orders"]:
                cantidad.append(x["Quantity"])
                if x["Quantity"] == max(cantidad):
                    print("La compra de mas cantidad de",i["FirstName"],"ha sido",x["Item"]) 
    if i["FirstName"] != nombre:
        print("No se ha encontrado esa persona")    
