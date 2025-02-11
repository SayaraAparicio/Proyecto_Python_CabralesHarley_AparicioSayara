import json
def abrirJSON():
    dicFinal={}
    with open("./campers.Json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./campers.Json",'w') as outFile:
        json.dump(dic,outFile)
d={}
zzz = True
while zzz == True:
    d=abrirJSON()
    print("1.Inicia Sesion")
    print("2.Registrarse")
    op=int(input(":"))
    if op ==2:
         nom=(input("Ingresa tus nombres: "))
         apl=(input("Ingresa tus apellidos: "))
         direc=(input("Ingresa tu direccion: "))
         acu=(input("Ingresa el nombre de tu acudiente: "))
         num=(input("Ingresa tu telefono: "))
         for i in range(len(d["Campers"]),len(d["Campers"])+1):
             nes=len(d["Campers"])
             print("Tu #Numero de identificacion es: ",nes)
             contraseña1=int(input("Añadir contraseña: "))
             f=len(d["Campers"])
             d["Campers"][f]={"#NumeroDeIdentificacion": nes,
             "Contraseña": contraseña1,
             "Nombres": nom,
             "Apellidos": apl,
             "Direccion": direc,
             "Acudiente": acu,
             "TelefonosDeContacto": num,
             "Estado": "",
             "Riesgo": "",
             "Jornada": "",
             "Notas":{"Proyecto60% ":"","Filtro30%":"","Trabajos10%":""}}
             guardarJSON(d)
    if op==1:
        print("Bienvenido a la plataforma, cual es tu rol?")
        print("1. ¿Eres camper?")
        print("2. ¿Eres trainer?")
        print("3. ¿Eres administrador?")
        persona = int(input(": "))
        if persona ==1:
             ID=int(input("¿Cual es su ID?"))
             CONTRA=int(input("¿Cual es su contraseña?"))
             m=False
             for i in range (len(d["Campers"])):
                 z=str(i)
                 if ID==d["Campers"][z]["#NumeroDeIdentificacion"]:
                    a=z
                    if CONTRA==d["Campers"][a]["Contraseña"]:
                     m=True
                     z1=True
                     
                         

                     while z1==True:
                        print("Que deseas hacer", d["Campers"][z]["Nombres"], "?")     
                        print("1. Ver tu informacion")
                        print("2. Ver tus notas")
                        print("3. Ver tu horario y salon asignado")
                        print("4. Cerrar sesion")
                        opc=int(input(": "))
                        if opc==1:
                            for i in range (1):
                                ssss=str(i)
                                id1=d["Campers"][a]["#NumeroDeIdentificacion"]
                                co1=d["Campers"][a]["Contraseña"]
                                nom1=d["Campers"][a]["Nombres"]
                                apl1=d["Campers"][a]["apellidos"]
                                dir1=d["Campers"][a]["Direccion"]
                                acu1=d["Campers"][a]["acudiente"]
                                tel1=d["Campers"][a]["Telefonos"]
                                est1=d["Campers"][a]["Estado"]
                                ris1=d["Campers"][a]["Riesgo"]
                                jor1=d["Campers"][a]["Jornada"]
                                not1=d["Campers"][a]["Notas"]
                                print("ID: ",id1," contraseña: ",co1," Nombres: ",nom1," Apellidos: ",apl1," Direccion: ",dir1," Acudiente: ",acu1," Telefono de contacto: ",tel1," Estado: ",est1," Riesgo: ",ris1," Jornada: ",jor1," Notas",not1)
                        if opc==4:
                            z1=False
             if m==False:
              print("Contraseña o usuario icorrectos")
        if persona==2:
             ID=int(input("¿Cual es su ID?"))
             CONTRA=int(input("¿Cual es su contraseña?"))
             m=False
             for i in range (len(d["Trainers"])):
                 z=str(i)
                 if ID==d["Trainers"][z]["NumeroDeIdentificacion"]:
                    a=z
                    if CONTRA==d["Trainers"][a]["Contraseña"]:
                     m=True
                     z2=True
                     while z2==True:
                        print("Que deseas hacer", d["Trainers"][z]["Nombres"], "?")  
                        print("1.Ver tu informacion")
                        print("2. ver tus horarios")
                        print("3. Ver tus estudiantes")   
                        print("4. Modificar notas")
                        print("5. Cerrar sesion")
                        opc=int(input(": "))
                        if opc==1:
                           print(d["Trainers"][a])
                        if opc==5:
                            z2=False
             if m==False:
               print("Contraseña o usuario icorrecto")
                     

        if persona==3:
             ID=int(input("¿Cual es su ID?"))
             CONTRA=int(input("¿Cual es su contraseña?"))
             m=False
             for i in range (len(d["Coordinadores"])):
                 z=str(i)
                 if ID==d["Coordinadores"][z]["NumeroDeIdentificacion"]:
                    a=z
                    if CONTRA==d["Coordinadores"][a]["Contraseña"]:
                     m=True
                     z3=True
                     while z3==True:
                       print("Que deseas hacer", d["Coordinadores"][z]["Nombres"], "?")  
                       print("1. Ver los estudiantes, trainers y Coordinadores")
                       print("2. Ver la informacion de cada grupo")
                       print("3. Modificar informacion de estudiantes, trainers y coordinadores")
                       print("4. Asignar horarios a los trainers")
                       print("5. Cambiar estado de los estudiantes")
                       print("6. modificar los grupos")
                       print("7. Añadir aulas")
                       print("8. Asignar campers a su grupo")
                       print("9. Cerrar sesion")
                       opc=int(input(": "))
                       if opc==1:
                           print("A quein deseas verle la informacion")
                           print("1. Campers")
                           print("2. Trainers")
                           print("3. Coordinadores")
                           opcc=int(input(": "))
                           if opcc==1:
                               for i in range (len(d["Campers"])):
                                ssss=str(i)
                                id1=d["Campers"][ssss]["#NumeroDeIdentificacion"]
                                co1=d["Campers"][ssss]["Contraseña"]
                                nom1=d["Campers"][ssss]["Nombres"]
                                apl1=d["Campers"][ssss]["apellidos"]
                                dir1=d["Campers"][ssss]["Direccion"]
                                acu1=d["Campers"][ssss]["acudiente"]
                                tel1=d["Campers"][ssss]["Telefonos"]
                                est1=d["Campers"][ssss]["Estado"]
                                ris1=d["Campers"][ssss]["Riesgo"]
                                jor1=d["Campers"][ssss]["Jornada"]
                                not1=d["Campers"][ssss]["Notas"]
                                print("ID: ",id1," contraseña: ",co1," Nombres: ",nom1," Apellidos: ",apl1," Direccion: ",dir1," Acudiente: ",acu1," Telefono de contacto: ",tel1," Estado: ",est1," Riesgo: ",ris1," Jornada: ",jor1," Notas",not1)
                           if opcc==2:
                               for i in range (len(d["Trainers"])):
                                ssss=str(i)
                                id1=d["Trainers"][ssss]["NumeroDeIdentificacion"]
                                co1=d["Trainers"][ssss]["Contraseña"]
                                nom1=d["Trainers"][ssss]["Nombres"]
                                apl1=d["Trainers"][ssss]["apellidos"]
                                hor1=d["Trainers"][ssss]["Horarios"]
                                rut1=d["Trainers"][ssss]["Ruta"]
                                est1=d["Trainers"][ssss]["Estado"]

                                print("ID: ",id1," contraseña: ",co1," Nombres: ",nom1," Apellidos: ",apl1," Horario: ",hor1," Ruta: ",rut1," Estado: ",est1)
                       if opc==6:
                            for i in range (len(d["Trainers"])):
                                ssss=str(i+1)
                                idd1=d["Grupos"][ssss]["Horario"]
                                con1=d["Grupos"][ssss]["Aula"]
                                nom1=d["Grupos"][ssss]["Ruta"]
                                apl1=d["Grupos"][ssss]["Trainer"]
                                cam1=d["Grupos"][ssss]["Campers"][""]

                                print("Grupo: ",ssss," Horario: ",idd1," Aula: ",con1," Ruta: ",nom1," Trainer: ",apl1," Campers: ",cam1)
                            au=int(input("Cual grupo quieres modificar"))
                            print
                            horario1=input("Cual es el horario nuevo: 1: (6 A.M.-10 A.M.) 2: (10 A.M.-12 M.) 3: (2 P.M.-6 P.M.) 4. (6 P.M.-10 P.M.)")
                            aula1=


                            ## nombrediccionario["Campers"][id]["ruta"]=nombrediccionario["rutas"]["nombre de la ruta"]

                            ## asginar
                            ## nombredccionairo["Grupos"]["numero grupo"]["Aula"]=nombrediccionario["Aulas]["Nombre aula"]
                            ## nombrediccionario["Grupos"]["Numero grupo"]["Horario"]=nombrediccionario["Aulas]["Nombre aula"]["Horarios"][Numero de horario]
                       if opc==9:
                           z3=False
                           






             if m==False:
                     print("Contraseña o usuario icorrectos")