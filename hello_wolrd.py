import streamlit as st 
import pandas as pd
 
st.write(
    """
    # Latihan web pertama Udin
    Hallo Zahraku, ini aku lagi latihan buat web yaa, bisa minta tolong didukung bukan direwelin!
    """
)

st.text('Halo, bisa kerjakan soal berikut yaa....')

st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")
