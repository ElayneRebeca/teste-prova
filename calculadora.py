# alteração Elayne
# alterando na feature

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Erro: divisão por zero!")
    return a / b

def calculadora():
    print("=== Calculadora ===")
    print("Operações: + | - | * | /")

    while True:
        try:
            a = float(input("\nPrimeiro número: "))
            op = input("Operação (+, -, *, /): ").strip()
            b = float(input("Segundo número: "))

            if op == "+":
                resultado = somar(a, b)
            elif op == "-":
                resultado = subtrair(a, b)
            elif op == "*":
                resultado = multiplicar(a, b)
            elif op == "/":
                resultado = dividir(a, b)
            else:
                print("Operação inválida!")
                continue

            print(f"Resultado: {resultado}")

        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            print("\nEncerrando calculadora.")
            break

if __name__ == "__main__":
    calculadora()