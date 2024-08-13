Feature Engineering

def preencher_nivel(gestor,nivel):
  if gestor==1:
    return "Pessoa Gestora"
  else:
    return nivel

dados.apply(lambda x: preencher_nivel())



    



