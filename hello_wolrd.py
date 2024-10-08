import streamlit as st 
import pandas as pd
 
st.write(
    """
    # Latihan web pertama Udin
    Hallo Zahraku, ini aku lagi latihan buat web yaa, bisa minta tolong didukung bukan direwelin!
    """
)

st.write(
 """
 Kamu sayang aku gasi? kalau emang sayang ya didukung belajar terus.
 Aku gasuka kamu rewel terus yaa, tapi kadang juga suka kangen rewelan dari kamu si. Tapi ya gimana ya, jangan banyak-banyak rewelnya.
 Kalau kamu tetep rewel, nanti kamu aku suruh buat ngafalin rumus di bawah ini....!
 """)

st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")
