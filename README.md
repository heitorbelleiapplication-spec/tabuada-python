<div align="center">

#  Tabuada em Python

Programa simples em **Python 3** que recebe um número inteiro e exibe sua tabuada de **1 a 10** no terminal.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)
![License](https://img.shields.io/badge/licen%C3%A7a-MIT-blue)

</div>

---

## 📌 Sobre o projeto

Este projeto apresenta um programa de **tabuada** desenvolvido em Python. O usuário informa um número inteiro — dentro do escopo da atividade, de **0 a 1000** — e o programa calcula e exibe as dez multiplicações desse número, de **1 até 10**.

O projeto foi criado para demonstrar conceitos fundamentais de programação, como:

- entrada de dados pelo terminal;
- armazenamento de valores em variáveis;
- estruturas de repetição com `for`;
- operações matemáticas;
- saída formatada de dados.

---

##  Como funciona

Ao iniciar o programa, ele aguarda que o usuário digite um número inteiro. Em seguida, utiliza um laço de repetição para percorrer os multiplicadores de `1` a `10` e mostra cada resultado no terminal.

O cálculo realizado em cada linha segue a lógica:

```text
número * multiplicador = resultado
```

---

##  Tecnologias e requisitos

- **Linguagem:** Python 3
- **Bibliotecas externas:** nenhuma
- **Sistema operacional:** Windows, macOS ou Linux
- **Terminal:** Prompt de Comando, PowerShell, Terminal ou terminal integrado de um editor

### Pré-requisito

É necessário ter o **Python 3** instalado no computador.

Para verificar a instalação, execute:

```bash
python --version
```

Em alguns sistemas, o comando pode ser:

```bash
python3 --version
```

---

##  Como executar

### 1. Obtenha o projeto

Baixe os arquivos do repositório ou clone-o com Git:

```bash
git clone https://github.com/SEU-USUARIO/tabuada-python.git
```

Depois, entre na pasta do projeto:

```bash
cd tabuada-python
```

> Substitua `SEU-USUARIO` pelo seu nome de usuário do GitHub.

### 2. Execute o programa

No Windows:

```bash
python main.py
```

No macOS ou Linux, se necessário:

```bash
python3 main.py
```

### 3. Informe um número

Digite um número inteiro de **0 a 1000** e pressione **Enter**. O programa exibirá a tabuada correspondente de 1 a 10.

---

##  Exemplo de uso

### Entrada

```text
2
```

### Saída

```text
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20
```

Assim, ao informar `2`, a tabuada começa em `2 * 1 = 2` e termina em `2 * 10 = 20`.

---

##  Estrutura do projeto

```text
tabuada-python/
├── README.md    # Apresentação e instruções do projeto
├── main.py      # Código-fonte do programa
├── LICENSE      # Licença MIT
└── .gitignore   # Arquivos que não devem ser versionados
```

---

##  Código principal

O funcionamento central do programa está no arquivo `main.py`:

```python
def main():
    numero = int(input())

    for multiplicador in range(1, 11):
        print(f"{numero} * {multiplicador} = {numero * multiplicador}")


if __name__ == "__main__":
    main()
```

O `range(1, 11)` gera os números de `1` a `10`. A cada repetição, o programa multiplica o número informado pelo multiplicador atual e mostra o resultado.

---

##  Resultado esperado

Para uma entrada válida, o programa imprime exatamente **10 linhas de resultado**, uma para cada multiplicador entre `1` e `10`.

Depois da décima multiplicação, o programa é encerrado normalmente. Para calcular outra tabuada, basta executá-lo novamente.

---

## 📄 Licença

Este projeto está disponibilizado sob a licença **MIT**. Consulte o arquivo [`LICENSE`](LICENSE) para mais informações.

---

<div align="center">

**Projeto concluído e pronto para execução.**

</div>
