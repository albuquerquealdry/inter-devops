**Desafio: Gerador de Senhas Fortes**  
Neste desafio, você criará um programa que gera senhas fortes e aleatórias com base nos critérios definidos pelo usuário.

---

### **Regras do Desafio**
1. O programa deve perguntar ao usuário:
   - O comprimento da senha (mínimo 6 caracteres).
   - Se a senha deve incluir letras maiúsculas.
   - Se a senha deve incluir números.
   - Se a senha deve incluir caracteres especiais (ex: `!@#$%^&*`).
2. O programa deve validar o comprimento mínimo.
3. A senha gerada deve ser completamente aleatória, respeitando os critérios selecionados.
4. O programa deve exibir a senha gerada.

---

### **Exemplo de execução**
```plaintext
Bem-vindo ao Gerador de Senhas Fortes!
Quantos caracteres a senha deve ter? 12
A senha deve incluir letras maiúsculas? (s/n): s
A senha deve incluir números? (s/n): s
A senha deve incluir caracteres especiais? (s/n): s

Senha gerada: @k9ZbP2#xAq7
```

---

### **Guia do Código Fonte**

#### **1. Importar Módulos Necessários**
Vamos usar o módulo `random` para criar uma senha aleatória.

```python
import random
import string
```

#### **2. Função para Criar a Senha**
Essa função gera a senha com base nos critérios fornecidos pelo usuário.

```python
def gerar_senha(comprimento, incluir_maiusculas, incluir_numeros, incluir_especiais):
    caracteres = string.ascii_lowercase  # Inclui letras minúsculas por padrão

    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiais:
        caracteres += "!@#$%^&*()-_=+"

    # Gera uma senha aleatória com os caracteres disponíveis
    senha = "".join(random.choice(caracteres) for _ in range(comprimento))
    return senha
```

#### **3. Função Principal**
Aqui está a lógica para capturar as entradas do usuário e gerar a senha.

```python
def main():
    print("Bem-vindo ao Gerador de Senhas Fortes!")

    # Solicitar o comprimento da senha
    while True:
        try:
            comprimento = int(input("Quantos caracteres a senha deve ter? (mínimo 6): "))
            if comprimento < 6:
                print("A senha deve ter pelo menos 6 caracteres.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido.")

    # Solicitar os critérios
    incluir_maiusculas = input("A senha deve incluir letras maiúsculas? (s/n): ").strip().lower() == "s"
    incluir_numeros = input("A senha deve incluir números? (s/n): ").strip().lower() == "s"
    incluir_especiais = input("A senha deve incluir caracteres especiais? (s/n): ").strip().lower() == "s"

    # Gerar a senha
    senha = gerar_senha(comprimento, incluir_maiusculas, incluir_numeros, incluir_especiais)

    # Exibir a senha gerada
    print("\nSenha gerada:", senha)
```

#### **4. Executar o Programa**
Finalmente, conectamos tudo para rodar o programa.

```python
if __name__ == "__main__":
    main()
```

---

### **Código Completo**
```python
import random
import string

def gerar_senha(comprimento, incluir_maiusculas, incluir_numeros, incluir_especiais):
    caracteres = string.ascii_lowercase  # Inclui letras minúsculas por padrão

    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_especiais:
        caracteres += "!@#$%^&*()-_=+"

    # Gera uma senha aleatória com os caracteres disponíveis
    senha = "".join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def main():
    print("Bem-vindo ao Gerador de Senhas Fortes!")

    # Solicitar o comprimento da senha
    while True:
        try:
            comprimento = int(input("Quantos caracteres a senha deve ter? (mínimo 6): "))
            if comprimento < 6:
                print("A senha deve ter pelo menos 6 caracteres.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido.")

    # Solicitar os critérios
    incluir_maiusculas = input("A senha deve incluir letras maiúsculas? (s/n): ").strip().lower() == "s"
    incluir_numeros = input("A senha deve incluir números? (s/n): ").strip().lower() == "s"
    incluir_especiais = input("A senha deve incluir caracteres especiais? (s/n): ").strip().lower() == "s"

    # Gerar a senha
    senha = gerar_senha(comprimento, incluir_maiusculas, incluir_numeros, incluir_especiais)

    # Exibir a senha gerada
    print("\nSenha gerada:", senha)

if __name__ == "__main__":
    main()
```

---