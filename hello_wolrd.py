import streamlit as st 
import pandas as pd
 
st.write(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)

st.write(pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
}))

st.title('Belajar Analisis Data')
st.header('Pengembangan Dashboard')
st.subheader('Pengembangan Dashboard')
st.caption('Copyright (c) 2023')
code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')

st.text('Halo, calon praktisi data masa depan.')

st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")