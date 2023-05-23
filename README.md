# numpy_scipy_matplotlib
 Segunda lista de ex métodos numéricos
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


2) Empregando sen(x) no mesmo intervalo [-PI, +PI], mas agora usando np.arange (com passo 0.2), 
   plote 6 gráficos, de sen(x) até sen(x-1), deslocando cada plot de 0.2,
   ou seja sen(x), sen(x-0.2) etc., usando para chamada ao plot os seguintes modelos de linhas:
   '-'    '--'    ':'     '-.'      '.'      'o'
   Depois, brinque com o parâmetro opcional color='cor' testando cores disponíveis (ver na documentação)


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
   analítica é 15/2.

'''
