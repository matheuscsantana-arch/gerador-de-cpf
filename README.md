# 🔢 Gerador de CPF 

Este é um projeto desenvolvido em Python com o objetivo de gerar números de CPF (Cadastro de Pessoas Físicas) válidos, seguindo o algoritmo oficial de cálculos de dígitos verificadores. O projeto foi criado para fins de estudo da lógica de programação e manipulação de strings e inteiros.

## 💻 Tecnologias

- Python 3.10+.
- Biblioteca `random`.

## ⚙️ Instalação

- Certifique-se de ter o Python instalado (versão 3.10 ou superior).
- Baixe o arquivo Gerador_CPF.py.
- Abra o terminal na pasta do arquivo e execute:

```bash
python Gerador_CPF.py
```

## 🛠️ Funcionalidades

O programa gera um CPF válido de 11 dígitos.
| Recurso | Descrição | Detalhes |
| :--- | :--- | :--- |
| **Geração Aleatória** | Gera os 9 primeiros dígitos de forma randômica. | Utiliza a biblioteca `random`. |
| **Cálculo de Dígitos** | Calcula matematicamente o 10º e 11º dígito. | Baseado em soma ponderada e resto da divisão por 11. |
| **Validação de Sequência** | Impede a geração de CPFs com todos os números iguais. | Verifica se o CPF gerado é uma repetição (ex: 111.111.111-11). |
| **Saída Formatada** | Exibe o resultado final em dois formatos diferentes. | Apresenta o CPF "limpo" (apenas números) e o "formal" (com pontos e traço). |

## 🕹️ Como usar

1. Execute o script Python.
2. O algoritmo irá gerar automaticamente os 9 dígitos iniciais.
3. O programa realiza o cálculo matemático para encontrar os dois dígitos verificadores.
4. O CPF gerado será exibido no terminal em dois formatos: apenas números e com pontuação oficial.
5. O programa se encerra automaticamente após gerar um CPF válido.

## 💡 Exemplo de uso

Ao rodar o programa, a saída no console seguirá este modelo:

![CPF gerado](assets/CPF-Gerado.PNG)

## 🚀 Status do Projeto

✅ Concluído

## 👤 Autor

Feito por **Matheus Felipe Claudino de Santana**  
GitHub: https://github.com/matheuscsantana-arch
