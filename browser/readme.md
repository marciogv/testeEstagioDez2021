# Teste 1 Estágio - WebScraping

## Tarefas de código:

* Queries de load: criar as queries para carregar o conteúdo dos arquivos obtidos nas tarefas de preparação num banco MySQL ou Postgres (Atenção ao encoding dos arquivos!)
* Montar uma query analítica que traga a resposta para as seguintes perguntas:
  1. Acessar o site: https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss;
  2. Buscar a versão mais recente do Padrão TISS (arquivo - padrao_tiss_componente_organizacional_201902.pdf);
  3. Baixar o componente organizacional;

## Linguagem de programação utilizada
Python

## Pacotes/bibliotecas utilizadas
* Selenium - para criar o WebDriver do Chrome e realizar as tarefas de automação de navegação;
* Request - realizar requisições, no caso de paǵinas na internet;
* Shutil - mover e copiar arquivos no sistema;
* Time - permite a contagem de tempo do sistema;
* Os - busca do caminho relativo dos arquivos no sistema operacional;

## Configurações do Projeto
* Instalação do programa Docker e Docker Compose para subir base de dados MySQL no sistema;
* Utilização do ambiente virtual 'Virtualenv';
* Download do 'chromedriver' da página 'https://chromedriver.chromium.org/downloads'
* Instalação dos seguintes pacotes/bibliotecas no ambiente virtual do Python:
  * Selenium;


## Estrutura do projeto
O programa é executado no arquivo 'main.js', que importa os diversos módulos presentes na pasta './src/utils/functions'. O arquivo 'pdf' baixado pelo programa é inserido na pasta './files/pdf'. O mesmo arquivo é copiado para a pasta do projeto 'transform_data' cujo caminho é 'transform_data/src/files/pdf.
Utilizamos a estratégia da criação de módulo para as funções e importação de um módulo para outro.
A estrutura exemplificada do projeto é apresentado no Canva a partir do link: https://www.canva.com/design/DAE1DLdx6cM/_4uojZ0TkQmFuHkC62e_Sw/view?utm_content=DAE1DLdx6cM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## Documentação
Para a documentação geral do código nos baseamos na C4 model que utilizamos para fazer a apresentação no Canva (https://www.canva.com/design/DAE1DLdx6cM/_4uojZ0TkQmFuHkC62e_Sw/view?utm_content=DAE1DLdx6cM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton). A documentação do código, do processo de construção do algoritmo, das funções com seus problemas e soluções foi feita através do DocStrins e adicionado ao início de cada módulo e cada função.