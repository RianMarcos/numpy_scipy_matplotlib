import numpy as np
import matplotlib.pyplot as plt


'''
- Lista de Exercícios II - 
- Trabalho individual

Usando NumPy, MatPlotLib e SciPy implemente os seguintes exercícios para exploração
e fixação de comandos e métodos destes módulos.

Os gráficos plotados ou cópias de tela de execução destes exercícios estão 
disponíveis na pasta "Exemplos de Resultados" e servem para exemplificar
uma possível solução (estão lá apenas para servir de apoio de explicação).


1) Utilizando o  intervalo [-PI, +PI], plote um gráfico usando o cos(x) como abscissa e o sen(x) como ordenada.
   Pesquise a função sobre axes no matplotlib (ou como foi feito nos exemplos anteriores) 
   para deixar o gráfico quadrado, mesma proporção largura x altura, 
   caso contrário o círculo parecerá uma elipse.
'''

v = np.linspace(-np.pi, np.pi, 100)
x = np.cos(v)
y = np.sin(v)

plt.figure(figsize=(5, 5))
plt.plot(x, y)
plt.show()


'''
2) Empregando sen(x) no mesmo intervalo [-PI, +PI], mas agora usando np.arange (com passo 0.2), 
   plote 6 gráficos, de sen(x) até sen(x-1), deslocando cada plot de 0.2,
   ou seja sen(x), sen(x-0.2) etc., usando para chamada ao plot os seguintes modelos de linhas:
   '-'    '--'    ':'     '-.'      '.'      'o'
   Depois, brinque com o parâmetro opcional color='cor' testando cores disponíveis (ver na documentação)
'''

v = np.arange(-np.pi, np.pi, 0.2)

graphs = [np.sin(v-i) for i in np.arange(0, 1.1001, 0.2)]
lines = ["-", "--", ":", "-.", ".", "o"]
for i, graph in enumerate(graphs):
    plt.plot(v, graph, lines[i])
plt.show()


'''
3) Plote os dois polinômios f(x) e g(x):
   f(x) = -2xˆ4 + 3xˆ3 + 7xˆ2 -10x + 18
   g(x) = xˆ4 +2xˆ3  -13xˆ2 -14x + 24
   Com x no intervalo [-4.5, 4.5] com 300 pontos. Antes de plt.show(), chame plt.grid(). 
   Implemente as funções em código Python:
   def f(x): 
      # retorno da função f
   def g(x): 
      # retorno da função g     
   Coloque as equações dos polinômios como rótulos (ver nos exemplos anteriores).
   Pesquise como centralizar os spines em 0,0 de forma a criar um gráfico com 
   os eixos cartesianos mostrados no formato tradicional.
'''

x = np.linspace(-4.5, 4.5, 300)
f_x = np.poly1d([-2, 3, 7, -10, 18])
g_x = np.poly1d([1, 2, -13, -14, 24])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.plot(x, f_x(x), label=r"$f(x) = -2x^4 + 3x^3 + 7x^2 - 10x +18$")
plt.plot(x, g_x(x), label=r"$g(x) = xˆ4 +2xˆ3  -13xˆ2 -14x + 24$")

plt.legend()
plt.show()


'''
4) Crie uma função python que retorna o maior de dois números enviados por parâmetro.
   Ela irá funcionar de maneira regular, ou seja, operando sobre 2 escalares.
   Verifique o funcionamento da função NumPy vectorize, e crie então a função
   que opera sobre vetores.

   Teste sua função duas vezes:
   a) com dois arrays numpy de 10 posições sorteadas de números inteiros
   no intervalo [10, 100[
   b) com dois arrays numpy de 10 posições sorteadas de números reais
   no intervalo ]0, 1[ .
   Em ambos cenários mostre os 3 vetores e use funções do NumPy para o sorteio.

'''

#4 dois arrays numpy de 10 posições sorteadas de números inteiros
def maior_2_numeros(x, y):
    if x > y:
        return x
    return y


vfunc = np.vectorize(maior_2_numeros)

a = np.random.randint(10, 100, 10)
b = np.random.randint(10, 100, 10)
c = vfunc(a, b)

print(f"a = {a}")
print(f"b = {b}")
print(f"MÁXIMOS= {c}")


print("==== 4.B)====")

# B) DOIS ARRAYS NUMPY DE 10 POSIÇÕES SORTEADAS DE NÚMEROS REAIS

d = np.random.random_sample(10)
e = np.random.random_sample(10)
f = vfunc(d, e)


print("Primeiro vetor randomico: ", d)
print("Segundo vetor randomico: ", e)
print("Máximos: ", f)

#print(f"d = {d}")
#print(f"e = {e}")
#print(f"MÁXIMOS DE f = {f}")




