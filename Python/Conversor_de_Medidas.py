"""
Esse algoritmo deverá fazer conversão das seguintes medidas:
Distância, Massa, Temperatura, Velocidade e Tempo

Made by Lucas Nogueira
"""
# 1 As medidas que o usuário pode converter
medidas = ["Distância", "Massa", "Temperatura", 'Velocidade', 'Tempo']

# 2 Unidades de Medida

# 2.1 Unidade de Distância
uniDistancia = ["Quilômetro(s)", "Metro(s)", "Milímetro(s)"]

# 2.2 Unidade de Massa
uniMassa = ["Tonelada(s)", "Quilograma(s)", "Grama(s)"]

# 2.3 Unidade de Temperatura
uniTemperatura = ["Celsius", "Fahrenheit", "Kelvin"]

# 2.4 Unidade de Velocidade
uniVelocidade = ["Km/H", "M/s"]

# 2.5 Unidade de Tempo
uniTempo = ["Horas", "Minutos", "Segundos"]


# 2.8 Comprimento


def apresentacao(nome):
    print("*", end="")
    print('-' * 60, end="")
    print("*")
    print("|", end="")
    print(f"{nome}".center(60), end="")
    print("|")
    print("*", end="")
    print('-' * 60, end="")
    print("*")


def apresentaConversao(primeira, segunda):
    print("*", end="")
    print('-' * 60, end="")
    print("*")
    print("|", end="")
    print(f"{primeira: ^26} -----> {segunda: ^26}", end="")
    print("|")
    print("*", end="")
    print('-' * 60, end="")
    print("*")


def start():
    apresentacao("Conversor de Medidas")
    enquadro(medidas)
    op = int(input("Insira a opção de medida que você deseja converter\n-> "))
    check(op)
    avaliacao(op)
    return op


def enquadro(lista):
    l = len(lista)

    print("|", end="")

    for i in range(l):
        j = i + 1
        if i % 2 == 0:
            print(f"{'':>2}[{j}] {lista[i]: <20}  ", end="")
            if lista[i] == lista[-1]:
                print(f"{'':>2}{'|':>31}", end="")
        else:
            print(f"{'':>2}[{j}] {lista[i]:<25} ", end='|')
            if lista[i] == lista[-1]:
                break
            print("\n|", end="")
    print("\n|", end='')
    print("_" * 60, end='')
    print("|", end='\n\n\n')


def check(op):
    while True:
        if op in list(range(1, 6)):
            return op

        else:
            op = int(input('Deseja [1] Continuar     [2] Sair\n-> '))
            if op == 1:
                start()
            else:
                break


def avaliacao(op):
    if op == 1:
        v, nUnidaed = distancia()
    if op == 2:
        v, nUnidaed = massa()
    if op == 3:
        v, nUnidaed = temperatura()
    if op == 4:
        v, nUnidaed = velocidade()
    if op == 5:
        v, nUnidaed = tempo()
    resultado(v, nUnidaed)
    check(-1)


def distancia():
    apresentacao("Distância")
    x, y, value = apresentaUnidades(uniDistancia)

    if x == 1 and y == 2:
        value = value * 1000
    elif x == 1 and y == 3:
        value = value * 1000**2

    elif x == 2 and y == 1:
        value = value / 1000
    elif x == 2 and y == 3:
        value = value * 1000

    elif x == 3 and y == 2:
        value = value / 1000
    elif x == 3 and y == 1:
        value = value / 1000**2
    apresentaConversao(uniDistancia[x-1], uniDistancia[y-1])
    return value, uniDistancia[y-1]




def massa():
    apresentacao("Massa")
    x, y, value = apresentaUnidades(uniMassa)
    if x == 1 and y == 2:
        value = value * 1000
    elif x == 1 and y == 3:
        value = value * 1000 ** 2

    elif x == 2 and y == 1:
        value = value / 1000
    elif x == 2 and y == 3:
        value = value * 1000

    elif x == 3 and y == 2:
        value = value / 1000
    elif x == 3 and y == 1:
        value = value / 1000 ** 2
    apresentaConversao(uniMassa[x-1], uniMassa[y-1])

    return value, uniMassa[y-1]


def temperatura():
    apresentacao("Temperatura")
    x, y, value = apresentaUnidades(uniTemperatura)
    # Cº -> Fº
    if x == 1 and y == 2:
        value = (value*1.8)+32
    # Cº -> Kº
    elif x == 1 and y == 3:
        value = value + 273.15
    # Fº -> Cº
    elif x == 2 and y == 1:
        value = (value - 32)*5/9
    # Fº -> Kº
    elif x == 2 and y == 3:
        value = (value - 32)*5/9 + 273.15
    # Kº -> Cº
    elif x == 3 and y == 2:
        value = (value - 273.15) * 1.8 + 32
    elif x == 3 and y == 1:
        value = value - 273.15
    apresentaConversao(uniTemperatura[x], uniTemperatura[y])

    return value, uniTemperatura[y-1]

def velocidade():
    apresentacao("Velocidade")
    x, y, value = apresentaUnidades(uniVelocidade)

    if x == 1 and y == 2:
        value = value / 3.6
    elif x == 2 and y == 1:
        value = value * 3,6
    apresentaConversao(uniVelocidade[x], uniVelocidade[y])

    return value, uniTemperatura[y-1]


def tempo():
    apresentacao("Tempo")
    x, y, value = apresentaUnidades(uniTempo)
    # Horas -> Minutos
    if x == 1 and y == 2:
        value = value * 60
    # Horas -> Segundos
    elif x == 1 and y == 3:
        value = value * 60**2
    # Minutos -> Horas
    elif x == 2 and y == 1:
        value = value / 60
    # Minutos -> Segundos
    elif x == 2 and y == 3:
        value = value * 60

    elif x == 3 and y == 1:
        value = value / 60**2
    elif x == 3 and y == 2:
        value = value / 60
    apresentaConversao(uniTempo[x], uniTempo[y])

    return value, uniTempo[y-1]


def apresentaUnidades(listaUnidades):
    enquadro(listaUnidades)


    uniNow = int(input("Qual Medida Você está usando agora?\n-> "))
    uniAfter = int(input("Para Qual Medida Você Deseja Converter?\n-> "))
    value = float(input("\nQual valor deve ser covertido?\n-> "))


    return uniNow, uniAfter, value
def resultado(r, novaUnidade):
    print("|", end="")
    for i in range(1):
        print(f"Resultado: {r:,.2f} {novaUnidade}".center(60), end="|")

    print("\n|", end='')
    print("_" * 60, end='')
    print("|", end='\n\n\n')

start()