import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

if 'data' not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv")
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year ]
    df_data = df_data[df_data['Value(£)'] > 0 ]
    df_data = df_data.sort_values(by='Overall', ascending=False)
    st.session_state['data'] = df_data


st.markdown("# FIFA23 OFFCIAL DATASET! ⚽")
st.sidebar.markdown(f"Desenvolvido por:")
st.sidebar.markdown("Luan Rodrigues")

btn = st.link_button(
            "Acesse os dados no Kagle",
            "https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database"
                    )

# if btn:
#     webbrowser.open_new_tab("https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database")

st.markdown(
    """
Texto Aleatório
"""
)    