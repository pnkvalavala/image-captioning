import requests
import streamlit as st
from imgcaptioning.pipeline import pipeline

st.set_page_config(
    page_title="Image Caption Generator",
    page_icon="📸",
    menu_items={
        'Report a bug': "https://github.com/pnkvalavala/image-captioning/issues",
        'About': "Just upload image and generate captions for free"
    }
)

st.markdown(
    "<h1 style='text-align: center;'>Image Caption Generator</h1>",
    unsafe_allow_html=True
)

option = st.selectbox('Image Source', ['URL', 'Upload', 'Camera'])
image = None

if option == 'Upload':
    image = st.file_uploader("Upload a image", type=['png', 'jpg'])
    if image:
        image = image.read()

elif option == 'URL':
    with st.form('url_form'):
        url = st.text_input("Enter Image URL")
        submit = st.form_submit_button("Submit")
    if submit:
        response = requests.get(url)
        image = response.content

elif option == 'Camera':
    image = st.camera_input("Take a picture")
    if image:
        image = image.read()

if image:
    output = pipeline(image=image)
    st.image(image)
    st.write(output)