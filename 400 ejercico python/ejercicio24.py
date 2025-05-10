# 24)El día juliano correspondiente a una fecha es un número entero que indica los días que han 
# transcurrido desde el 1 de enero del año indicado.        Queremos crear un programa principal que al introducir una fecha nos diga el día juliano 
# que corresponde. Para ello podemos hacer las siguientes subrutinas:              LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).              DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.              EsBisiesto: Recibe un año y nos dice si es bisiesto.               Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano.

def leer_fecha():
    dia = int(input("Introduce el dia: "))
    mes = int(input("Introduce el mes: "))
    año = int(input("Introduce el año: "))
    return dia, mes, año

def es_bisiesto(año):
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

def dias_del_mes(mes, año):
    if mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        return 29 if es_bisiesto(año) else 28
    else:
        return 31

def calcular_dia_juliano(dia, mes, año):
    dia_juliano = dia
    for i in range(1, mes):
        dia_juliano += dias_del_mes(i, año)
    return dia_juliano


def main():
    dia, mes, año = leer_fecha()
    dia_juliano = calcular_dia_juliano(dia, mes, año)
    print(f"El dia juliano correspondiente es: {dia_juliano}")

if __name__ == "__main__":
    main()