'''
5) Calculando área aproximada com Soma de Riemann

   Elabore um programa que aplique a Soma de Riemann para estimar a área
   solicitando ao usuário o tamanho do passo (base do retângulo), apresente
   o valor estimado da área e o erro relativo.
   Os passos devem ser frações exatas de 1, como por exemplo:
   1, 0.5, 0.25, 0.125, 0.1, 0.0625, 0.05, 0.04, 0.03125, 0.025, 0.0125 etc
   para não extrapolarem o intervalo.

   Erro relativo = | analitico - aproximado | / | analítico |

   Plote o gráfico apresentando os retângulos, o valor aproximado e o erro
   relativo.
   Dica para plotar os retângulos: simplesmente usar plt.bar (deixando as cores sem interferir)
   https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html

   Para comparar o resultados, crie 3 gráficos (sub plots) na mesma plotagem
   e contabilize os três valores da área calculada:
   - pegando altura pela esquerda (antes do passo)
   - pegando altura no meio (métade do passo)
   - pegando altura pela direita (depois do passo)

   Use a função python criada para calcular as seguintes integrais definidas:
   a) Para a reta f(x) = 2x, integrada no intervalo [1, 4], cuja solução analítica é 15.
   (ver gráficos exemplos de resultado)

   b) Para a função f(x) = 1/8(x^2 -2x + 8), integrada no intervalo [-2, 4], cuja solução
   analítica é 15/6.
'''


def f(x):
    return 2*x


print("Digite o passo:")
passo = float(input())

a = 1
b = 4

# =======GRÁFICO 1=======

x = np.linspace(0, 5, 100)

X = np.arange(a, b, passo)

plt.subplot(1, 3, 1)
plt.plot(x, 2*x)
x = 0
y = 0
area = 0
for i in range(int((b-a)/passo)):
    x = X[i] + passo/2
    y = f(X[i])
    area += passo*y
    plt.bar(x, y, passo)
plt.xlabel(
    f"Area aproximada = {area}\nArea calculada = 15.0\n Erro relativo = {100*(15-area)/15}%")
plt.axis("scaled")

# =======GRÁFICO 2=======
plt.subplot(1, 3, 2)
x = np.linspace(0, 5, 100)
plt.plot(x, 2*x)
x = 0
y = 0
area = 0

for i in range(int((b-a)/passo)):
    x = X[i]+passo/2
    y = f(X[i] + passo/2)
    area += passo*y
    plt.bar(x, y, passo)
plt.xlabel(
    f"Area aproximada = {area}\nArea Calculada = 15.0\n Erro relativo = {100* (15-area)/15}%")
plt.axis("Scaled")

# =======GRÁFICO 3=======

plt.subplot(1, 3, 3)
x = np.linspace(0, 5, 100)
plt.plot(x, 2*x)
x = 0
y = 0
area = 0

for i in range(int((b-a)/passo)):
    x = X[i] + passo/2
    y = f(X[i] + passo)
    area += passo*y
    plt.bar(x, y, passo)
plt.xlabel(
    f"Area aproximada = {area}\nArea calculada = 15.0\n Erro relativo = {100 * (area - 15)/15}%")
plt.axis("scaled")
plt.show()

 
#LETRA B

def f(x):
    return 1/8*(x**2 - 2*x + 8)


print("Digite o passo:")
passo = float(input())

a = -2
b = 4


# =======GRÁFICO 1=======

x = np.linspace(-2, 4, 100)

X = np.arange(a, b, passo)

plt.subplot(1, 3, 1)
plt.plot(x, 1/8*(x**2 - 2*x + 8))
x = 0
y = 0
area = 0
for i in range(int((b-a)/passo)):
    x = X[i] + passo/2
    y = f(X[i])
    area += passo*y
    plt.bar(x, y, passo)
plt.xlabel(
    f"Area aproximada = {area}\nArea calculada = 15/2\n Erro relativo = {100*((15/2)-area)/15}%")
plt.axis("scaled")

# =======GRÁFICO 2=======
plt.subplot(1, 3, 2)
x = np.linspace(-2, 4, 100)
plt.plot(x, 1/8*(x**2 - 2*x + 8))
x = 0
y = 0
area = 0

for i in range(int((b-a)/passo)):
    x = X[i]+passo/2
    y = f(X[i] + passo/2)
    area += passo*y
    plt.bar(x, y, passo)
plt.xlabel(
    f"Area aproximada = {area}\nArea Calculada = 15/2\n Erro relativo = {100* ((15/2)-area)/15}%")
plt.axis("Scaled")

# =======GRÁFICO 3=======

plt.subplot(1, 3, 3)
x = np.linspace(-2, 4, 100)
plt.plot(x, 1/8*(x**2 - 2*x + 8))
x = 0
y = 0
area = 0

for i in range(int((b-a)/passo)):
    x = X[i] + passo/2
    y = f(X[i] + passo)
    area += passo*y
    plt.bar(x, y, passo)
plt.xlabel(
    f"Area aproximada = {area}\nArea calculada = 15/2\n Erro relativo = {100 * (area - (15/2))/15}%")
plt.axis("scaled")
plt.show()
 
