import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
st.write(
    """
    # Haloo Semuanya
    Ini adalah web pertamaku
    """
)

st.write('''
kita mempunyai sebuah fungsi yaitu:
''')

st.latex(r'y=x^2+2x+1')
st.write('''
Lalu, kita akan membuat grafik untuk fungsi tersebut
''')

def f(x):
 return x**2+2*x+1

x=np.linspace(0,10,100)

plt.figure(figsize=(12, 5))
plt.plot(x, f(x))
plt.title("Plot Fungsi diatas")
plt.show()

st.pyplot(plt)
