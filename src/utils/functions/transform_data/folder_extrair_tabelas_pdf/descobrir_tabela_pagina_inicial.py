import re

def descobrir_tabela_pagina_inicial(read_pdf, nome_quadro, pagina_final, qtdade_tabelas_pagina_inicial):
    pagina_atual = read_pdf.getPage(pagina_final - 1)
    page_content = pagina_atual.extractText()

    # Retirar quebra de página para realizar a busca das Tabelas
    sem_quebra = page_content.replace("\n", "")
    qtdade_quadros_inicio_fim_na_pagina = re.findall("(Quadro\s(\w+))(?s:.*?)(Fonte:)", sem_quebra)
    index = 0
    for quadro in qtdade_quadros_inicio_fim_na_pagina:
        if quadro[0] == nome_quadro:
            if (len(qtdade_quadros_inicio_fim_na_pagina)) == qtdade_tabelas_pagina_inicial:
                return index
            else:
                return index + 1
        index += 1