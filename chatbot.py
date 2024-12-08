from nltk.chat.util import Chat, reflections

# Lista de dicas financeiras extraídas e organizadas
pairs = [
    (r"como organizar minhas finanças?", [
        "1. Liste todas as receitas e despesas.\n"
        "2. Divida os gastos em fixos e variáveis.\n"
        "3. Defina um orçamento mensal para controlar o saldo."
    ]),
    (r"como criar uma reserva de emergência?", [
        "1. Poupe regularmente uma parte do salário.\n"
        "2. Mantenha o dinheiro em investimentos seguros e líquidos, como Tesouro Selic ou poupança.\n"
        "3. Objetivo: Acumular de 3 a 6 meses de despesas fixas."
    ]),
    (r"quais são as melhores práticas para investir?", [
        "1. Defina seus objetivos financeiros.\n"
        "2. Conheça seu perfil de investidor: conservador, moderado ou arrojado.\n"
        "3. Diversifique seus investimentos para reduzir riscos."
    ]),
    (r"como reduzir meus gastos?", [
        "1. Identifique despesas desnecessárias e corte-as.\n"
        "2. Utilize cupons e promoções.\n"
        "3. Compare preços antes de comprar qualquer coisa."
    ]),
    (r"como negociar dívidas?", [
        "1. Entre em contato com credores para renegociar condições.\n"
        "2. Priorize o pagamento de dívidas com juros mais altos.\n"
        "3. Considere a consolidação de dívidas, se for vantajoso."
    ]),
    (r"como começar a investir?", [
        "Para começar a investir:\n"
        "1. Defina seus objetivos financeiros (curto, médio ou longo prazo).\n"
        "2. Conheça seu perfil de investidor (conservador, moderado ou arrojado).\n"
        "3. Estude os diferentes tipos de investimentos, como renda fixa, ações ou fundos imobiliários.\n"
        "4. Comece com investimentos simples, como Tesouro Direto ou fundos de índice.\n"
        "5. Diversifique sua carteira para reduzir riscos."
    ]),
    (r"como organizar minhas finanças pessoais?", [
        "Aqui estão algumas dicas para organizar suas finanças pessoais:\n"
        "1. Liste todas as suas receitas e despesas.\n"
        "2. Crie um orçamento mensal e respeite-o.\n"
        "3. Identifique e elimine gastos desnecessários.\n"
        "4. Reserve uma parte de sua renda para poupança ou investimentos.\n"
        "5. Construa uma reserva de emergência equivalente a 3-6 meses de despesas."
    ]),
    (r"quais são os melhores investimentos para iniciantes?", [
        "Os melhores investimentos para iniciantes incluem:\n"
        "1. Tesouro Direto: Seguro e de baixo custo.\n"
        "2. Fundos de índice (ETFs): Fácil diversificação.\n"
        "3. CDBs ou LCIs/LCAs: Oferecem boa rentabilidade com segurança.\n"
        "4. Fundos de investimento com baixa taxa de administração.\n"
        "5. Poupança (apenas como reserva de curto prazo)."
    ]),
    (r"como reduzir dívidas?", [
        "Para reduzir suas dívidas:\n"
        "1. Liste todas as suas dívidas, incluindo valores e taxas de juros.\n"
        "2. Priorize o pagamento de dívidas com juros mais altos.\n"
        "3. Negocie condições melhores com seus credores.\n"
        "4. Evite fazer novas dívidas enquanto não resolver as antigas.\n"
        "5. Crie um plano de pagamento e seja disciplinado."
    ]),
    (r"como montar um orçamento?", [
        "Para montar um orçamento eficaz:\n"
        "1. Liste todas as suas receitas mensais.\n"
        "2. Registre suas despesas fixas (como aluguel e contas).\n"
        "3. Identifique despesas variáveis e ajuste onde for possível.\n"
        "4. Reserve uma parte da sua renda para poupança ou investimentos.\n"
        "5. Monitore e revise seu orçamento regularmente."
    ]),
    (r"como funciona o Tesouro Direto?", [
        "O Tesouro Direto é uma plataforma para investir em títulos públicos emitidos pelo governo. Funciona assim:\n"
        "1. Você empresta dinheiro ao governo e recebe juros em troca.\n"
        "2. Existem títulos pré-fixados (juros fixos) e pós-fixados (ligados à inflação ou Selic).\n"
        "3. É um investimento seguro e ideal para iniciantes.\n"
        "4. Você pode começar com valores baixos e acompanhar seus rendimentos online."
    ]),
    (r"quais são as vantagens de diversificar investimentos?", [
        "Diversificar investimentos traz benefícios como:\n"
        "1. Redução do risco: Se um investimento não performar bem, outros podem compensar.\n"
        "2. Aproveitamento de diferentes oportunidades no mercado.\n"
        "3. Melhor estabilidade para sua carteira financeira.\n"
        "4. Maior proteção contra crises em setores específicos."
    ]),
    (r"quais são os erros comuns ao investir?", [
        "Os erros comuns ao investir incluem:\n"
        "1. Não definir objetivos claros antes de investir.\n"
        "2. Colocar todo o dinheiro em um único ativo.\n"
        "3. Investir sem entender os riscos envolvidos.\n"
        "4. Reagir emocionalmente às oscilações do mercado.\n"
        "5. Negligenciar taxas e custos dos investimentos."
    ]),
    (r"sair", [
        "Obrigado por usar o chatbot. Até logo!"
    ]),
    (r"(.*)", [
        "Desculpe, não entendi sua pergunta. Tente reformular ou seja mais específico."
    ])
]

# Função para o chatbot com interação dinâmica
def obter_resposta(entrada):
    chatbot = Chat(pairs, reflections)
    return chatbot.respond(entrada)

