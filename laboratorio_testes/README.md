# 🧪 Laboratório de Testes: Validação do Gerador de Senhas

Este laboratório descreve os cenários de teste executados para garantir o funcionamento correto, a resiliência e os critérios de aceitação de segurança do gerador de senhas.

## 🚀 Como Executar os Testes no Google Colab

Para validar o script sem a necessidade de instalação local, siga os passos abaixo no ambiente de nuvem:

1. Acesse o [Google Colab](https://google.com).
2. Crie um **Novo Notebook**.
3. Copie o código do arquivo `main.py` deste repositório e cole em uma célula de código.
4. Execute a célula pressionando `Ctrl + Enter` ou clicando no botão **Play**.
5. Interaja com o terminal de entrada fornecendo os valores dos cenários abaixo.

---

## 📋 Cenários de Teste (Casos de Uso)

Para homologar a segurança do script, execute as seguintes entradas no prompt do programa:

### Cenário 1: Validação de Política de Segurança Mínima (Teste de Negativa)
* **Objetivo:** Garantir que o sistema barra a geração de senhas excessivamente curtas e vulneráveis.
* **Entrada esperada:** Digite o número `5` (ou qualquer valor menor que 8).
* **Resultado Esperado:** O programa deve exibir a mensagem: *"Erro: O tamanho mínimo permitido por segurança é 8 caracteres."* e encerrar sem exibir nenhuma senha.

### Cenário 2: Validação de Complexidade Obrigatória (Teste de Fronteira)
* **Objetivo:** Verificar se o algoritmo força a inclusão de todos os tipos de caracteres recomendados pelo NIST mesmo em tamanhos pequenos.
* **Entrada esperada:** Digite o número `8`.
* **Resultado Esperado:** O programa deve gerar uma senha curta de 8 dígitos. Inspecione visualmente se ela possui obrigatoriamente: 1 maiúscula, 1 minúscula, 1 número e 1 caractere especial.

### Cenário 3: Teste de Estresse e Alta Entropia (Cenário Padrão Corporativo)
* **Objetivo:** Validar o comportamento do script ao gerar chaves longas para uso em servidores ou ambientes de alta criticidade.
* **Entrada esperada:** Digite o número `32` ou `64`.
* **Resultado Esperado:** O sistema deve gerar instantaneamente uma string aleatória massiva, sem travamentos e com distribuição uniforme de caracteres.

---

## 🛡️ Verificação de Segurança Avançada (Conceitual)

Ao analisar a execução, certifique-se de que cada execução gera uma senha **completamente distinta da anterior**, mesmo utilizando exatamente o mesmo tamanho de entrada. Isso valida que o gerador baseado no módulo `secrets` (CSPRNG) está operando com um estado de entropia adequado fornecido pelo Kernel do sistema operacional, inviabilizando ataques de previsão de estado.
