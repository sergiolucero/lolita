import streamlit as st
import os

os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

st.markdown(
    """
    <h3 style="color: #FFD700; text-align: center; font-size: 48px; font-weight: bold; text-shadow: 2px 2px 4px #000000;">LolitaGPT</h3>
    """,
    unsafe_allow_html=True,
)
