import streamlit as st
import random
import time

st.set_page_config(layout="wide")

st.title("📊 AURAXIS - Forex Trading")

# Simulação de preço EUR/USD
if "price" not in st.session_state:
    st.session_state.price = 1.0800

def update_price():
    variation = random.uniform(-0.0005, 0.0005)
    st.session_state.price = round(st.session_state.price + variation, 5)

# Menu em abas
tab1, tab2, tab3 = st.tabs(["📈 Mercado", "📊 Histórico", "⚙️ Configurações"])

with tab1:
    st.subheader("Par de Moedas: EUR/USD")
    st.metric("Preço Atual", st.session_state.price)
    
    if st.button("Atualizar preço"):
        update_price()
        st.rerun()

with tab2:
    if "history" not in st.session_state:
        st.session_state.history = []

    st.session_state.history.append(st.session_state.price)
    st.line_chart(st.session_state.history)

with tab3:
    risk = st.slider("Risco por operação (%)", 1, 10, 2)
    st.write(f"Risco selecionado: {risk}%")
