# Punto medio de x puntos (cuyas coordenadas se encuentran en un archivo), dibujar gráfica y sacar en otro archivo el punto medio

# Imports
import matplotlib.pyplot as plt
import sys

# Listas coordenadas 'x' e 'y'
coord_x = []
coord_y = []

def createLists():
    for i in data:
        list = i.replace("\n", "").replace("(", "").replace(")", "").replace(" ", "").split(";")

        for word in list:
            c = word.split(",")
            for i, elem in enumerate(c):
                if i % 2 == 0:
                    coord_x.append(int(elem))
                else:
                    coord_y.append(int(elem))

# Dibujamos la gráfica con los puntos de la lista (azules) y calculamos su punto medio (rojo)
def drawGraphic():
    listX = 0
    listY = 0

    for x, y in zip(coord_x, coord_y):
        plt.scatter(x, y, c='blue')
        listX += x
        listY += y

    num = len(coord_x)
    midpointX = listX / num
    midpointY = listY / num

    plt.scatter(midpointX, midpointY, c='red')
    plt.show()

    writeOutput(midpointX, midpointY)


# Escribimos las coordenadas del punto medio en un archivo output.txt
def writeOutput(midpointX, midpointY):
    outputFile = open("output.txt", "w")
    outputFile.write("Las coordenadas del punto medio son: ("+str(midpointX)+", "+str(midpointY)+")")
    outputFile.close()





# Comprobación de argumentos
if len(sys.argv) == 2:
    inputFile = open(sys.argv[1], "r")
    data = inputFile.readlines()
    inputFile.close()
    createLists()
    drawGraphic()
else:
    print("Error - Introduce los argumentos correctamente")
    print("Debe escribir el nombre del archivo que tiene las coordenadas de los puntos")
    print("Ejemplo: Punto_Medio.py input.txt")
