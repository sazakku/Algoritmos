def add():
    try:
        a = int(input("Ingrese el primer valor: \n"))
        b = int(input("Ingrese el segundo número: \n"))
        
        if a and b:
            c = a + b
            print(f"El valor de la suma es: {c}")
        else:
            print("Error :C")
    except ValueError:
        print("No se aceptan valores diferentes a numeros")
        add()

if __name__ == "__main__":
    add()