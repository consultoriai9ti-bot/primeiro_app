import streamlit as st

def main():
    # Configuração da página
    st.set_page_config(page_title="Calculadora Smart", page_icon="⚡", layout="centered")

    # Estilo personalizado para centralizar o título
    st.markdown("""
        <style>
        .main-header {
            text-align: center;
            margin-bottom: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # Cabeçalho principal
    st.markdown("<h1 class='main-header'>⚡ Calculadora Smart</h1>", unsafe_allow_html=True)

    # Container Principal (Card de Controle)
    with st.container(border=True):
        st.subheader("Entrada de Dados")
        
        # Linha para as entradas numéricas
        col_num1, col_num2 = st.columns(2)
        with col_num1:
            num1 = st.number_input("1º Número", value=0.0, step=1.0, format="%.2f")
        with col_num2:
            num2 = st.number_input("2º Número", value=0.0, step=1.0, format="%.2f")

        # Seleção da Operação com Ícones
        operacao = st.radio(
            "Selecione a Operação:",
            ["➕ Soma", "➖ Subtração", "✖️ Multiplicação", "➗ Divisão"],
            horizontal=True
        )

        st.write("")  # Espaçamento
        
        # Botão de Ação Acentuado
        btn_calcular = st.button("🚀 Calcular Agora", use_container_width=True, type="primary")

    # Área de Exibição do Resultado
    if btn_calcular:
        st.write("")
        with st.container(border=True):
            st.subheader("Resultado")
            
            if operacao == "➕ Soma":
                res = num1 + num2
                st.success(f"### **{num1:.2f} + {num2:.2f} = {res:.2f}**")
                st.balloons()

            elif operacao == "➖ Subtração":
                res = num1 - num2
                st.success(f"### **{num1:.2f} - {num2:.2f} = {res:.2f}**")
                st.balloons()

            elif operacao == "✖️ Multiplicação":
                res = num1 * num2
                st.success(f"### **{num1:.2f} × {num2:.2f} = {res:.2f}**")
                st.balloons()

            elif operacao == "➗ Divisão":
                if num2 == 0:
                    st.error("⚠️ **Divisão impossível:** O segundo número não pode ser zero.")
                else:
                    res = num1 / num2
                    st.success(f"### **{num1:.2f} ÷ {num2:.2f} = {res:.2f}**")
                    st.balloons()

if __name__ == "__main__":
    main()
    Feito
