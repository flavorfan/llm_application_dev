import streamlit as st
import pandas as pd
import numpy as np

st.write("""
# confidence formular for workday

This app predicts the type!
""")

# sidebar
st.sidebar.header('User Input Parameters')


def user_input_features():
    a = st.sidebar.slider('a: x轴平移', 0.0, 8.0, 0.8, 0.1)
    b = st.sidebar.slider('b：y轴平移', -1, 1, 0)
    c = st.sidebar.slider('c：x轴拉伸', -1.0, 2.0, 1.0, 0.1)

    st.sidebar.subheader('r:出勤率')
    r = st.sidebar.slider('r:出勤率', 0.1, 1.0, 1.0, 0.1)

    d = (1 - (1-r)**2) ** 0.5
 
    data = {'a': a,
            'b': b,
            'c': c,
            'r': r, 
            'd': d}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

# main window
st.subheader('参数设定')
st.write(df)

def sigmoid(x, a, b, c=1, d=1):
    return d / (1 + np.exp(-c*(x - a))) + b

x = np.linspace(1.0, 20.0, 100)
# y = sigmoid(x, a=15, b=0,  c=-0.3, d=1)
a = df.a.values[0]
b = df.b.values[0]
c = df.c.values[0]
d = df.d.values[0]

y = sigmoid(x, a, b,  c, d)

# convert x, y to dataframe
st.subheader('sigmoid函数曲线: x = total_cnt')
chart_data = pd.DataFrame(zip(x,y), columns=['x', 'y'])
st.line_chart(chart_data, x='x', y='y')

# datafram
st.subheader('数据表格')
table_x = np.linspace(1, 16, 16)
table_y = sigmoid(table_x, a, b,  c, d)
table_data = pd.DataFrame(zip(table_x,table_y), columns=['cnt', 'confidence_max'])
st.write(table_data)
