# 🛡️ Gerador de Senhas Criptograficamente Seguro (Python)

Este é um projeto desenvolvido como parte dos meus estudos no 2º ano de **Segurança da Informação**. O objetivo foi criar uma ferramenta capaz de gerar senhas de alta entropia, seguindo as melhores práticas de cibersegurança.

## 🚀 Diferencial Técnico (Foco em Segurança)

A maioria dos geradores de senha básicos utiliza a biblioteca padrão `random` do Python. No entanto, em Segurança da Informação, o módulo `random` **não deve ser utilizado** para fins de segurança ou criptografia, pois ele gera números pseudoaleatórios que podem ser previstos por um atacante.

Neste projeto, apliquei:
*   **Módulo `secrets`:** Utilizado para gerar números aleatórios criptograficamente seguros (CSPRNG), ideais para gerenciar segredos como senhas, tokens de segurança e chaves de autenticação.
*   **Complexidade Obrigatória:** O algoritmo garante que, independentemente do tamanho escolhido, a senha gerada conterá obrigatoriamente pelo menos:
    *   1 caractere maiúsculo
    *   1 caractere minúsculo
    *   1 dígito numérico
    *   1 caractere especial

## 🛠️ Tecnologias Utilizadas

*   **Python 3.x**
*   Biblioteca `secrets` (Nativa)
*   Biblioteca `string` (Nativa)

## 🔧 Como Executar o Projeto

1. Certifique-se de ter o Python instalado na sua máquina.
2. Execute o comando:
   ```bash
   python main.py
   ```

## 📝 Próximos Passos (Roadmap de Evolução)
* [ ] Criar uma Interface Gráfica (GUI) simples para o usuário.
* [ ] Adicionar uma métrica para exibir o nível de entropia da senha gerada.
* [ ] Implementar a opção de salvar as senhas de forma criptografada localmente.
      
      Atenciosamente;
