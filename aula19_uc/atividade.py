import pandas as pd 
import numpy as np 



try:

 print('Obtendo dados...')

 ENDERECO_DADOS = 'BaseDPEvolucaoMensalCisp.csv'

 df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='Iso-8859-1')


 df_recup_veiculo = df_ocorrencias[['munic','recuperacao_veiculos']]
 df_recup_veiculo = df_recup_veiculo.groupby(['munic']).sum(['recuperacao_veiculos']).reset_index()

 print(df_recup_veiculo.head())
 print('Dados obtidos com sucesso!')

 array_recup_veiculo = np.array(df_recup_veiculo['recuperacao_veiculos'])
 
 media_recup_veiculo = np.mean(array_recup_veiculo)
 mediana_recup_veiculo = np.median(array_recup_veiculo)

 distancia = abs((media_recup_veiculo - mediana_recup_veiculo) / mediana_recup_veiculo)

 q1 = np.quantile(array_recup_veiculo, 0.25, method='weibull')
 q3 = np.quantile(array_recup_veiculo, 0.75, method='weibull')
 iqr = q3 - q1
 minimo = np. min(array_recup_veiculo)
 limite_inferior = q1 - (1.5*iqr)
 limite_superior = q3 + (1.5*iqr)
 maximo = np.max(array_recup_veiculo)
 amplitude_total = maximo - minimo 

 print('\nMedidas de Posição e Dispersão')
 print(30*'=')
 print(f'Menor valor: {minimo}')
 print(f'Limite inferior: {limite_inferior}')
 print(f'Q1: {q1}')
 print(f'Q3: {q3}')
 print(f'Limite superior: {limite_superior}')
 print(f'Maior valor: {maximo}')
 print(f'IQR: {iqr}')
 print(f'Amplitude total: {amplitude_total}')
 df_recup_veiculo_outliers_sup = df_recup_veiculo[
    df_recup_veiculo['recuperacao_veiculos'] > limite_superior
 ]

 print('\nDPs com recuperações superiores as demais:')
 print(30*'=')
 if len(df_recup_veiculo_outliers_sup) == 0:
    print('Não existem DPs com valores discrepantes superiores')

 else:
    print(df_recup_veiculo_outliers_sup.sort_values(
       by='recuperacao_veiculos', ascending=False 
    ))

except ImportError as e:
    print(f'Erro ao obter dados: {e}')
    exit()
