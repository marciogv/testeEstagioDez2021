# Teste 2 Estágio - Transformação de dados

## Tarefas de código:

* Extrair do pdf do teste 1 acima os dados dos Quadros 30,31,32 (Tabela de categoria do Padrão TISS);
* Salvar dados em tabelas estruturadas, em csvs;
* Zipar todos os csvs num arquivo "Teste_{seu_nome}.zip".

## Linguagem de programação utilizada
Python

## Pacotes/bibliotecas utilizadas
* PyPDF2 - leitura do arquivo 'pdf';
* Tabula - busca análise das tabelas na página pdf;
* Request - realizar requisições, no caso de paǵinas na internet;
* Shutil - mover arquivos no sistema;
* Re - busca textual através de expressões regulares;
* Csv - para carregar arquivos csv;
* Os - busca do caminho relativo dos arquivos no sistema operacional;

## Configurações do Projeto
* Utilização do ambiente virtual 'Virtualenv';

## Preparação dos arquivos
* Utilizado o programa do teste anterior 'browser' para download do arquivo 'pdf' que é utilizado neste programa.

## Estrutura do projeto
O programa é executado no arquivo 'main.js', que importa os diversos módulos presentes na pasta './src/utils/functions' e dentro de suas respectivas pastas (ex: o módulo que trata as tabelas com erros se encontra em './functions/folder_extrair_tabelas_pdf'). Na pasta './src/files/pdf' esta o arquivo 'pdf' utilizado para extração das tabelas e na pasta './src/files/csv' é salvo o arquivo 'zip' com os arquivos 'csv' que contém os dados das tabelas.
Utilizamos a estratégia da criação de módulo para as funções e importação de um módulo para outro.
A estrutura exemplificada do projeto é apresentado no Canva a partir do link: https://www.canva.com/design/DAE1DLdx6cM/_4uojZ0TkQmFuHkC62e_Sw/view?utm_content=DAE1DLdx6cM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## Documentação
Para a documentação geral do código nos baseamos na C4 model que utilizamos para fazer a apresentação no Canva (https://www.canva.com/design/DAE1DLdx6cM/_4uojZ0TkQmFuHkC62e_Sw/view?utm_content=DAE1DLdx6cM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton). A documentação do código, do processo de construção do algoritmo, das funções com seus problemas e soluções foi feita através do DocStrins e adicionado ao início de cada módulo e cada função.