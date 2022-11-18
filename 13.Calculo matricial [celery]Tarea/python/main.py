from celery import Celery
import time
import numpy as np
from rich.console import Console
from rich.table import Table


app = Celery('tasks', broker= 'redis://localhost', backend='redis://localhost:6379')

@app.task                
def saludo():
    print("hoal")
    return "saludo"

@app.task 
def funcion_calculo(file , command):

    m = open(file, 'r')
    Lines = m.readlines()
    
    count = 0
    # Strips the newline character
    array = list()
    for line in Lines:
        count += 1
        array.append(list(line.strip()))

    result=None
    if(command == "pot"):
        result = exp_matrix(array, 3)
    if(command == "log"):
        result = log_matrix(np.array(array))
    if(command == "raiz"):
        result = sqrt_matrix(np.array(array))
    

    table = Table(title="Tabla de resultados")

    table.add_column("Comando", justify="right", style="cyan", no_wrap=True)
    table.add_column("Archivo", style="magenta")
    table.add_column("Matriz", style="magenta")
    table.add_column("Resultado", justify="right", style="green")

    table.add_row(command , file, str(array), str(result))

    console = Console()
    console.print(table)

@app.task                
def calcular_matrix_test():


    m=np.ones((2,2))
    print(dibujar_matrix(m))
    print("suma")
    print(dibujar_matrix(suma_matrix(m, m)))
    print("raiz")
    print(dibujar_matrix(sqrt_matrix(m)))
    print("pot")
    print(dibujar_matrix(exp_matrix(m,5)))
    print("log")
    print(dibujar_matrix(log_matrix(suma_matrix(m, m))))

    return "calcular_matrix_test"

             
def dibujar_matrix(m):
    dibujo = ''
    for fila in m:
        dibujo+='['
        for columna in fila:
            dibujo+=str(columna)+','
        dibujo+='],'
    return dibujo


def suma_matrix(A,B):
    return dibujar_matrix(A+B)

def sqrt_matrix(m):
    
    array_2d = np.array(m, dtype=np.float)

    array_2d_sqrt = np.sqrt(array_2d)

    print(array_2d_sqrt)
    return array_2d_sqrt




def exp_matrix(a,n):
    narray = []
    count = 0
    for i in a:
        narray.append([])
        for j in i:
            narray[count].append(int(j)**n)
        count += 1
    return narray

def log_matrix(m):
    narray = []
    count = 0
    for i in m:
        narray.append([])
        for j in i:
            narray[count].append(np.log(int(j)))
        count += 1
    return narray