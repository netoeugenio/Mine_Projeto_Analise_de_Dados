import streamlit as st
from PIL import Image

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Portfólio • Eugenio Paiva", layout="wide")

# ---------------- HEADER ----------------
st.title("📊 Portfólio Profissional — Eugenio Paiva")
st.markdown("Analista de Dados • Python • Dashboards • Estatística • EDA")

# ---------------- SOBRE MIM ----------------
st.header("👨‍💼 Sobre Mim")
st.write(
    """
Sou estudante e praticante dedicado na área de **Análise de Dados**, com experiência em
Python, Pandas, NumPy e Técnicas de Estatística Aplicada.

Tenho foco em transformar dados em **insights úteis**, criar visualizações claras,
trabalhar com datasets reais e fictícios e desenvolver soluções que apoiem decisões
estratégicas das empresas.
    """
)

# ---------------- HABILIDADES ----------------
st.header("🛠️ Habilidades")
cols = st.columns(3)
skills = [
    "Python", "Pandas", "NumPy", "Matplotlib / Seaborn", "Estatística Aplicada",
    "Análise Exploratória de Dados (EDA)", "Limpeza e Tratamento de Dados",
    "Criação de Datasets Sintéticos", "Git e GitHub"
]

for idx, skill in enumerate(skills):
    cols[idx % 3].markdown(f"✔️ **{skill}**")

# ---------------- PROJETOS ----------------
st.header("💼 Projetos")

st.subheader("📌 Projeto 1 — Geração de Dados de Vendas Fictícias & Limpeza")
st.write(
    """
Projeto focado na criação de um dataset sintético simulando vendas de um e-commerce.
Inclui geração de dados realistas (ID, datas, produtos, valores) e introdução
de erros como valores faltantes, duplicados e outliers para treinar habilidades
avançadas de **limpeza e preparação de dados**.

**Tecnologias:** Python, Pandas, NumPy  
**Habilidades:** geração de dados, padronização, detecção de outliers.
    """
)
st.link_button("🔗 Ver no GitHub", "https://github.com/netoeugenio/Mine_Projeto_Analise_de_Dados")

st.markdown("---")

st.subheader("📌 Projeto 2 — Análise Estatística de Dados de E-commerce")
st.write(
    """
Projeto que simula o comportamento de usuários em um e-commerce, incluindo visitas,
tempo no site, itens adicionados ao carrinho e valor gasto. Aplicação de técnicas
estatísticas e visualizações para identificar padrões e correlações.

**Tecnologias:** Python, Pandas, NumPy, Matplotlib/Seaborn  
**Habilidades:** estatística aplicada, segmentação, correlação, visualização.
    """
)
st.link_button("🔗 Ver no GitHub", "https://github.com/netoeugenio/Mine_Projeto_Analise_de_Dados")

# ---------------- CONTATO ----------------
st.header("📞 Contato")
st.write("**E-mail:** eugeniopaiva67@gmail.com")
st.write("**LinkedIn:** www.linkedin.com/in/eugenio-paiva-0786b7267")
st.write("**GitHub:** https://github.com/netoeugenio/Mine_Projeto_Analise_de_Dados")

st.success("Portfólio carregado com sucesso!")
