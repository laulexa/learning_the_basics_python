name = 'Laura'
last_name = 'Roa'
major = '  Industrial Engineering  '
print(name + ' ' + last_name)
print(name * 5)
print(len(name), len(last_name))
print(major.lower())
print(major.upper())
print(major.strip())

'''
Uso de sep
El parámetro sep permite especificar cómo separar los elementos al imprimir. En este ejemplo, los elementos “Nunca”, “pares”, “de” y “aprender” 
se imprimirán con una coma y un espacio entre ellos, resultando en “Nunca, pares, de, aprender”. Puedes cambiar sep por cualquier cadena de caracteres 
que desees usar como separador.
'''
print("Nunca", "pares", "de", "aprender", sep=", ")
# Nunca, pares, de, aprender

'''
Uso de end
El parámetro end cambia lo que se imprime al final de la llamada a print. En lugar de imprimir cada mensaje en una nueva línea, 
end="" asegura que “Nunca” y “pares” se impriman en la misma línea, resultando en “Nunca pares”. Por defecto, end es un salto de 
línea ("\n"), lo que hace que cada llamada a print comience en una nueva línea.
'''
print("Nunca", end=" ")
print("pares de aprender")
#Nunca pares de aprender

'''
Impresión de variables
Puedes usar print para mostrar el valor de las variables. 
'''
print("name:", name)
print("Last name:", last_name)

'''
Uso de formato con f-strings
Las f-strings permiten insertar expresiones dentro de cadenas de texto. Al anteponer una f a la cadena de texto, 
puedes incluir variables directamente dentro de las llaves {}.
'''
print(f"Name: {name}, Last Name: {last_name}")
'''
Uso de formato con format
El método format es otra forma de insertar valores en cadenas de texto. Usando {} como marcadores de posición, 
puedes pasar los valores que quieres insertar como argumentos de format. 
'''
print("Name {}, Last Name: {}".format(name, last_name))
'''
Impresión con formato específico
Puedes controlar el formato de los números al imprimir. En este ejemplo, :.2f indica que el número debe mostrarse con dos decimales.
 Así, imprimirá “Valor: 3.14”, redondeando el número a dos decimales. Esto es especialmente útil cuando trabajas con datos numéricos 
 y necesitas un formato específico.
'''
valor = 3.1416
print("Valor: {:.2f}".format(valor))
'''
Saltos de línea y caracteres especiales
Los saltos de línea en Python se indican con la secuencia de escape \n. Por ejemplo, para imprimir “Hola\nmundo”, que aparecerá en dos líneas:
'''
print("Hola\nMundo")

'''
Si necesitas imprimir una ruta de archivo en Windows, que incluya barras invertidas, también necesitarás usar secuencias de escape para evitar que
Python interprete las barras invertidas como parte de secuencias de escape. Por ejemplo:
'''
print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt")