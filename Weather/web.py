import streamlit as st
# import pillow

# Header
st.header("This is a header with a divider", divider='rainbow')

# Subheader with colored text and emoji
st.header('_Streamlit_ is :blue[cool] :sunglasses:')

# Paragraphs and points
st.markdown('''
            This is a paragraph
            - 1
            - 2
            - 3
            ''')

# Clickable word to link
st.markdown('''
            [Subscribe](https://nitrotype.com)
            ''')

st.image("https://images.pexels.com/photos/2071882/pexels-photo-2071882.jpeg?cs=srgb&dl=pexels-wojciech-kumpicki-1084687-2071882.jpg&fm=jpg")

