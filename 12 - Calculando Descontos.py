#Calculando Descontos

n1 = float(input(' Qual e o preço do produto a dar o desconto? R$'))
d = 5
v = n1 * d / 100
f = n1 - v
print(f' O produto que custava R${n1:.2f} teve um desconto de {d}% e agora custa R${f:.2f} ')
