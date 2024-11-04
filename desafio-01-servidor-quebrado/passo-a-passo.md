### Desafio do Agente James: Configuração do Servidor Nginx

Em um dia comum, o Agente James se deparou com um problema urgente: o site da empresa apresentava um erro 403 ao ser acessado. Sabendo que precisava resolver rapidamente, ele se conectou ao servidor Nginx para investigar.

### Notas

O servidor pode ser acessado no ip da maquina na porta 80
O arquivo index.html fica em /var/www/html dentro do servidor 

#### Etapa 1: Solução do Erro 403

1. **Acesse o servidor via SSH.**
2. **Verifique o status do Nginx.**
3. **Localize o arquivo de configuração do Nginx.**
4. **Identifique o diretório onde o arquivo `index.html` está armazenado.**
5. **Verifique as permissões do diretório e do arquivo `index.html`.**
6. **Ajuste as permissões, se necessário.**
7. **Reinicie o Nginx.**
8. **Teste o acesso ao site pelo IP do servidor.**

Após corrigir o problema, o desenvolvedor solicitou uma nova página para substituir a atual.

#### Etapa 2: Troca da Página no Servidor

1. **Use a pagina HTML em etapa02.**
2. **Crie uma Pull Request (PR) para a nova página.**
3. **Substitua manualmente o arquivo `index.html` no servidor.**
4. **Reinicie o Nginx, se necessário.**
5. **Teste a nova página pelo IP do servidor.**

Boa sorte, Agente James!