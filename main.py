# titulo
# input do chat
# a cada mensagem enviada:
    # mostrar a mensagem que o usuario enviou no chat
    # enviar essa mensagem para a IA responder
    # aparece na tela a resposta da IA

# streamlit - frontend e backend - apenas com Python
# pip install streamlit openai

import streamlit as     st
from   openai    import OpenAI # biblioteca para acessar a API da OpenAI - "com maiusculo" é uma funcionalidade especifica da biblioteca

modelo = OpenAI(api_key="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")
# A api_key é uma chame especifica de cada um que programa. Precisa entrar com seu usuário e criar a chave.

st.write("# Como posso te ajudar?") # markdown=Formatação de texto -> O "#" deixa como título em negrito e grande "##" dois deixa menor, "###" três menor ainda

# session_state = memoria do streamlit
if not "lista_mensagens" in st.session_state: 
    st.session_state["lista_mensagens"] = [] # Se a lista não existir, cria uma lista vazia

# adicionar uma mensagem
# st.session_state["lista_mensagens"].append(mensagem)

# role    = quem enviou a mensagem = "função"
# content = texto da mensagem      = "conteudo"

# exibir o histórico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    role    = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui...") # input da mensagem

if mensagem_usuario:
    # user      -> ser humano
    # assistant -> inteligencia artificial
    # content   -> conteudo da mensagem
    st.chat_message("user").write(mensagem_usuario) # mostra a mensagem do usuario na tela -> "user" mostra um ícone do usuario 
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)

    # resposta da IA
    resposta_modelo = modelo.chat.completions.create( # Precisa passar a lista de mensagem e o modelo da IA.
        messages=st.session_state["lista_mensagens"],
        model   ="gpt-4o"
    )
    
    resposta_ia = resposta_modelo.choices[0].message.content # Primeiro item da mensagem (0) -> content (texto da mensagem)

    # exibir a resposta da IA na tela
    st.chat_message("assistant").write(resposta_ia) #"assistant" mostra um ícone de robo (ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)


