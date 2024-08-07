Uso de bibliotecas de Python (pandas) - lendo e entendendo nossos dados

Leia os arquivos: usamos o  read_excel , mas pensamos também em usar o  read_csv , caso esse fosse o formato do nosso arquivo, ou  read_json . Ou seja, o pandas permite ler diferentes formatos de arquivo.

Espiar nossos dados: temos as  funções head e tail , em que podemos visualizar as primeiras e últimas linhas de nossa tabela respectivamente.

Ver a dimensão dos nossos dados: temos a  função len , que nos mostra a quantidade de linhas que temos e a  função shape , que mostra a quantidade de linhas e de colunas que temos.

Ter informações sobre os nossos dados: temos a  função columns , que nos diz quais são nossas colunas, a  função info  que nos mostra os índices, as colunas, o total de dados, a quantidade de cada tipo de dado, que nesse caso chamamos de dtypes, o quanto de cada variável são de valores não nulos (entenderemos melhor esse conceito mais à frente), e a memória que a nossa tabela está ocupando. E a  função describe, que nos dá informações sobre as variáveis numéricas, valores máximos e mínimos, média, desvio, mediana (também veremos esses conceitos mais a frente).


