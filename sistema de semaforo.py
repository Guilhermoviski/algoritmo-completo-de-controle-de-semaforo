print("semaforo está em que cor, digite 1 para vermelho, 2 para verde e 3 para amarelo.")
corSema = int(input())

pontoCNH = int(0)
totalValorMulta = float(0)
totalMulta = int(0)

if corSema == 1:

    print("você passou pelo sinal vermelho e recebeu uma multa gravíssima, 7 pontos, 293,47 reais por avançar o sinal vermelho.")

    pontoCNH += 7

    totalValorMulta += 293.47

    totalMulta += 1

elif corSema == 3:
    print("você recebeu um aviso por passar no semaforo amarelo.")

elif corSema == 2:
    print("você passou pelo semaforo verde, tudo certo.")

print("você está a quantos km/hr?")
velocidade = float(input())

print("quanto é o limite da via")
limitVia = float(input())

limitPorcen = (velocidade - limitVia) * 100/limitVia

#aviso por passar no limite

if limitPorcen <= 9:
    print(f"descrição detalhada da sua CNH: {pontoCNH} pontos. {totalValorMulta: .2f} Reais de multa e {totalMulta} multa(s) no total.")

#multa 10 - 19%

elif limitPorcen >= 10 and limitPorcen <= 19:
    print(f"você foi multado em 4 pontos e 130,14 reais por passar{limitPorcen: .0f}% acima do limite da via.")

    pontoCNH += 4
    totalValorMulta += 130.14
    totalMulta += 1

    print(f"descrição detalhada da sua CNH: {pontoCNH} pontos. {totalValorMulta: .2f} Reais de multa e {totalMulta} multa(s) no total.")

#multa 20 - 49%

elif limitPorcen >= 20 and limitPorcen <= 49:
    print(f"você foi multado em 5 pontos e 195,23 reais por passar{limitPorcen: .0f}% acima do limite da via.")

    pontoCNH += 5
    totalValorMulta += 195.23
    totalMulta += 1

    print(f"descrição detalhada da sua CNH: {pontoCNH} pontos. {totalValorMulta: .2f} Reais de multa e {totalMulta} multa(s) no total.")

#multa 50%+

elif limitPorcen >= 50:
    print(f"você foi multado em 5 pontos e 880,41 reais por passar{limitPorcen: .0f}% acima do limite da via.")

    totalValorMulta += 880.41
    totalMulta += 1

    print(f"descrição detalhada da sua CNH: {pontoCNH} pontos. {totalValorMulta} Reais de multa e {totalMulta} multa(s) no total. AVISO! SUA CNH RECEBEU UMA SUSPENSÃO IMEDIATA DO DIREITO DE DIRIGIR")

