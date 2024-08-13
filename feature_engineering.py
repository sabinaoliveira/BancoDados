Feature Engineering

def preencher_nivel(gestor,nivel):
  if gestor==1:
    return "Pessoa Gestora"
  else:
    return nivel

dados["NOVO_NIVEL"] = dados.apply(lambda x: preencher_nivel(x["GESTOR"], x["NIVEL"]), axis=1)

dados["NOVO_NIVEL"].value_counts()

dados = pd.get_dummies(dados, columns=["NIVEL"])

def determinar_geracao(idade):
  if 39<idade<58:
    return "Geração X"
  elif 29<idade <=39:
    return "MilLenial"
  elif 13<idade <=29:
    return "Geração Z"
  else:
    return "Outra geração"

  dados["GERACAO"] = dados["IDADE"].apply(determinar_geracao)

  dados["GERACAO"].value_counts()

  



    



