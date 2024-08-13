Feature Engineering

def preencher_nivel(gestor,nivel):
  if gestor==1:
    return "Pessoa Gestora"
  else:
    return nivel

dados["NOVO_NIVEL"] = dados.apply(lambda x: preencher_nivel(x["GESTOR"], x["NIVEL"]), axis=1)



    



