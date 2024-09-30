import streamlit as st
import pandas as pd

# 浮動小数点の桁数の設定
#pd.set_option('display.float_format', lambda x: f'{x:.3f}')
#pd.options.display.precision = 3
df_2 = pd.read_excel('./data/sales_data/価格表.xlsx')
df_2=df_2.fillna(method='ffill')
st.dataframe(df_2)
