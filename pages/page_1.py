import streamlit as st

code = '''
import streamlit as st

st.title('ふわアプリ')
st.caption('python勉強用')
st.subheader('自己紹介')
st.text('python勉強中\n'
        'streamlitのテスト')
'''

st.code(code, language='python')
