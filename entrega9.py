# Crear un archivo
f = open("flag.txt", "w") 
f.write("quiero salir de fiesta pero estoy haciendo programación :) ") 
f.close

f = open("flag.txt", "r") 
print(f.read())

 