### Desafio: **Começando com Docker**

**Objetivo:** Contunar Familiarizar-se com os comandos básicos do Docker e entender como trabalhar com containers e imagens .

Notas: 
 Nginx por padrao executa na porta 80, manteremos isso como padrão nos laboratórios.
 O backend fast desenvolvido escuta sempre na porta 8000, permanecer a porta dos servidores como 8000.

#### Passo 1: Crie um registry docker

Crie uma conta no Docker Hub

#### Passo 2: Faça o Docker Login no Docker HUB

Para permitir que sua máquina consuma do registry, execute o comando abaixo e siga o passo a passo da retornado pela console:
 
```bash
docker login
```

#### Passo 3: Buildar imagem Backend

Navegue ate a pasta backend da aula-04 e ajustes os erros presentes no Dockerfile:

Depois de corriji construa a imagem com o nome <seu-registry>/psytrance-festival-backend e com a tag 1.0.0

```bash
docker build . -<?>  <seu-registry>/psytrance-festival-backend:<sua_tag>
```

rode localmente com o docker run e teste a rota /artists na maquina local.

#### Passo 4: Buildar imagem Frontend

Navegue ate a pasta backend da aula-04 e ajustes os erros presentes no Dockerfile:

Depois de corriji construa a imagem com o nome <seu-registry>/psytrance-festival-frontend e com a tag 1.0.0

```bash
docker build . -<?>  <seu-registry>/psytrance-festival-frontend:<sua_tag>
```

Abra mais um terminal e rode também o frontend com o docker run e teste se a pagina mostra os artistas.

#### Passo 5: Enviando para o Docker hub

Para enviar para o registry basta executar 

```bash
docker push <seu-registry>/psytrance-festival-frontend:<sua_tag>
```

faça o mesmo para o backend

```bash
docker push <seu-registry>/psytrance-festival-backend:<sua_tag>
```

para consultar o nome da imagem e a tag rodar:
```bash
docker images
```

#### Passo 5: Rodando imagem no servidor remoto:

Se conecte ao seu servidor aluno via ssh.

Carregue as imagens publicadas anteriomente na máquina

```bash
docker pull <seu-registry>/psytrance-festival-frontend:<sua_tag> 
```

```bash
docker pull <seu-registry>/psytrance-festival-backend:<sua_tag> 
```

#### Passo 6: Execute em segundo plano os containers no servidor

Para executar no servidor e liberar sua console, é necessário rodar a imagem em segundo plano com o comando -d :

```bash
docker run -d -<?> <porta-do-host>:<porta-do-container> <seu-registry>/psytrance-festival-frontend:<sua_tag>
```

```bash
docker run -d -<?> <porta-do-host>:<porta-do-container> <seu-registry>/psytrance-festival-backend:<sua_tag>
```

#### Passo 7: Construindo versão 1.0.2 do backend.


Retorne a máquina Local e copie o conteúdo que está em arquivos na aula 4 e subistitua o código do backend :


repita todo o processo de buildar a imagem com o código atualizado, porém dessa vez, a tag deve ser 1.0.2.

```bash
docker push <seu-registry>/psytrance-festival-backend:1.0.2
```

Pare o container do backend atual e note que o frontend ja parou de retornar os dados da api.(Necessário recarregar a página)
Execute o container do backend na versão 1.0.2 com o docker run e veja a atualização.