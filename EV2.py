
i=0
responde=[] #responde es lugar cualquiere pais 
print("****"*20)
print("bienviendos es falabella")
print("****"*20)

lugar=int(input("lugar pais viajar cuanto: "))# numero responde para pais quiere cualquiere elige ejemplo yo qiere 4 pais
cuanto=int(input("personas cuanto: "))#solo personas cuanto despues total USD
while i<lugar:
    responde.append(input(f"que quiere lugar es pais  {i+1}: "))
    personas=int(input(f"su junto familia (personas es USD):"))#cuanto personas para vas viajar pais
    if personas !=cuanto :
        print()
    else:
        personas * cuanto
        totalP*=cuanto
    while True:
        try:
            hotel=int(input("cuanto hotel es  dia/noches : "))
            hotelpagar=int(input("hotel noche dormir (USD): "))
            tour=int(input("quiere visita lugar conocer real cuanto : "))
            if tour == 0:
                print()
            else:
                tour == 1
                tourpagar=int(input(f"lugar visita {i+1} real conocer: "))
                print("***"*20)
            break
        except:  
        
            print("por favor solo numero responde!!!!")
    
    totalP = personas * cuanto 
    totalHotel = hotel * hotelpagar
    totalT = tourpagar * cuanto 
    i+=1
print("tipo total")
print(f"lugar pais:{responde}")
print(f"hotel es (USD total):{totalHotel} USD")
print(f"personas USD {totalP}")
print(f"tour es total {totalT}")

