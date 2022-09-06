from PIL import Image
from typing import Container
import streamlit as st 
import phonenumbers
import requests
from streamlit_lottie import st_lottie


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None 
    return r.json()
#anamations assets
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_cwyafad8.json")
lottie_coding2 = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_uxftmfw0.json")

#images
image1 = Image.open("pictures/kayak.jpg")
image2 = Image.open("pictures/kayak1.jpg")
image3 = Image.open("pictures/fish.jpg")
#page title
st.set_page_config(page_title="JACKTROLL", page_icon=":imp:")

#page contents

st.title("Hello I am JACK! :smiling_imp:")
st.subheader("a Troll of prankery :sweat_smile:")

#links
st.write("---")
left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.header("This is the link to YT channel")
    st.write("[YT link here >](https://www.youtube.com/channel/UCZSMk0I15f2caNnJko6o4zg)")
    st.write("##")
    st.header("This is a link to DISCORD")
    st.write("[DISCORD link >](https://discord.gg/GuAFe6Swq2)")

#anamations
with middle_column:
    st_lottie(lottie_coding, height=150, width=150, key="youtube")
    st_lottie(lottie_coding2, height=150, width=150, key="discord")

with st.container():
    st.write("---")
    st.title("cool pictures :sunglasses:")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(image1)
        st.header("Nice log out of Badin lake")
        st.write("---")
        st.image(image2)
        st.header("Fishing day!!! :fishing_pole_and_fish: ")
        st.write("---")
        st.image(image3)
        st.header("3/4s Pound small mouth")

st.title("Email me I am lonley :sob:")
contact_form = """
<form action="https://formsubmit.co/cutemonkeyjack@gmail.com" method="POST">
     <input type="text" name="name" placeholder="your name" required>
     <input type="email" name="email" placeholder="your email" required>
     <textarea name="message" placeholder="your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
        


