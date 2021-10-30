#Variables
inversion_bitcoin= 1.2
bitcoin_a_euro= 40000

#Función para el cambio de bitcoin a euro
def bitcoin_euro(inversion_bitcoin, bitcoin_a_euro):
    resultado_euros= inversion_bitcoin * bitcoin_a_euro
    return resultado_euros

#Si el valor está por debajo hay que avisar
if (bitcoin_a_euro<30000):
    print("ha_caido")

#Si no está por debajo
else:
    print("no_ha_caido")

#Cambio de variables y hacer lo mismo
inversion_bitcoin= 1.2
bitcoin_a_euro= 25000

def bitcoin_euro(inversion_bitcoin, bitcoin_a_euro):
    resultado_euros= inversion_bitcoin * bitcoin_a_euro
    return resultado_euros

if (bitcoin_a_euro<30000):
    print("ha_caido")

else:
    print("no_ha_caido")

