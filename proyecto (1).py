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
             "apellidos": apl,
             "Direccion": direc,
             "acudiente": acu,
             "Telefonos": num, 
             "Estado": "Inscrito",
             "Jornada": "",
             "Ruta":{}
             }
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
                                id1=d["Campers"][a]["#NumeroDeIdentificacion"]
                                co1=d["Campers"][a]["Contraseña"]
                                nom1=d["Campers"][a]["Nombres"]
                                apl1=d["Campers"][a]["apellidos"]
                                dir1=d["Campers"][a]["Direccion"]
                                acu1=d["Campers"][a]["acudiente"]
                                tel1=d["Campers"][a]["Telefonos"]
                                est1=d["Campers"][a]["Estado"]
                                jor1=d["Campers"][a]["Jornada"]
                                print("ID: ",id1," contraseña: ",co1," Nombres: ",nom1," Apellidos: ",apl1," Direccion: ",dir1," Acudiente: ",acu1," Telefono de contacto: ",tel1," Estado: ",est1," Jornada: ",jor1)
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
                        print("3. Ver tus estudiantes")   
                        print("4. Cerrar sesion")
                        opc=int(input(": "))
                        if opc==1:
                             for i in range (1):
                                f=str(a)

                                idd1=d["Trainers"][f]["NumeroDeIdentificacion"]
                                con1=d["Trainers"][f]["Contraseña"]
                                nom1=d["Trainers"][f]["Nombres"]
                                apl1=d["Trainers"][f]["apellidos"]
                                hor1=d["Trainers"][f]["Horarios"]
                                est1=d["Trainers"][f]["Estado"]
                                print("ID: ",idd1," contraseña: ",con1," Nombres: ",nom1," Apellidos: ",apl1," Horario: ",hor1," Estado: ",est1)
                        if opc==4:
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
                       print("5. Cambiar estado de los estudiantes a retirado")
                       print("6. modificar los grupos")
                       print("7. Añadir y ver aulas")
                       print("8. Asignar campers a su grupo")
                       print("9. Quienes pasaron el examen de admision")
                       print("10. Asignar notas")
                       print("11. Crear grupos")
                       print("12. Cerrar sesion")
                       opc=int(input(": "))
                       if opc==1:
                           print("A quien deseas verle la informacion")
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
                                jor1=d["Campers"][ssss]["Jornada"]
                                not1=d["Campers"][ssss]["Ruta"]
                                print("ID: ",id1," contraseña: ",co1," Nombres: ",nom1," Apellidos: ",apl1," Direccion: ",dir1," Acudiente: ",acu1," Telefono de contacto: ",tel1," Estado: ",est1," Jornada: ",jor1," Ruta",not1)
                           if opcc==2:
                               for i in range (len(d["Trainers"])):
                                ssss=str(i)
                                id1=d["Trainers"][ssss]["NumeroDeIdentificacion"]
                                co1=d["Trainers"][ssss]["Contraseña"]
                                nom1=d["Trainers"][ssss]["Nombres"]
                                apl1=d["Trainers"][ssss]["apellidos"]
                                hor1=d["Trainers"][ssss]["Horarios"]
                                est1=d["Trainers"][ssss]["Estado"]
                                print("ID: ",id1," contraseña: ",co1," Nombres: ",nom1," Apellidos: ",apl1," Horario: ",hor1," Estado: ",est1)
                           if opcc==3:
                              for i in range (len(d["Coordinadores"])):
                               ssss=str(i)
                               idd1=d["Coordinadores"][ssss]["NumeroDeIdentificacion"]
                               con1=d["Coordinadores"][ssss]["Contraseña"]
                               nom1=d["Coordinadores"][ssss]["Nombres"]
                               apl1=d["Coordinadores"][ssss]["apellidos"]
                               est1=d["Coordinadores"][ssss]["Estado"]
                               print("ID: ",idd1," Contraseña: ",con1," Nombres: ",nom1," Apellidos: ",apl1," Estado: ",est1)
                       if opc==2:
                          for i in range (len(d["Trainers"])):
                                ssss=str(i+1)
                                idd1=d["Grupos"][ssss]["Horario"]
                                con1=d["Grupos"][ssss]["Aula"]
                                nom1=d["Grupos"][ssss]["Ruta"]
                                apl1=d["Grupos"][ssss]["Trainer"]
                                cam1=d["Grupos"][ssss]["Campers"]
                                print("Grupo: ",ssss," Horario: ",idd1," Aula: ",con1," Ruta: ",nom1," Trainer: ",apl1," Campers: ",cam1)
                       if opc==3:
                          mo=int(input("A quien quieres modificar: 1. Campers 2. Trainers 3. Coordinadores"))
                          if mo==1:
                              for i in range (len(d["Campers"])):
                                 ssss=str(i)
                                 idd1=d["Campers"][ssss]["#NumeroDeIdentificacion"]
                                 con1=d["Campers"][ssss]["Contraseña"]
                                 nom1=d["Campers"][ssss]["Nombres"]
                                 apl1=d["Campers"][ssss]["apellidos"]
                                 dir1=d["Campers"][ssss]["Direccion"]
                                 acu1=d["Campers"][ssss]["acudiente"]
                                 tel1=d["Campers"][ssss]["Telefonos"]
                                 print("ID: ",idd1," contraseña: ",con1," Nombres: ",nom1," Apellidos: ",apl1," Direccion: ",dir1," Acudiente: ",acu1," Telefono de contacto: ",tel1)
                              mocam=(input("A quien quieres modificar (ingresar ID)")) 
                              d["Campers"][mocam]["Contraseña"]=int(input("Dame la contaseña mofificada: "))
                              d["Campers"][mocam]["Nombres"]=input("Dame el nombre modificado: ")
                              d["Campers"][mocam]["apellidos"]=input("Dame el apellido modificado: ")
                              d["Campers"][mocam]["Direccion"]=input("Dame la direccion modificada: ")
                              d["Campers"][mocam]["acudiente"]=input("Dame el nombre del acudiente modificado: ")
                              d["Campers"][mocam]["Telefonos"]=input("Dame el numero de telefono modificado: ")
                              guardarJSON(d)
                          if mo==2:
                              for i in range (len(d["Trainers"])):
                                 ssss=str(i)
                                 idd1=d["Trainers"][ssss]["NumeroDeIdentificacion"]
                                 con1=d["Trainers"][ssss]["Contraseña"]
                                 nom1=d["Trainers"][ssss]["Nombres"]
                                 apl1=d["Trainers"][ssss]["apellidos"]
                                 print("ID: ",idd1," contraseña: ",con1," Nombres: ",nom1," Apellidos: ",apl1)
                              motra=(input("A quien quieres modificar (ingresar ID)"))
                              d["Trainers"][motra]["Contraseña"]=int(input("Dame la contaseña mofificada: "))
                              d["Trainers"][motra]["Nombres"]=input("Dame el nombre modificado: ")
                              d["Trainers"][motra]["apellidos"]=input("Dame el apellido modificado: ")
                              d["Trainers"][motra]["Direccion"]=input("Dame la direccion modificada: ")
                              guardarJSON(d)
                          if mo==3:
                              for i in range (len(d["Coordinadores"])):
                                 ssss=str(i)
                                 idd1=d["Coordinadores"][ssss]["NumeroDeIdentificacion"]
                                 con1=d["Coordinadores"][ssss]["Contraseña"]
                                 nom1=d["Coordinadores"][ssss]["Nombres"]
                                 apl1=d["Coordinadores"][ssss]["apellidos"]
                                 print("ID: ",idd1," Contraseña: ",con1," Nombres: ",nom1," Apellidos: ",apl1," Estado: ",est1)
                              mocor=(input("A quien quieres modificar: "))
                              d["Coordinadores"][mocor]["Contraseña"]=input("Dame la contaseña modificada: ")
                              d["Coordinadores"][mocor]["Nombres"]=input("Dame el nombre modificado: ")
                              d["Coordinadores"][mocor]["apellidos"]=input("Dame el apellido modificado: ")
                              guardarJSON(d)
                       if opc==4:
                          for i in range (len(d["Coordinadores"])):
                              ssss=str(i)
                              idd1=d["Trainers"][ssss]["NumeroDeIdentificacion"]
                              con1=d["Trainers"][ssss]["Contraseña"]
                              nom1=d["Trainers"][ssss]["Nombres"]
                              apl1=d["Trainers"][ssss]["apellidos"]
                              print("ID: ",idd1," Contraseña: ",con1," Nombres: ",nom1," Apellidos: ",apl1," Estado: ",est1)
                          mohor=(input("A quien quieres modificar (ingresar ID): "))
                          horar=(input("Que horario desea asignarle: "))
                          d["Trainers"][mohor]["Horarios"]=d
                       if opc==5:
                               for i in range (len(d["Campers"])):
                                 ssss=str(i)
                                 idd1=d["Campers"][ssss]["#NumeroDeIdentificacion"]
                                 con1=d["Campers"][ssss]["Contraseña"]
                                 nom1=d["Campers"][ssss]["Nombres"]
                                 apl1=d["Campers"][ssss]["apellidos"]
                                 tel1=d["Campers"][ssss]["Estado"]
                                 print("ID: ",idd1," contraseña: ",con1," Nombres: ",nom1," Apellidos: ",apl1," Estado: ",tel1)
                               esta=(input("Cual es el estudiantes que quieres pasar a inactivo (ingrese ID)"))
                               d["Campers"][esta]["Estado"]="Retirado"
                       if opc==6:
                            for i in range (len(d["Grupos"])):
                                ssss=str(i+1)
                                idd1=d["Grupos"][ssss]["Horario"]
                                con1=d["Grupos"][ssss]["Aula"]
                                nom1=d["Grupos"][ssss]["Ruta"]
                                apl1=d["Grupos"][ssss]["Trainer"]
                                print("Grupo: ",ssss," Horario: ",idd1," Aula: ",con1," Ruta: ",nom1," Trainer: ",apl1)
                            au=(input("Cual grupo quieres modificar"))
                            for i in range(len(d["aulas"])):
                               v=str(i)
                               s=d["aulas"][v]["Nombre"]
                               print(v,". ",s)
                            aula9=str(input("Cual es la aula que quieres asignar: "))
                            d["Grupos"][au]["Aula"]=d["aulas"][aula9]["Nombre"]
                            horario9=str(input("Cual es el horario a asignar: 1: (6 A.M.-10 A.M.) 2: (10 A.M.-12 M.) 3: (2 P.M.-6 P.M.) 4. (6 P.M.-10 P.M.): "))
                            d["Grupos"][au]["Horario"]=d["aulas"][aula9]["HorariosDisponibles"][horario9]
                            rut9=str(input("Cual ruta deseas asignarle: 0. Java, 1. NodeJS, 2. NetCore"))
                            d["Grupos"][au]["Ruta"]=d["Rutas"][rut9]
                            
                            for i in range (len(d["Trainers"])):
                              ssss=str(i)
                              idd1=d["Trainers"][ssss]["NumeroDeIdentificacion"]
                              con1=d["Trainers"][ssss]["Contraseña"]
                              nom1=d["Trainers"][ssss]["Nombres"]
                              apl1=d["Trainers"][ssss]["apellidos"]
                              print("ID: ",idd1," Contraseña: ",con1," Nombres: ",nom1," Apellidos: ",apl1)
                            tra9=str(input("Que trainer quieres asignarle (ingresa ID): "))
                            d["Grupos"][au]["Trainer"]=d["Trainers"][tra9]["Nombres"]


                            guardarJSON(d)
                       if opc==7:
                           for i in range(len(d["aulas"])):
                             ñ=str(i)
                             nom5=d["aulas"][ñ]["Nombre"]
                             hor5=d["aulas"][ñ]["HoraDeInicio"]
                             horf5=d["aulas"][ñ]["HoraDeFin"]
                             horarios5=d["aulas"][ñ]["Horarios"]
                             horariosd5=d["aulas"][ñ]["HorariosDisponibles"]


                             print( ñ,". Salon: ",nom5," Hora de inicio: ",hor5," Hora de fin: ",horf5," Horarios: ",horarios5," Horarios disponibles",horariosd5)#," Nombre: ",nom9,"")
                           noma=input("Cual es el nombre del nuevo salon: ")
                           r=len(d["aulas"])
                           d["aulas"][r]={"Nombre":noma,
                           "HoraDeInicio": "6 A.M.",
                           "HoraDeFin": "10 P.M.",
                           "Horarios": {"1": "6 A.M.-10 A.M.","2": "10 A.M.-12 M.","3": "2 P.M.-6 P.M.","4": "6 P.M.-10 P.M."}}
                           guardarJSON(d)
                       if opc==8:
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
                             jor1=d["Campers"][ssss]["Jornada"]
                             not1=d["Campers"][ssss]["Ruta"]
                             if est1=="Aprobado":
                                 print("ID: ",id1," contraseña: ",co1," Nombres: ",nom1," Apellidos: ",apl1," Direccion: ",dir1," Acudiente: ",acu1," Telefono de contacto: ",tel1," Estado: ",est1," Jornada: ",jor1," Ruta",not1)
                         est2=int(input("A quien quieres añadir (ingresar ID): "))
                         est1=str(est2)
                         for i in range (len(d["Grupos"])):
                          ssss=str(i+1)
                          idd1=d["Grupos"][ssss]["Horario"]
                          con1=d["Grupos"][ssss]["Aula"]
                          nom1=d["Grupos"][ssss]["Ruta"]
                          apl1=d["Grupos"][ssss]["Trainer"]
                          print("Grupo: ",ssss," Horario: ",idd1," Aula: ",con1," Ruta: ",nom1," Trainer: ",apl1)
                         gru1=str(input("A cual grupo lo quieres añadir (ingrese numero de grupo):"))
                         s=str(len(d["Grupos"][gru1]["Campers"]))
                         
                         horario11=str(d["Grupos"][gru1]["Horario"])
                         if d["Grupos"][gru1]["Ruta"]["Ruta"]=="Java":
                            a=0
                         if d["Grupos"][gru1]["Ruta"]["Ruta"]=="NodeJS":
                            a=1
                         if d["Grupos"][gru1]["Ruta"]["Ruta"]=="NetCore":
                            a=2
                         Ruta11=str(d["Rutas"][a])

                         d["Grupos"][gru1]["Campers"][s]={"#NumeroDeIdentificacion": d["Campers"][est1]["#NumeroDeIdentificacion"],
                         "Contraseña":  d["Campers"][est1]["Contraseña"],
                         "Nombres":  d["Campers"][est1]["Nombres"],
                         "apellidos":  d["Campers"][est1]["apellidos"],
                         "Direccion":  d["Campers"][est1]["Direccion"],
                         "acudiente":  d["Campers"][est1]["acudiente"],
                         "Telefonos":  d["Campers"][est1]["Telefonos"], 
                         "Estado":  "Cursando",
                         "Jornada":  d["Campers"][est1]["Jornada"],
                         "Ruta": Ruta11
                         }
                         

                         d["Campers"][est1]["Estado"]="Cursando"
                         d["Campers"][est1]["Jornada"]=horario11
                         d["Campers"][est1]["Ruta"]=Ruta11
                         
                         guardarJSON(d)
                       if opc==9: 
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
                             jor1=d["Campers"][ssss]["Jornada"]
                             not1=d["Campers"][ssss]["Ruta"]
                             
                             if est1=="Inscrito":
                                 print("ID: ",id1," contraseña: ",co1," Nombres: ",nom1," Apellidos: ",apl1," Direccion: ",dir1," Acudiente: ",acu1," Telefono de contacto: ",tel1," Estado: ",est1," Jornada: ",jor1," Ruta",not1)
                          apro1=str(input("Quien aprobo (ingrese ID): "))
                          d["Campers"][apro1]["Estado"]="Aprobado"
                          guardarJSON(d)      
                       if opc==11:
                         for i in range(1):
                             f=str(len(d["Grupos"])+1)
                             d["Grupos"][f]={"Horario": "",
                             "Aula": "",
                             "Ruta": "",
                             "Trainer": "",
                             "Campers": {}
                             }
                             guardarJSON(d)
                       if opc==12:
                           z3=False
             if m==False:
                 print("Contraseña o usuario icorrectos")