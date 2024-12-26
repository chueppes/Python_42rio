import sys

try:
    if len(sys.argv) == 1:
        exit()
    # Verifica se há mais de um argumento e se há apenas um valor esperado
    assert len(sys.argv) == 2, "AssertionError: more than one argument is provided"

    # Verifica se o argumento passado é um número
    assert sys.argv[1].isdigit(), "AssertionError: argument is not an integer"

    # Converte o argumento para inteiro
    numero = int(sys.argv[1])

    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except AssertionError as e:
    print(e)
