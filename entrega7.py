#Número aleatorio
import random

#Bucle del 0 al 50
for x in range (51):
  print(x)


#Cálculo de hambre
edad = random.randint(1,100)
inc_satisfaccion_por_helado = (edad/100)
satisfaccion_inicial = edad/100
dinero_inicial = 2000
precio_helado_inicial = 100
inc_precio_helado = 20/100
satisfaccion_minima = 85/100
satisfaccion_maxima = 100/100

# Comer helados hasta llegar a la satisfacción mínima
# o hasta quedarnos sin dinero
satisfaccion_actual = satisfaccion_inicial
dinero_actual = dinero_inicial
precio_helado_actual = precio_helado_inicial
helados_consumidos = 0

print("Satisfacción inicial ", satisfaccion_inicial*100)
print()
while ((satisfaccion_actual<satisfaccion_minima) and 
		((satisfaccion_actual+inc_satisfaccion_por_helado) <=
           satisfaccion_maxima) and
		((dinero_actual-precio_helado_actual)>0)):
	# Comer un helado
    helados_consumidos = helados_consumidos + 1
    
	# Recalcular satisfacción actual
    satisfaccion_actual = (satisfaccion_actual + 	
						inc_satisfaccion_por_helado)
                            
    # Recalcular el dinero que me queda
    dinero_actual = dinero_actual - precio_helado_actual
    
    # Visualizar datos
    print("ITERACION ACTUAL " , helados_consumidos)
    print("* Helados consumidos ", helados_consumidos)
    print("* Precio helado ", precio_helado_actual)
    print("* Dinero que nos queda ", dinero_actual)
    print("* Satisfacción ", satisfaccion_actual*100)
    print("------")
    print()    
    # Actualizar el precio del helado
    precio_helado_actual = (precio_helado_actual * 
    						(1+inc_precio_helado))
                            
    
if(helados_consumidos<=0):
	print("No me he podido comer ningún helado :-(")

# Visualizar datos
print("* Helados TOTALES consumidos ", helados_consumidos)
print("* Dinero TOTAL que me queda ", dinero_actual)
print("* Satisfacción CONSEGUIDA", satisfaccion_actual*100)

#Diagrama de flujo
import webbrowser
webbrowser.open("https://www.figma.com/file/mah8Zw7X6eIvE5Wl7WZpDy/entrega-7?node-id=0%3A1")