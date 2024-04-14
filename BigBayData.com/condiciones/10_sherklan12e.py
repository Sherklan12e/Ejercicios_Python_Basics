# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu. Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.

# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.

# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.


print("""
        Bienvenido ala pizzeria
        1) si
        2) no
        """)
eleccion = int(input("Que pizza desea la vegetariana o no ?: "))
if eleccion == 1 or eleccion == 2:
    print("""
          igredientees diponibles:
          1)pimiento
          2)tofu
          3)peperoni
          4)jamon
          5)salmon
          elija 1 opcion
          """)
opcion = int(input("opcion: "))
if opcion == 1 or opcion ==2:
    print("pizza vegetariana!")
    print("Ingredientes: Pimiento y tofu")
elif opcion == 3 or opcion == 4 or opcion == 5:
    print("pizza no vegetariana!")
    print("Ingredientes: Peperoni, Jamón y Salmón")