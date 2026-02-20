SB = float(input("Salário Bruto: "))
SL = float(input("Salário Líquido: "))
VH = float(input("Valor da hora-aula: "))
HT = int(input("Número de horas trbalhadas no mes: "))
PD = float(input("Percentual do desconto do INSS: "))
TD = float(input("Total de desconto: "))

SB = HT * VH
TD = (PD/100) * SB
SL = SB - TD

print("Salário bruto: , ", SB, "Salário Líquido: ", SL)
