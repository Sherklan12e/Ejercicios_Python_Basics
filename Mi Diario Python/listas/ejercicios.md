Ejercicio 1
Escriba una función que tome una lista de números y devuelva la suma acumulada, es decir, una nueva lista donde el primer elemento es el mismo, el segundo elemento es la suma del primero con el segundo, el tercer elemento es la suma del resultado anterior con el siguiente elemento y así sucesivamente. Por ejemplo, la suma acumulada de [1,2,3] es [1, 3, 6].

Ejercicio 2
Escribe una función llamada "elimina" que tome una lista y elimine el primer y último elemento de la lista y cree una nueva lista con los elementos que no fueron eliminados.
Luego escribe una función que se llame "media" que tome una lista y devuelva una nueva lista que contenga todos los elementos de la lista anterior menos el primero y el último.

Ejercicio 3
Escribe una función "ordenada" que tome una lista como parámetro y devuelva True si la lista está ordenada en orden ascendente y devuelva False en caso contrario.
Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada([b, a]) retorna False.

Ejercicio 4
A - Escribe una función llamada "duplicado" que tome una lista y devuelva True si tiene algún elemento duplicado. La función no debe modificar la lista.
B - Crear una función que genere una lista de 23 números aleatorios del 1 al 100 y comprobar con la función anterior si existen elementos duplicados. (Puedes ver el módulo random como guía)


Ejercicio 5
Escribe una función llamada "elimina_duplicados" que tome una lista y devuelva una nueva lista con los elementos únicos de la lista original. No tienen porque estar en el mismo orden.

Ejercicio 6
Escribe una función que lea las palabras de un archivo de texto (texto.txt) y construya una lista donde cada palabra es un elemento de la lista.

Ejercicio 7
Escribe una función llamada "inversa" que busque todas las palabras inversas de una lista.
Ejemplo de palabras inversas: radar, oro, rajar, rallar, salas, somos, etc...


Ejercicio 8 
Para comprobar si una palabra está en una lista se puede utilizar el operador "in", pero sería una búsqueda lenta, ya que busca a través de las palabras en orden.
Debido a que las palabras están en orden alfabético, podemos acelerar las cosas con una búsqueda de bisección (también conocida como búsqueda binaria), que es similar a lo que haces cuando buscas una palabra en el diccionario. Comenzamos por el centro y comprobamos si la palabra que buscamos está antes o después del centro. Si está antes, se busca solo en la primera mitad, si está después se busca en la otra mitad de la lista. Con esto reduciremos el tiempo de búsqueda