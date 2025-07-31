from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)


import streamlit as st

st.title("2種類の専門家への相談アプリケーション")

st.write("##### 動作モード1: マーケティングに関する相談")
st.write("マーケティングに関する相談事項を入力することで、専門家が回答をしてくれます。")
st.write("##### 動作モード2: 採用に関する相談")
st.write("採用に関する相談事項を入力することで、専門家が回答をしてくれます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["マーケティングに関する相談", "採用に関する相談"]
)

st.divider()

if selected_item == "マーケティングに関する相談":
    input_message = st.text_input(label="マーケティングに関する相談事項を入力してください。")

else:
    input_message = st.text_input(label="採用に関する相談事項を入力してください。")

if st.button("実行"):
    st.divider()

    if selected_item == "マーケティングに関する相談":

        if input_message:
            messages = [
            SystemMessage(content="あなたは、マーケティングに関する専門家です。相談に答えてください。"),
            HumanMessage(content=input_message),
            ]
            result = llm(messages)
            st.write(result.content)

        else:
            st.error("相談事項を入力してから「実行」ボタンを押してください。")

    else:
        if  input_message:
            messages = [
            SystemMessage(content="あなたは、採用に関する専門家です。相談に答えてください。"),
            HumanMessage(content=input_message),
            ]
            result = llm(messages)
            st.write(result.content)

        else:
            st.error("相談事項を入力してから「実行」ボタンを押してください。")
