# src/dashboard_main.py
import os
import sys

# 1. Garante que o Python encontre as pastas irmãs (utils, components, load)
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

import streamlit as st
import pandas as pd
from utils.db import get_engine
from load.queries import DASHBOARD_QUERY
from components.charts import plot_engagement_bar, plot_stars_vs_size

# --- CONFIGURAÇÃO ---
st.set_page_config(page_title="GitHub Java Trends", page_icon="📊", layout="wide")

@st.cache_data(ttl=600)
def fetch_data():
    engine = get_engine()
    df = pd.read_sql(DASHBOARD_QUERY, engine)
    df['size_mb'] = df['size_kb'] / 1024.0
    return df

# --- CARGA E FILTROS ---
try:
    df = fetch_data()
except Exception as e:
    st.error(f"Erro de conexão com o banco. O Docker está rodando? Detalhe: {e}")
    st.stop()

st.sidebar.header("🎯 Filtros")
min_stars = st.sidebar.slider("Mínimo de Estrelas", int(df['stargazers_count'].min()), int(df['stargazers_count'].max()), 5000)
df_filtered = df[df['stargazers_count'] >= min_stars]

# --- INTERFACE ---
st.title("📊 GitHub Java Trends - Dashboard")

# Métricas
c1, c2, c3, c4 = st.columns(4)
c1.metric("Estrelas", f"{df_filtered['stargazers_count'].sum():,}")
c2.metric("Engajamento Médio", f"{df_filtered['engagement_rate'].mean():.2f}%")
c3.metric("Taxa de Contribuição", f"{df_filtered['contribution_rate'].mean():.2f}%")
c4.metric("Issues", f"{df_filtered['open_issues_count'].sum():,}")

st.divider()

# Gráficos usando o módulo components
col_l, col_r = st.columns(2)
with col_l:
    st.subheader("🏆 Engajamento")
    st.plotly_chart(plot_engagement_bar(df_filtered), use_container_width=True)

with col_r:
    st.subheader("🔍 Estrelas vs Tamanho")
    st.plotly_chart(plot_stars_vs_size(df_filtered), use_container_width=True)

st.subheader("📋 Detalhes")
cols_to_show = ['full_name', 'owner', 'stargazers_count', 'forks_count', 'contribution_rate', 'engagement_rate', 'size_mb']
st.dataframe(df_filtered[cols_to_show], use_container_width=True)