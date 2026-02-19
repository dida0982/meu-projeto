n = int(input("Digite o tamanho da lista: ")) #input para pegar texto. int para converter o texto em número.

contador = 0 #começa com 0

while n > 1:
    n = n // 2
    contador += 1 # acrescenta o número de etapas / Ele só registra que uma divisão aconteceu.

print(f"Número máximo de etapas na pesquisa binária: {contador}")
#f → permite colocar variáveis dentro da string / {variavel} → mostra o valor da variável
