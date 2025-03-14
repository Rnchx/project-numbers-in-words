def numeros_por_extenso(numero):
    if numero < 0 or numero > 999999:
        return "Número fora do intervalo de 0 a 999999."

    unidades = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
    especiais = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
    dezenas = ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
    centenas = ['', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']

    if numero < 10:
        return unidades[numero]

    milhar = numero // 1000
    resto = numero % 1000
    centena = resto // 100
    resto = resto % 100
    dezena = resto // 10
    unidade = resto % 10

    partes = []

    if milhar > 0:
        if milhar == 1:
            partes.append("mil")
        else:
            partes.append(milhar + " mil")

    if centena > 0:
        if centena == 1 and dezena == 0 and unidade == 0:
            partes.append("cem")
        else:
            partes.append(centenas[centena])

    if dezena > 0:
        if dezena == 1:
            partes.append(especiais[unidade])
        else:
            partes.append(dezenas[dezena])

    if unidade > 0 and dezena != 1:
        partes.append(unidades[unidade])

    return " e ".join(partes)

while True:
    try:
        numero = int(input("Digite um número para retorná-lo escrito por extenso: "))
        print(numeros_por_extenso(numero))
    except ValueError:
        print("Digite apenas números!")
