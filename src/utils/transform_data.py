import PyPDF2
import tabula
import zipfile


pdf_file = open('test.pdf', 'rb')

#Faz a leitura usando a biblioteca
read_pdf = PyPDF2.PdfFileReader(pdf_file)

# pega o numero de páginas
number_of_pages = read_pdf.getNumPages()

array_quadros = ["Quadro 30", "Quadro 31", "Quadro 32"]
array_quadros_completo = []

def busca_inicio_quadros(pdf_read, number_pages, array_quadros):
    entrou_no_quadro = False
    for pagina in range(number_of_pages):
        numero_pagina_atual = pagina + 1
        pagina_atual = read_pdf.getPage(pagina)
        page_content = pagina_atual.extractText()
        sem_quebra = page_content.replace("\n", "")
        for quadro in array_quadros:
            if entrou_no_quadro == True:
                res_search_fonte = sem_quebra.find("Fonte:")
                if res_search_fonte != -1:
                    busca_fim_quadros(numero_pagina_atual)
            res_search_quadro = sem_quebra.find(quadro)
            if (res_search_quadro != -1):
                array_quadros_completo.append({'quadro':quadro, 'pagina_inicio':numero_pagina_atual})
                entrou_no_quadro = True
                array_quadros.remove(quadro)
                if quadro == "Quadro 32":
                    busca_fim_quadros(numero_pagina_atual)

def busca_fim_quadros(pagina):
    # print(f'Finalizou na página {pagina}')
    entrou_no_quadro = False
    array_quadros_completo[-1]['pagina_final'] = pagina


busca_inicio_quadros(read_pdf, number_of_pages, array_quadros)


# Lendo tabelas com erros no Tabula
def tratando_tabela_com_erros(tabela):
# for tabela in dfs:
#     for linha in tabela:
    #     print(linha)
    # print('ESTA', tabela, type(tabela))
    # print(list(tabela.columns))
    primeira_coluna = tabela.iloc[:, 0]
    new = primeira_coluna.str.split(" ", n=1, expand=True)
    tabela["Código"] = new[0]
    tabela["Descrição da categoria"] = new[1]

    tabela.drop(tabela.columns[0], axis=1, inplace=True)
    tabela = tabela.dropna()
    tabela = tabela.iloc[1: , :]
    return tabela



def add_novo_arquivo_obj_com_erros(quadro_atual, quadro):
    for col in quadro_atual.columns:
        nome_arquivo_CSV = col.replace(" ", "")
        quadro['nome_arquivo'] = nome_arquivo_CSV
        return nome_arquivo_CSV

def add_novo_arquivo_obj(quadro_atual, quadro):
    coluna = quadro_atual.columns[1]
    nome_arquivo_csv = coluna.replace(" ", "")
    quadro['nome-arquivo'] = nome_arquivo_csv
    return nome_arquivo_csv


arquivos_csv = []
for quadro in array_quadros_completo:
    pagina_inicial = quadro['pagina_inicio']
    pagina_final = quadro['pagina_final']
    quadros_pagina_inicial = tabula.read_pdf("test.pdf", pages=pagina_inicial)
    qtdade_quadros_pagina_inicial = len(quadros_pagina_inicial)

    if qtdade_quadros_pagina_inicial == 1:
        quadro_atual = quadros_pagina_inicial[0]
    else:
        quadro_atual = quadros_pagina_inicial[1]

    if pagina_final == pagina_inicial:
        qtdade_colunas_tabela = len(list(quadro_atual.columns))
        if qtdade_colunas_tabela == 1:
            nome_arquivo_csv = add_novo_arquivo_obj_com_erros(quadro_atual, quadro)
            tabela = tratando_tabela_com_erros(quadro_atual)
            tabela.to_csv(f'{nome_arquivo_csv}.csv', index=False)
            arquivos_csv.append(f'{nome_arquivo_csv}.csv')

    else:
        array_quadros = []
        for pagina in range(pagina_inicial, pagina_final + 1):
            quadro_pagina_atual = tabula.read_pdf("test.pdf", pages=pagina)
            if pagina == pagina_inicial:
                quadro_pagina_atual = quadro_atual
                nome_arquivo_csv = add_novo_arquivo_obj(quadro_atual, quadro)
                quadro_pagina_atual.to_csv(f'{nome_arquivo_csv}.csv', index=False, header=False)
                arquivos_csv.append(f'{nome_arquivo_csv}.csv')
            else:
                quadro_pagina_atual = quadro_pagina_atual[0]
                quadro_pagina_atual.to_csv(f'{nome_arquivo_csv}.csv', mode='a', index=False)


def criando_arquivo_zip(arquivos_csv):
    z = zipfile.ZipFile('Teste_{Marcio_Vieira}.zip', 'w', zipfile.ZIP_DEFLATED)
    for arquivo in arquivos_csv:
        z.write(arquivo)
    z.close()

criando_arquivo_zip(arquivos_csv)

'''
Coisas a fazer:

 - Refatorar código alterando as funções, colocando em novos módulos
 - Arrumar as condicionais de 'pagina_final == pagina_inicial' e 'qtdade_colunas_tabela' == 0, adicionando else, 
    visto que em outros casos a tabela de várias páginas poderia ter um início em página com outras tabelas
 - Colocar no main.py o início dos dois programas
 - Fazer Documentação dos programas!!!
 
'''