# Vamos desenhar a fórmula como imagem usando matplotlib

import matplotlib.pyplot as plt

# Criando a figura
plt.figure()

# Fórmula em formato LaTeX
formula = r"$f = \sqrt{\left(\frac{1}{1^c}\right) - \left(\frac{r^2}{4c^2}\right)}$"

# Adicionando a fórmula no centro da imagem
plt.text(0.5, 0.5, formula, ha='center')

# Removendo os eixos
plt.xticks([])
plt.yticks([])

# Exibindo
plt.show()
