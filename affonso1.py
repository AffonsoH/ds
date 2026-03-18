altura = float(input("Qual sua altura? "))
peso = float(input("Qual seu peso? "))
imc = float(peso / (altura*altura))
idade = int(input("Qual sua idade?"))
if idade > 59:
    if imc < 22.18:
        print(listadepesos[0]);
    elif imc < 27.1:
        print(listadepesos[1]);
    elif imc < 30.1:
        print(listadepesos[2]);
    elif imc > 30.0:
        print(listadepesos[3]);
    ;
atleta = input("Você pratica algum esporte ou faz exercícios físicos? ")
listadepesos = ["Abaixo do peso", "Peso normal", "Acima do peso", "Obesidade grau 1", "Obesidade grau 2", "Obesdidade grau 3"]
if atleta == "Sim" or atleta == "sim" or atleta == "s":
    if imc < 18.6:
        print(listadepesos[0]);
    elif imc < 30.0:
        print(listadepesos[1]);
    elif imc < 40:
        print(listadepesos[2])
elif imc < 18.6:
    print(listadepesos[0]);
elif imc < 25.0:
    print(listadepesos[1]);
elif imc < 30.0:
    print(listadepesos[2]);
elif imc < 35.0:
    print(listadepesos[3]);
elif imc < 40:
    print(listadepesos[4]);
elif imc >= 40:
    print(listadepesos[5])