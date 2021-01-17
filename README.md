# lab-monopoly

## pré requisitos
* Para subir o serviço é necessária a instalação do Docker e do Docker Compose na sua máquina, instaladores: https://docs.docker.com/engine/install/ e https://docs.docker.com/compose/install/.

* Para executar os arquivos da pasta notebooks é necessária a instalação do jupyter em seu ambiente: https://jupyter.org/install.

* Para executar os testes é necessário instalar a biblioteca pytest

## instalação
Não é necessária a instalação de pacotes python localmente, basta subir o ambiente de desenvolvimento que ele realizará a instalação em um container docker.

## como subir o serviço
Na pasta raiz do projeto, execute o comando abaixo:

```console
docker-compose up
```

## como acessar o serviço
O Serviço está disponível em uma API na porta 80. Caso deseje trocar a porta em seu computador, altere a primeira porta da opção "PORTS" do arquivo docker-compose.yml

Todas as rotas respondem HTTP POST em formato JSON.

Através do caminho /docs, é possível acessar a documentação interativa das rotas, gerada automaticamente:

![documentação swagger da aplicação](https://raw.githubusercontent.com/chris-redfield/lab-monopoly/main/images/docs.png)

​1. /monopoly​/new_game

* Inicializa um novo jogo

​2. /monopoly​/process_round

* Processa uma rodada do jogo atual

​3. /monopoly​/run_game

* Executa um novo jogo completo, ou executa o jogo atual até o final

​4. /monopoly​/run_games

* Executa n jogos, retorna estatísticas dos jogos

![demo da rota run_games](https://raw.githubusercontent.com/chris-redfield/lab-monopoly/main/images/stats.png)


## desenvolvimento
Mudanças entram em efeito após o reinicio do serviço (docker-compose up), não há necessidade de reconstrução do container, com exceção de casos onde novas funcionalidades / bibliotecas forem adicionadas.

## testes
Para executar os testes, navegue até a raiz do projeto e execute o comando abaixo para realizar os testes com os prints do serviço (para ver os jogos no log). 

```console
pytest -s
```

Caso não queira ver os prints basta remover o '-s'.