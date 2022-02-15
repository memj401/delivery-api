# **Introdução**

Implementação de uma API REST simples, utilizando o framewok Flask, para gerenciamento dos pedidos realizados por um serviço de delivery. 
A API é responsável por realizar operações de criação,deleção,edição e busca de dados em uma base de dados localizada em um arquiso do tipo .JSON previamente disponibilizado.
A comunicação entre API e o cliente se dá por meio de requisições e respostas codificadas pelo tipo de dado JSON.
Uma descrição mais detalhada do projeto pode ser encontrada no [documento referente](TesteProgramacao_API.pdf).

# **Requisitos e Tecnologias Utilizadas** 
- [Flask](https://flask.palletsprojects.com/en/2.0.x/): Microframework em Python para desenvolvimento web utilizado para desenvolvimento da aplicação da API
- [Docker](https://www.docker.com): Plataforma utilizada na conteinerização da aplicação desenvolvida
- [Insomnia](https://insomnia.rest): Cliente API utilizado para  teste da API, por meio da realização de requisições e análise das respostas da aplicação desenvolvida

# **Estrutura da Aplicação**
 Para aplicação deste projeto, optou por modularizar o serviço em quatro arquivos distintos a fim possibilitar maior escalabilidade ao projeto, além de facilitar a implementação de mudanças no código. 
Encontra-se abaixo uma breve descrição da funcionalidade cada um dos arquivos presentes no projeto dentro da aplicação:

- [app.py](src/app.py):  Arquivo que apresenta as configurações de runtime da aplicação e configuração do servidor
- [rotas.py](src/rotas.py): Arquivo onde estão definidas todas as rotas para prestação de serviçoes da aplicação
- [controladoraPedidos.py](src/controladoraPedidos.py): Arquivo onde se encontranm as funcionalidades de verificação e validação dos parâmetros fornecidos pela requisição
- [repositorioPedidos.py](src/repositorioPedidos.py): Arquivo onde se encontram as funções de acesso e modificação da base de dados
- [docker-compose.yml](docker-compose.yml), [requirements.txt](requirements.txt) e [Dockerfile](Dockerfile): Arquivos utilizados para inicialização e configuração da imagem da aplicação utilizada prelo Docker.
 
# **Como Executar a Aplicação**
Após o download do repositório é necessário fornecer uma base de dados, com o nome de "pedidos.json", e colocá-la no repositório [src](src).
Vale ressaltar que a base de dados fornecida deve seguir o padrão definido pelo [exemplo](src/pedidos.json) fornecido.
Em seguida, com o Docker instalado, basta executar o seguinte comando no repositório em que os arquivos [docker-compose.yml](docker-compose.yml), [requirements.txt](requirements.txt) e [Dockerfile](Dockerfile) se encontram para dar início a execução da imagem:
```
docker-compose up -d 
```
Para terminar a execução da imagem, basta executar o seguinte comando:
```
docker-compose down
```
# **Sistema de Roteamento da Aplicação**
Como a implementação feita utliza um sistema baseado em rotas para criação dos Endpoints da API, é necessário explicitar como  o roteamento é feito, além da estrutura necessária para realização das requisições, a fim de garantir o seu funcionamento esperado. 
Uma definição da estrutura de rotas e requisições encontra-se no arquivo de [rotas](src/rotas.md).


# **Backlog de Tarefas Realizadas**
- [x] Executar uma Aplicação Simples de Teste em Flask
- [x] Escrever o Arquivo de Rotas e Definir Todas a Rotas Necessárias para Aplicação
- [x] Teste do Roteamebto da Aplicação 
- [x] Escrever o Arquivo de Repositório e Definir Todas as Operações Relacionadas a Base de Dados
- [x] Teste das Operações do Repositório
- [x] Escrever o Arquivo de Controladora e Validações da Requisição
- [x] Teste da Controladora
- [x] Teste Geral da Aplicação 
- [x] Escrever os Arquivos de Configuração do Docker
- [x] Testar Execução da Imagem 
- [x] Teste Geral da Aplicação 
- [x] Upload dos Arquivos Necessários para o Github
- [x] Escrever os arquivos [rotas.md](src/rotas.md) e README.md


 
 
 
 
