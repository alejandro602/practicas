from random import randint


menu=True

stats=[10,10,10]
objetos=["pocion","armadura"]
cantidad_objetos=[3,1]
puntos_stats=2
stats_enemigo=[0,0,0]#fuerza,destreza,constitucion
nivel=1
nivel_plus=2
exp=1
while menu==True:
    if nivel==nivel_plus:
        puntos_stats+=1
        nivel_plus*=1
    print("")
    print("")
    print("")
    print("")
    print("")
    print("==menu==")
    print("=========")
    print("1:mochila")
    print("2:stats")
    print("3:luchar")
    print("4:salir")
    print("=========")
    decision=int(input("a que quieres acceder: "))
    if decision==1:
        while menu==True:
           print("")
           print("")
           print("")
           print("")
           print("")
           print("==mochila==")
           print("===========")
           print(f"1:{objetos[0]}: {cantidad_objetos[0]}x")
           print(f"2:{objetos[1]}: {cantidad_objetos[1]}x")
           print(f"2:{objetos[2]}: {cantidad_objetos[2]}x")
           print(f"{len(objetos)+1}:salir")
           print("=========") 
           mochila_decision=int(input("que quieres hacer:  "))
           if mochila_decision==len(objetos)+1:
               break
    elif decision==2:
        while menu==True:
            print("")
            print("")
            print("")
            print("")
            print("")
            print("==stats==")
            print("=========")
            print(f"fuerza: {stats[0]}")
            print(f"destreza: {stats[1]}")
            print(f"constitucion: {stats[2]}")
            print("1:volver")
            print("2:mejora de stats")
            print("=========")
            stats_decision=int(input("que quieres hacer:  "))
            if stats_decision==1:
                break
            elif stats_decision==2:
                while menu==True:
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("==mejoras==")
                    print(f"eres nivel {nivel}")
                    print("=========")
                    print("1:fuerza++")
                    print("2:destreza++")
                    print("3:constitucion++")
                    print("4:volver")
                    print("=========")
                    print(f"Tienes {puntos_stats} puntos de stats")
                    stats_mejoras=int(input("que stat quieres mejorar: "))
                    while menu==True:
                        if puntos_stats==0:
                            print("no tienes puntos")
                            break
                        else:
                            if stats_mejoras==1:
                                stats[0]+=1
                                puntos_stats-=1
                                print("fuerza++")
                                break
                            elif stats_mejoras==2:
                                stats[1]+=1
                                puntos_stats-=1
                                print("destreza++")
                                break
                            elif stats_mejoras==3:
                                stats[2]+=1
                                puntos_stats-=1
                                print("constitucion++")
                                break
                            elif stats_mejoras==4:
                                break
                            elif stats_mejoras>4:
                                break
                    break
    elif decision==3:
        while menu==True:
            enemigo = randint(0,7)
            if enemigo==1:
               print("limo")
               #fuerza
               stats_enemigo[0]=randint(2,4)
               #destreza
               stats_enemigo[1]=randint(2,4)
               #constitucion
               stats_enemigo[2]=randint(6,8)
               break
            elif enemigo==2:
                print("esqueleto")
                #fuerza
                stats_enemigo[0]=randint(3,5)
                #destreza
                stats_enemigo[1]=randint(3,5)
                #constitucion
                stats_enemigo[2]=randint(10,12)
                break
            elif enemigo==3:
                print("jesus alcocer") 
                #fuerza
                stats_enemigo[0]=666
                #destreza
                stats_enemigo[1]=666
                #constitucion
                stats_enemigo[2]=666
                break
            elif enemigo==4:
                print("Gallina demoniaca")
                #fuerza
                stats_enemigo[0]=randint(10,14)
                #destreza
                stats_enemigo[1]=randint(8,12)
                #constitucion
                stats_enemigo[2]=randint(8,10)
                break
            elif enemigo==5:
                print("Gallina demoniaca")
                #fuerza
                stats_enemigo[0]=randint(10,14)
                #destreza
                stats_enemigo[1]=randint(8,12)
                #constitucion
                stats_enemigo[2]=randint(8,10)
                break
            elif enemigo==6:
                print("Gobling chemil")
                #fuerza
                stats_enemigo[0]=randint(8,10)
                #destreza
                stats_enemigo[1]=randint(6,9)
                #constitucion
                stats_enemigo[2]=randint(12,14)
                break
            elif enemigo==7:
                print("nacho")
                #fuerza
                stats_enemigo[0]=randint(14,17)
                #destreza
                stats_enemigo[1]=randint(6,10)
                #constitucion
                stats_enemigo[2]=randint(12,16)
                break
            elif enemigo==0:
                print("puerta")
                #fuerza
                stats_enemigo[0]=0
                #destreza
                stats_enemigo[1]=0
                #constitucion
                stats_enemigo[2]=randint(8,10)
                break
    elif decision==4:
       nivel+=1
    elif decision>4:
        print("numero no valido")
        break
        
        


