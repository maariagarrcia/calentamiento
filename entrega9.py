#Crear un archivo
f = open("flag.txt", "w") 
f.write("Voy a intentar sacar un 10 :) ") 
f.close

f = open("flag.txt", "r") 
print(f.read())

 