### Desafio do Agente James: Configuração do Servidor Nginx

Em um dia comum, o Agente Jame precisou que o mesmo nginx agora fosse deployado em um servidor, so que agora o requesito é que seja um container docker com uma página personalizada. 

### Notas

O nginx por padrao responde a porta 80

#### Etapa 1: Investigar portas de serviço e conexão com a internet

1. **Valide se a porta SSH está aberta**
2. **Entre no servidor**
3. **Instale os requesitos minimos para subir um container na máquina usando o Daemon do Docker**
4. **Valide a conexão com a internet do servidor**

Após corrigir o problema, o desenvolvedor solicitou uma nova página para substituir a atual.

#### Etapa 2: Criando uma nova imagem docker com uma pagina personalizada

1. **Use a pagina HTML em outro_repo.**
2. **Use como referência o Dockerfile explicado na aula para criar sua imagem personalizada com a pagina HTML que esta dentro de outro_repo(Sempre atendo aos diretorios)**
3. **Envie sua imagem para o registry publico**
4. **Inicie o container e faça Binding para a porta 3000 do servidor para que a pagina seja acessada na porta 3000**
5. **Mude para porta 80 e deixe o container rodando e background**
6. **Verifique dentro do container qual OS é baseado a imagem com o comando cat /etc/os-release**
7. **Execute dentro do container uma request para https://api.thecatapi.com/v1/images/search**
8. **Copie e abra no Browser a url retornada na chamada**

Boa sorte, Agente James!