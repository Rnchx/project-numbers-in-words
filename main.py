def numeros_por_extenso(numero):
    if numero < 0 or numero > 999999999999999999999999999999999999:
        print("Número fora do intervalo de 0 a 999999999999999999999999999999999999.")

    unidades = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
    especiais = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
    dezenas = ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
    centenas = ['', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']

    if numero < 10:
        return unidades[numero]
    
    decilhao = numero // 1000000000000000000000000000000000
    resto = numero % 1000000000000000000000000000000000
    nonilhao = resto // 1000000000000000000000000000000
    resto = resto % 1000000000000000000000000000000
    octilhao = resto // 1000000000000000000000000000
    resto = resto % 1000000000000000000000000000
    septilhao = resto // 1000000000000000000000000
    resto = resto % 1000000000000000000000000
    sextilhao = resto // 1000000000000000000000
    resto = resto % 1000000000000000000000
    quintilhao = resto // 1000000000000000000
    resto = resto % 1000000000000000000
    quatrilhao = resto // 1000000000000000
    resto = resto % 1000000000000000
    trilhao = resto // 1000000000000
    resto = resto % 1000000000000
    bilhao = resto // 1000000000
    resto = resto % 1000000000
    milhao = resto // 1000000
    resto = resto % 1000000
    milhar = resto // 1000
    resto = resto % 1000
    centena = resto // 100
    resto = resto % 100
    dezena = resto // 10
    unidade = resto % 10

    # milhar = numero // 1000
    # resto = numero % 1000
    # centena = resto // 100
    # resto = resto % 100
    # dezena = resto // 10
    # unidade = resto % 10

    partes = []

    if decilhao > 0:
        if decilhao == 1:
            partes.append("um decilhão")
        else:
            partes.append(numeros_por_extenso(decilhao) + " decilhões")

    if nonilhao > 0:
        if nonilhao == 1:
            partes.append("um nonilhão")
        else:
            partes.append(numeros_por_extenso(nonilhao) + " nonilhões")

    if octilhao > 0:
        if octilhao == 1:
            partes.append("um octilhão")
        else:
            partes.append(numeros_por_extenso(octilhao) + " octilões")

    if septilhao > 0:
        if septilhao == 1:
            partes.append("um septilão")
        else:
            partes.append(numeros_por_extenso(septilhao) + " septilhões")

    if sextilhao > 0:
        if sextilhao == 1:
            partes.append("um sextilhão")
        else:
            partes.append(numeros_por_extenso(sextilhao) + " sextilhões")

    if quintilhao > 0:
        if quintilhao == 1:
            partes.append("um quintilhão")
        else:
            partes.append(numeros_por_extenso(quintilhao) + " quintilhões")

    if quatrilhao > 0:
        if quatrilhao == 1:
            partes.append("um quatrilhão")
        else:
            partes.append(numeros_por_extenso(quatrilhao) + " quatrilhões")

    if trilhao > 0:
        if trilhao == 1:
            partes.append("um trilhão")
        else:
            partes.append(numeros_por_extenso(trilhao) + " trilhões")

    if bilhao > 0:
        if bilhao == 1:
            partes.append("um bilhão")
        else:
            partes.append(numeros_por_extenso(bilhao) + " bilhões")

    if milhao > 0:
        if milhao == 1:
            partes.append("um milhão")
        else:
            partes.append(numeros_por_extenso(milhao) + " milhões")        

    if milhar > 0:
        if milhar == 1:
            partes.append("mil")
        else:
            partes.append(numeros_por_extenso(milhar) + " mil")

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
