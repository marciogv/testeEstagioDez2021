import PyPDF2
import re
import tabula
import pandas as pd


dfs = tabula.read_pdf("test.pdf", pages='114')
dfs2 = tabula.read_pdf("test.pdf", pages='115')

for tabela in dfs:
    print(list(tabela.columns))
    print(tabela.values)
    print(tabela.shape[1])


# Lendo tabelas com erros no Tabula
for tabela in dfs:
    # for linha in tabela:
    #     print(linha)
    # print(tabela, type(tabela))
    # print(list(tabela.columns))
    new = tabela['Tabela de Tipo do Demandante'].str.split(" ", n=1, expand=True)
    tabela["Código"] = new[0]
    tabela["Descrição da categoria"] = new[1]
    tabela.drop(columns=["Tabela de Tipo do Demandante"], inplace=True)
    # print(list(tabela.columns))
    # tabela.name = 'Tabela de Tipo de Demandante'
    print(list(tabela.columns))
    print(tabela.values)
    print(tabela.shape[1])
    # tabela.to_csv('testando_novamente.csv', header=False)


for tabela in dfs2:
    print(list(tabela.columns))
    print(tabela.values)
    print(tabela.shape[1])



# print(len(dfs))


# tabula.convert_into("teste2.pdf", "teste10.csv", output_format="csv", pages='120')
# tabula.convert_into("test.pdf", "teste3.json", output_format="json", pages='120')
# tabula.convert_into("test.pdf", "teste3.tsv", output_format="tsv", pages='120')


# dfs = tabula.read_pdf("test.pdf", pages=115, stream=True)


pdf_file = open('test.pdf', 'rb')







#
# #Faz a leitura usando a biblioteca
# read_pdf = PyPDF2.PdfFileReader(pdf_file)
#
# # pega o numero de páginas
# number_of_pages = read_pdf.getNumPages()
#
# array_quadros = ["Quadro 30", "Quadro 31", "Quadro 32"]
# array_quadros_completo = []
#
# def busca_inicio_quadros(pdf_read, number_pages, array_quadros):
#     entrou_no_quadro = False
#     for pagina in range(number_of_pages):
#         numero_pagina_atual = pagina + 1
#         print("PAGINA ATUAL:", numero_pagina_atual)
#         pagina_atual = read_pdf.getPage(pagina)
#         page_content = pagina_atual.extractText()
#         sem_quebra = page_content.replace("\n", "")
#         for quadro in array_quadros:
#             if entrou_no_quadro == True:
#                 res_search_fonte = sem_quebra.find("Fonte:")
#                 if res_search_fonte != -1:
#                     busca_fim_quadros(numero_pagina_atual)
#                     # break
#             res_search_quadro = sem_quebra.find(quadro)
#             if (res_search_quadro != -1):
#                 array_quadros_completo.append({'quadro':quadro, 'pagina_inicio':numero_pagina_atual})
#                 print(f'Começou na página {numero_pagina_atual}')
#                 entrou_no_quadro = True
#                 array_quadros.remove(quadro)
#                 if quadro == "Quadro 32":
#                     busca_fim_quadros(numero_pagina_atual)
#
# def busca_fim_quadros(pagina):
#     print(f'Finalizou na página {pagina}')
#     entrou_no_quadro = False
#     array_quadros_completo[-1]['pagina_final'] = pagina
#
#
# busca_inicio_quadros(read_pdf, number_of_pages, array_quadros)
# print(array_quadros_completo)

