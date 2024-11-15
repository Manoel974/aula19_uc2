import pandas as pd 
import numpy as np 

try:

    print('Obtendo Dados...')
    ENDERECO_DADOS_VENDAS = 'tb_Vendas2017_Miranda.csv'
    ENDERECO_DADOS_CADASTRO = 'tb_CadastroProdutos2017_Miranda.csv'

    df_vendas = pd.read_csv(ENDERECO_DADOS_VENDAS, sep=';', encoding= 'Iso-8859-1')
    
    df_vendas_produtos = df_vendas['Quantidade Vendida']
    # df_vendas_produtos = df_vendas_produtos.sum(['Quantidade Vendida']

    print(df_vendas_produtos)
    print('Dados obtidos com sucesso!')
    print(30*'=')

    print('Obtendo Dados...')
    df_produtos = pd.read_csv(ENDERECO_DADOS_CADASTRO,sep=';', encoding='Iso-8859-1')

    df_cadastro_produtos = df_produtos[['Tipo' , 'Categoria' , 'Custo Unitario' , 'Preco Unitario']]

    print(df_cadastro_produtos)
    print('Dados Obtidos com Sucesso!!!')
    print(30*'=')   


    array_vendas_produtos = np.array(df_vendas['Quantidade Vendida'])
    media_vendas_produtos = np.mean(array_vendas_produtos)
    mediana_vendas_produtos = np.median(array_vendas_produtos)
    maximo = np.max(array_vendas_produtos)
    minimo = np.min(array_vendas_produtos)
    q1 = np.quantile(array_vendas_produtos, 0.25, method='weibull')
    q2 = np.quantile(array_vendas_produtos, 0.75, method='weibull')
    iqr = q2 - q1
    Amplitude = maximo - minimo 
    limite_inferior = q1 - (1.5*iqr)
    limite_superior = q2 + (1.5*iqr)

    print('Valores de Vendas: ')

    print(F'Maior Valor {maximo}')
    print(f'Menor Valor {minimo}')
    print(f'Limite superior: {limite_superior}')
    print(f'Limite inferior: {limite_inferior}')




except Exception as e:
 print(f'Erro ao obter dados: {e}')