import streamlit as st
import time

st.title("Stream 超入門")

st.write("Interactive")

left_clumu, right_clumu = st.columns(2)
button = left_clumu.button("右カラムに文字を表示")
if button:
    right_clumu.write("ここは右カラム")

expander = st.expander("問い合わせ")
expander.write("問い合わせ内容を書く")
# text = st.text_input("あなたの趣味は？")
# "あなたの趣味:", text 

# co = st.slider("あなたの今の調子は？" , 0, 100, 50)
# "コンディション",co 

# if st.checkbox("Show Image"):
#     img = Image.open("test.jpg")
#     st.image(img, caption="Kingyo", use_column_width=True)