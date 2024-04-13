# Desarrollar un programa en Python que determine si el año introducido es un año bisiesto o no. Sabiendo que…

# Si el año es uniformemente divisible por 4, vaya al paso 2. De lo contrario, vaya al paso 5. Si el año es uniformemente divisible por 100, vaya al paso 3. De lo contrario, vaya al paso 4. Si el año es uniformemente divisible por 400, vaya al paso 4. De lo contrario, vaya al paso 5. El año es un año bisiesto (tiene 366 días). El año no es un año bisiesto (tiene 365 días).


year = int(input("Enter year here: "))

if (year % 4== 0 and year % 100 !=0) or  (year % 400 ==0):
    print("the year is bisiesto")
else:
    print("the year is not bisiesto!")