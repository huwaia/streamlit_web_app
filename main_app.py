import streamlit as st
from PIL import Image

st.title('ふわアプリ')
st.caption('python勉強用')

# 画像
image = Image.open('./data/touka.png')
st.image(image, width=200)

st.subheader('自己紹介')
st.text('python勉強中\n'
        'streamlitのテスト')

# 動画
video_file = open('./data/code_87.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
