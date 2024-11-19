import pandas as pd 
import numpy as np 

try:

    print('Obtendo Dados...')
    ENDERECO_DADOS_VENDAS = 'tb_Vendas2017_Miranda.csv'
    ENDERECO_DADOS_CADASTRO = 'tb_CadastroProdutos2017_Miranda.csv'

    df_vendas = pd.read_csv(ENDERECO_DADOS_VENDAS, sep=';', encoding= 'Iso-8859-1')
    
    df_vendas_produtos = df_vendas[['Quantidade Vendida', 'ID Produto']]
    # df_vendas_produtos = df_vendas_produtos.sum(['Quantidade Vendida']

    print(df_vendas_produtos)
    print('Dados obtidos com sucesso!')
    print(30*'=')

    print('Obtendo Dados...')
    df_produtos = pd.read_csv(ENDERECO_DADOS_CADASTRO,sep=';', encoding='Iso-8859-1')

    df_cadastro_produtos = df_produtos[['Tipo' , 'Categoria' , 'Preco Unitario' , 'ID Produto']]
    df_produtos.loc[:, 'Preco Unitario'] = df_produtos[
       'Preco Unitario'].str.replace(',','.').astype(float)
    
    print(df_cadastro_produtos)
    print('Dados Obtidos com Sucesso!!!')
    print(30*'=')   

 
    # array_vendas_produtos = np.array(df_vendas['Quantidade Vendida'])
    # media_vendas_produtos = np.mean(array_vendas_produtos)
    # mediana_vendas_produtos = np.median(array_vendas_produtos)
    # maximo = np.max(array_vendas_produtos)
    # minimo = np.min(array_vendas_produtos)
    # q1 = np.quantile(array_vendas_produtos, 0.25, method='weibull')
    # q2 = np.quantile(array_vendas_produtos, 0.75, method='weibull')
    # iqr = q2 - q1
    # Amplitude = maximo - minimo 
    # limite_inferior = q1 - (1.5*iqr)
    # limite_superior = q2 + (1.5*iqr)

    # print('Valores de Vendas: ')

    # print(F'Maior Valor {maximo}')
    # print(f'Menor Valor {minimo}')
    # print(f'Limite superior: {limite_superior}')
    # print(f'Limite inferior: {limite_inferior}')




except Exception as e:
 print(f'Erro ao obter dados: {e}')

try:

    
    array_vendas_produtos = np.array(df_vendas['Quantidade Vendida'])
    media_vendas_produtos = np.mean(array_vendas_produtos)
    mediana_vendas_produtos = np.median(array_vendas_produtos)
    maximo = np.max(array_vendas_produtos)
    minimo = np.min(array_vendas_produtos)
    q1 = np.quantile(array_vendas_produtos, 0.25, method='weibull')
    q2 = np.quantile(array_vendas_produtos, 0.50, method='weibull')
    q3 = np.quantile(array_vendas_produtos, 0.75, method='weibull')
    distancia = abs(
       (media_vendas_produtos - mediana_vendas_produtos) / mediana_vendas_produtos *100
    )
    iqr = q3 - q1
    Amplitude = maximo - minimo 
    limite_inferior = q1 - (1.5*iqr)
    limite_superior = q3 + (1.5*iqr)
   

    print('Valores de Vendas: ')
    print(f'Média do Valor Total: {media_vendas_produtos}')
    print(f'Mediana do Valor total: {mediana_vendas_produtos}')
    print(f'Distância de Valor total: {mediana_vendas_produtos}')
    print(F'Maior Valor {maximo}')
    print(f'Menor Valor {minimo}')
    print(f'Limite superior: {limite_superior}')
    print(f'Limite inferior: {limite_inferior}')
    df_vendas_produtos_outliers_inferiores = df_vendas_produtos[
       df_vendas_produtos['Quantidade Vendida'] < limite_inferior
    ]
    df_vendas_produtos_outliers_superiores = df_vendas_produtos[
       df_vendas_produtos['Quantidade Vendida'] > limite_superior
    ]


    print('\nOutliers inferiores: ')
    print(30*'=')
    if len(df_vendas_produtos_outliers_inferiores) == 0:
       print('Não existem outliers inferiores!')
    else:
       print(df_vendas_produtos_outliers_superiores.sort_values(
          by='Quantidade Vendida', ascending=False
       ))

                                                               
    

except Exception as e:
   print(f'Erro ao obter dados:')
