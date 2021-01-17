# lab-monopoly

### instalação
Não é necessária a instalação de pacotes localmente, basta subir o ambiente de desenvolvimento que ele realizará a instalação em um container docker.

### como subir o serviço
Na pasta raiz do projeto, execute o comando abaixo:

```console
docker-compose up
```

### como acessar o serviço
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
