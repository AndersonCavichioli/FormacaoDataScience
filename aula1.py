import pandas as pd

notas = pd.read_csv("./arquivos/ratings.csv")
a = notas.head(notas) #head lê as 5 primeiras e 5 ultimas avaliações do arquivo

notas.shape(notas) #Detalha todo o conteudo do arquivo, nesse caso aqui, contendo 100836 linhas e 4 colunas

notas.columns = ["usuarioID", "filmeID", "nota", "momento"] #altera o nome das colunas contidas no arquivo
print(a)