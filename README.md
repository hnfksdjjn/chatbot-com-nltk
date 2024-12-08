# chatbot-com-nltk
Este projeto consiste em um chatbot financeiro que interage com o usuário, fornecendo respostas e dicas sobre como organizar finanças, investir, calcular saldo restante, entre outros temas relacionados. O sistema é construído usando o Tkinter para a interface gráfica, além de integrar funções de cálculo de saldo e um chatbot básico para responder a perguntas sobre finanças. A seguir, vou detalhar as três partes do código:

### Parte 1: Interface Gráfica com Tkinter

A primeira parte do projeto é a interface gráfica, construída usando a biblioteca `Tkinter`. Aqui, você tem a janela principal com um título, tamanho fixo e um fundo cinza. O layout inclui:

- **Título e ícone da janela**: A janela é configurada com um título "Chatbot Financeiro" e um ícone personalizado.
- **Imagem de fundo**: Uma imagem é adicionada na parte inferior da janela principal para personalizar a interface.
- **Menu de opções**: O menu é um `Combobox` que permite ao usuário selecionar uma das várias opções financeiras, como "Como organizar minhas finanças?", "Como criar uma reserva de emergência?", e outras relacionadas ao controle financeiro.
- **Área de resposta**: Uma área de texto é fornecida para mostrar as respostas do chatbot ou o resultado de cálculos financeiros.
- **Botões**: Dois botões são definidos:
  - **Obter Resposta**: Quando pressionado, o chatbot responde de acordo com a opção selecionada no menu.
  - **Limpar**: Limpa a área de resposta e redefine o menu de opções.
 
  - ![chat](https://github.com/user-attachments/assets/2c8230db-cbb1-4a65-8c8c-289d4d1f65c6)


A função `responder` é responsável por identificar a opção escolhida e fornecer a resposta correspondente. Se a opção for "calcular saldo restante", uma nova janela é aberta para o cálculo.

### Parte 2: Função `calcular_saldo`

A segunda parte contém a função `calcular_saldo`, responsável por calcular o saldo restante após o usuário informar seu salário ou capital inicial e as despesas. Esta função recebe dois parâmetros:

- **capital**: O valor inicial, que pode ser o salário ou o capital que o usuário possui.
- **gastos**: Uma lista de valores representando as despesas mensais do usuário.

A função calcula a soma total das despesas e subtrai esse total do capital informado, retornando o saldo restante e o total de gastos. O resultado é exibido na interface.

![calcu](https://github.com/user-attachments/assets/9093fab4-315a-44ae-9b96-d8550d7f1d6c)


### Parte 3: Chatbot de Dicas Financeiras

A terceira parte implementa um chatbot simples utilizando a biblioteca `nltk.chat.util` para interagir com o usuário. A funcionalidade é baseada em um conjunto de regras que correspondem a perguntas específicas sobre finanças e respondem com dicas e orientações. O chatbot usa uma lista de pares (patterns, respostas), onde cada padrão (pergunta) é associado a uma resposta predefinida.

- **Padrões de perguntas e respostas**: Os padrões são baseados em expressões regulares, permitindo que o chatbot reconheça perguntas como "Como organizar minhas finanças?" e forneça uma resposta detalhada.
- **Função `obter_resposta`**: Esta função usa o módulo `Chat` do `nltk` para fazer a correspondência entre a entrada do usuário e os padrões definidos. Quando o usuário faz uma pergunta, o chatbot responde de acordo com a correspondência encontrada.

- ![dicas](https://github.com/user-attachments/assets/f5bc1cac-8988-45c4-a7f7-cae21539ef1b)


### Fluxo de Funcionamento

1. **Escolha de uma opção**: O usuário seleciona uma pergunta a partir do menu.
2. **Obtenção da resposta**: Se a pergunta for relacionada a finanças gerais, o chatbot utiliza a função `obter_resposta` para fornecer a resposta.
3. **Cálculo de saldo restante**: Se a opção for "calcular saldo restante", uma nova janela é aberta para que o usuário insira seu capital e despesas, e o saldo restante é calculado.
4. **Limpeza da interface**: O usuário pode limpar as respostas na área de texto a qualquer momento.

Este projeto pode ser expandido com mais funcionalidades, como integrações com APIs de finanças ou cálculos mais complexos.
