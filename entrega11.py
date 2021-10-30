import random
import seaborn as sns
import matplotlib.pyplot as plt

# Variables
iterations=15500
variables=['horario','salario','teletrabajo','nivel empleo','categoría',\
'ubicación','duracion contrato','trabajo en equipo','viajes','ambiente']

# El peso que tiene respecto a cada variable que yo antes he definido
def Monte_Carlo(grade):
    final_results=[] 
    weight=[0.10,0.15,0.05,0.15,0.12,0.13,0.1,0.05,0.08,0.07] 
    for n in range(iterations):
        results=[]
        for i in range(len(variables)):
            value = weight[i] * (random.uniform(grade[i][0], grade[i][1])) 
            results.append(value)

        final_results.append(sum(results)) 
    return final_results

# Lo que ofrecen las tres ofertas de trabajos
a= Monte_Carlo([[3,10],[2,6],[3,6.5],[6,9],[9,10],[1,9],[2,4],[8,8],[7,9],[1,8]])
 
b= Monte_Carlo([[8,8],[8,9],[7,9],[0,4.5],[2,9.5],[5,8],[7,9],[5,6],[6,8],[2,10]])

c= Monte_Carlo([[5,6],[8,8],[1,8],[9,10],[10,10],[2,3.5],[5,6],[0,9],[2,4],[10,10]])

# Gráfica datos
fig = plt.figure(figsize=(10,6)) 
sns.distplot(a)
sns.distplot(b)
sns.distplot(c)
fig.legend(labels=['Job A','Job B','Job C']) 
plt.title('Monte-Carlo Distributions') 
plt.show()

# La mejor opción es la C en comparación con los otros dos trabajos.