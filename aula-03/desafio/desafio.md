### Desafio: **Começando com Docker**

**Objetivo:** Familiarizar-se com os comandos básicos do Docker e entender como trabalhar com containers e imagens .

#### Passo 1: Baixar uma Imagem

Vamos começar com uma imagem popular para testar. Execute o comando abaixo para baixar a imagem do **Ubuntu**:

```bash
docker pull nginx
```

Aguarde até que o Docker baixe a imagem. Após a conclusão, use o comando `docker images` para verificar a imagem baixada.

#### Passo 2: Criar um Container Interativo

Agora que temos uma imagem, vamos criar um container interativo usando a imagem do nginx. Execute o comando abaixo:

```bash
docker run  -p 80 nginx
```

Esse comando inicia um container com o nginx.

Agora que temos uma imagem, vamos criar um container, vamos expor o servico no servidor na porta 8000.
```bash
docker run -<?> <?>:80 nginx
```

Teste o servidor e garanta que a porta responde corretamente

#### Passo 3: Verificar Containers em Execução

Para listar todos os containers em execução, execute:

```bash
docker ps
```

Se você deseja ver todos os containers, incluindo os que estão parados, use:

```bash
docker ps -a
```

#### Passo 4: Parar um Container

Para parar o container interativo que você iniciou, use o comando abaixo:

```bash
docker stop <ID_do_container>
```

Substitua `<ID_do_container>` pelo ID do seu container, que pode ser obtido usando o comando `docker ps -a`.

#### Passo 5: Remover um Container

Agora, vamos remover o container. Use o comando abaixo:

```bash
docker rm <ID_do_container>
```

#### Passo 6: Remover uma Imagem

Você não precisa mais da imagem do nginx, pode removê-la com o comando:

```bash
docker rmi ubuntu
```
#### Passo 7: Construindo a Imagem de API psy
### Execute esses passos na maquina local.


Crie uma nova imagem com o Dockerfile dentro da pasta backend:

```bash
docker build . -<?> <nome-da-imagem>
```

Liste e garanta que a imagem existe.

#### Passo 8: Crie uma nova versão da imagem
### Execute esses passos na maquina local.


Dentro de app.py mude para a versao 1.0.1 e depois adicione na lista mais um artista da sua preferência.

Construa a imagem
```bash
docker build . -<?> <nome-da-imagem>:1.0.1
```

Liste e garanta que a imagem existe.

#### Passo 9: Execute o container criado por você
### Execute esses passos na maquina local.

Rodando Container
```bash
docker run  -<?> <?>:80 <nome-da-imagem>:<tag-da-imagem>
```
Teste e garanta que a imagem exite