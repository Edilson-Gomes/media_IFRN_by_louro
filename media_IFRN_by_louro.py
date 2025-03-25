import streamlit as st 

st.title("Média do IFRN")

nota1 = st.number_input("Nota da primeira etapa(40%): ")
nota2 = st.number_input("Nota da segunda etapa(60%): ")
media = (2*nota1 + 3*nota2) / 5

res = st.button("Resultado")

if res:
    st.write(f"<h3 style='color:limegreen'>{media:.0f}</h3>", unsafe_allow_html=True)
    if media >= 60.0:
        st.write("<h2 style='color:yellow'>Aprovado!</h2>", unsafe_allow_html=True)
        st.balloons()
    else:
        st.warning("RECUPERAÇÃO! Estude para prova final.")
        