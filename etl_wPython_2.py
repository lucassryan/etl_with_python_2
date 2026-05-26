import pandas as pd
import csv

def extrair_dados(arquivo):
    dados = []

    with open(arquivo, mode='r', encoding='utf-8-sig') as arquivo:
        infos = csv.DictReader(arquivo)

        for linha in infos:
            dados.append(linha)

    return(dados)

'''dados = extrair_dados('dataset_vendas.csv')
for linha in dados[:200]:
    print(linha)'''


def transformar_dados(dados):
    dados_tratados = []

    for linha in dados:

        #Trata a data da venda
        data_venda = linha['data_venda'].strip().replace('-', ' ').replace('/', ' ').split()

        partes_data_venda = len(data_venda)

        if partes_data_venda == 3:
            bloco1 = data_venda[0]
            bloco2 = data_venda[1]
            bloco3 = data_venda[2]

            tamanho_primeiro_bloco = len(bloco1)

            bloco1 = int(data_venda[0])
            bloco2 = int(data_venda[1])
            bloco3 = int(data_venda[2])

            if tamanho_primeiro_bloco == 4:
                ano = bloco1
                mes = bloco2
                dia = bloco3

                ano = f'{ano:04d}'
                mes = f'{mes:02d}'
                dia = f'{dia:02d}'

                data_venda_format = f'{ano}-{mes}-{dia}'

            elif tamanho_primeiro_bloco == 2:
                dia = bloco1
                mes = bloco2
                ano = bloco3

                dia = f'{dia:02d}'
                mes = f'{mes:02d}'
                ano = f'{ano:04d}'

                data_venda_format = f'{ano}-{mes}-{dia}'

            else:
                data_venda_format = None

        else:
            data_venda_format = None

        #Trata o nome dos clientes
        cliente = linha['cliente'].strip().capitalize()

        if cliente == '':
            cliente = None
        else:
            cliente_format = cliente

        #Trata o gênero
        genero = linha['genero'].strip().lower()

        if genero != '':
            if genero[0] == 'f':
                genero = 'Feminino'
            if genero[0] == 'm':
                genero = 'Masculino'
            else:
                genero = None
        else:
            genero = None

        #Trata o produto
        produto = linha['produto'].strip().capitalize()

        if produto == '':
            produto = None
        else:
            produto_format = produto

        
        #Trata o preço
        preco = linha['preco'].strip()
        preco = str(preco)

        preco = preco.replace('R$', '').replace('.', '').replace(',', '.')

        preco_format = float(preco)

        #Trata a quantidade
        quantidade = linha['quantidade'].strip()

        if quantidade != '':
            quantidade = int(quantidade)
        else:
            quantidade = None


        #Trata o total
        total = linha['total'].strip()

        if total != '':
            total = int(total)
        else:
            total = None
        
        #Trata o tempo de entrega
        tempo_entrega = linha['tempo_entrega'].strip()
        tempo_entrega = tempo_entrega.lower().replace('h', ' ').replace('m', ' ').replace(':', ' ').replace('s', ' ').split()

        quantidade = len(tempo_entrega)

        tempo_entrega_format = None

        if quantidade == 3:
            hora = int(tempo_entrega[0])
            minuto = int(tempo_entrega[1])
            segundo = int(tempo_entrega[2])

            hora = f'{hora:02d}'
            minuto = f'{minuto:02d}'
            segundo = f'{segundo:02d}'

            tempo_entrega_format = f'{hora}:{minuto}:{segundo}'
        
        elif quantidade == 2:
            hora = 00
            minuto = int(tempo_entrega[0])
            segundo = int(tempo_entrega[1])

            minuto = f'{minuto:02d}'
            segundo = f'{segundo:02d}'

            tempo_entrega_format = f'{hora}:{minuto}:{segundo}'

        #Trata a cidade
        cidade = linha['cidade'].strip().capitalize()

        if cidade == '':
            cidade = None
        else:
            cidade_format = cidade

        nova_linha = {
            'cliente': cliente_format,
            'data_venda': data_venda_format,
            'genero': genero,
            'produto': produto_format,
            'preco': preco_format,
            'quantidade': quantidade,
            'total': total,
            'tempo_entrega': tempo_entrega_format,
            'cidade': cidade_format
        }

        dados_tratados.append(nova_linha)

    return(dados_tratados)

'''dados_tratados = transformar_dados(dados)
for linha in dados_tratados[:200]:
    print(linha)'''

##========== LOAD ==========##
#Função carregar o dado em um novo arquivo
def salvar_dados(dados_tratados, dados_final):
    colunas = dados_tratados[0].keys()

    with open(dados_final, mode='w', newline='', encoding='utf-8-sig') as arquivo_final:

        escritor_csv = csv.DictWriter(arquivo_final, fieldnames=colunas)

        escritor_csv.writeheader()
        escritor_csv.writerows(dados_tratados)

##========= ORQUESTRAÇÃO DO PIPELINE =========##

def main():

    #Arquivos de entrada e saida
    arquivo_entrada = 'arquivos/dataset_vendas.csv'
    arquivo_saida = 'arquivos/dataset_vendas_limpo.csv'


    #=== EXTRACT ===#
    #Chamo a função que extrai os dados do arquivo bruto
    dados = extrair_dados(arquivo_entrada)

    #=== TRANSFORM ===#
    dados_tratados = transformar_dados(dados)
    print('Dados limpos.')

    #=== LOAD ===#

    salvar_dados(dados_tratados, arquivo_saida)

#Verifica se o código esta sendo executado diretamente e executa
if __name__ == "__main__":
    main()

