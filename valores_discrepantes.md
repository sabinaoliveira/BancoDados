VALORES DISCREPANTES:

calculamos a média e o desvio padrão dos salários com mean() e std(), usando media_salario e desvio_salario, respectivamente. definimos o limite superior como media_salario + (3*desvio_salario), resultando em 64,806.16, um valor adequado para outliers

Após identificar os outliers, decidimos se os removeríamos ou substituiríamos. no nosso caso, verificamos a faixa salarial e substituímos salários discrepantes pela média da faixa correspondente, garantindo coerência