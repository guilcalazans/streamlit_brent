import streamlit as st
import yfinance as yf

st.set_page_config(
    page_title = 'TC 4',
    layout = 'wide'
)

st.header("**Painel de Preço de Fechamento de ações do Brent**")

# ticker = st.text_input('Digite o ticker da ação','BBAS3')
ticker = 'BZ=F'
# empresa = yf.Ticker(f"{ticker}.SA") 
empresa = yf.Ticker(f"{ticker}") 

tickerDF = empresa.history(period = "1d",
                           start = "2019-01-01",
                           end ="2025-01-20")
col1, col2 = st.columns([1,1])

with col1:
    st.write(f"**Empresa:** {empresa.info['shortName']}")

with col2:
    st.write(f"**Preço Atual: $** {empresa.info['previousClose']}")

st.line_chart(tickerDF.Close)
