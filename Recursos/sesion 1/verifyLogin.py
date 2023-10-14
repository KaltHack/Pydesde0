# ! VERIFICA SI EL USUARIO ES MAYOR DE 18 Y NACIONALIDAD ARGENTINA
print("BIENVENIDO AL PROGRAMA\n")

def permisos(parametro1, parametro2):

    # Comprueba si eres mayor de edad y si tu nacionalidad es argentina, en ese caso da el acceso
    if parametro1 >= 18 and parametro2 == "Arg":
        print("Puedes pasar")
    # Comprueba si eres menor o si no eres argentino, en ese caso no da el acceso
    elif parametro1 < 18 or parametro2 != "Arg":  
        print("No puedes Pasar")
    else:
        print("ERROR: coloca un dato válido")

    # Nota: Or procede si cualquier condicional se cumple.  And procede solo si todas cumplen

loginEdad = int(input("Coloca tu edad: "))
loginNacionalidad = (input("Coloca tu nacionalidad: "))


# ========================================
# ========================================

permisos(loginEdad, loginNacionalidad)
