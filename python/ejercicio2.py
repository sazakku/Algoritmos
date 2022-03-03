def numbers():
    
    try:
        a = int(input("Ingrese el primer valor: \n"))
        b = int(input("Ingrese el segundo número: \n"))
        
        if a < b:
            print("El valor menor es: " + str(a))
        elif a > b:
            print("El valor menor es: " + str(b))
        elif a == b:
            print("son iguales")
            numbers()
        else:
            print("Error :C")
    except ValueError:
        print("No se aceptan valores diferentes a numeros")
        numbers()

if __name__ == "__main__":
    numbers()
    