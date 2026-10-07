from datetime import date

def pedir_fecha():
    while True:  # Repite hasta que el usuario ingrese una fecha válida
        try:
            dia = int(input("Día de nacimiento: ")) # Define la variable "dia" como entero y lo ingresado en dia de nacimiento se va a guardar en dia.
            mes = int(input("Mes de nacimiento: ")) # Define la variable "mes" como entero y lo ingresado en esa variable va a ser el dato extraido de Mes de Nacimiento
            anio = int(input("Año de nacimiento: ")) 

            nacimiento = date(anio, mes, dia) # La variable "nacimiento" extrae los datos de año, mes y dia para organizarlos dentro de "date"
  
            if nacimiento > date.today():
                print(" La fecha no puede ser en el futuro. Intentá de nuevo.\n") # Si la fecha de nacimiento es mayor a la fecha actual tira error
                continue    

            # Verificar que sea una fecha razonable (no hace 300 años)
            if anio < 1900:
                print(" El año ingresado es demasiado antiguo. Intentá de nuevo.\n") # Si el año ingresado es menor a 1900 tira error
                continue        

            return nacimiento  # Fecha válida, la devolvemos

        except ValueError:
            print(" Fecha inválida (ej: día o mes inexistente). Intentá de nuevo.\n")
        except Exception:
            print(" Ingresá solo números. Intentá de nuevo.\n") # Si se escriben letras tira error (solo acepta numeros)


def calcular_edad(nacimiento):
    hoy = date.today()

    # Diferencia total en días (bisiestos incluidos automáticamente)
    total_dias = (hoy - nacimiento).days

    # Años
    anios = hoy.year - nacimiento.year
    if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
        anios -= 1
 
    # Fecha base después del último cumpleaños
    anio_cumple = hoy.year if (hoy.month, hoy.day) >= (nacimiento.month, nacimiento.day) else hoy.year - 1
    ultimo_cumple = nacimiento.replace(year=anio_cumple)

    # Meses desde el último cumpleaños
    meses = hoy.month - ultimo_cumple.month
    if hoy.day < ultimo_cumple.day:
        meses -= 1
    if meses < 0:
        meses += 12

    # Fecha base después de contar los meses
    mes_base = ultimo_cumple.month + meses
    anio_base = ultimo_cumple.year
    if mes_base > 12:
        mes_base -= 12
        anio_base += 1
    despues_de_meses = ultimo_cumple.replace(year=anio_base, month=mes_base)

    # Semanas y días restantes
    dias_restantes = (hoy - despues_de_meses).days
    semanas = dias_restantes // 7
    dias = dias_restantes % 7

    return anios, meses, semanas, dias, total_dias


# Programa principal (toma todos los datos procesados anteriormente y los muestra) Command Print = Mostrar Variable
print("=== Calculadora de edad exacta ===\n")
nacimiento = pedir_fecha()
anios, meses, semanas, dias, total_dias = calcular_edad(nacimiento)

print(f"\nTu edad exacta es:")
print(f"   {anios} años")
print(f"   {meses} meses")
print(f"   {semanas} semanas")
print(f"   {dias} días")
print(f"\n    Total: {total_dias} días vividos")
