import json

def abrirJSON():
    dicFinal={}
    with open("./camper.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./camper.json",'w') as outFile:
        json.dump(dic,outFile)
d={}
zzz = True
while zzz == True:
    d=abrirJSON()
    print("Bienvenido a la plataforma, cual es tu rol?")
    print("1. ¿Eres camper?")
    print("2. ¿Eres trainer?")
    print("3. ¿Eres administrador?")
    persona = int(input(": "))
    if persona ==1:
        iterador=1
        ID=int(input("¿Cual es su ID?"))
        for i in range (iterador+1):
            z=str(i)
            if ID==d["Estudiantes"][z]["#NumeroDeIdentificacion"]:
                print("Que deseas hacer", d["Estudiantes"][z]["Nombres"], "?")

            else:
                iterador=iterador+1
