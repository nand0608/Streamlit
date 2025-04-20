import streamlit as st

st.title ("image project")

from PIL import Image
img = Image.open("im.jpg")
st.image(img,width=300,caption = "hellooooooo")

### vid_file = open("vi.mp4", "rb")
### vid_bytes = vid_file.read()
### st.write(vid_bytes) 

audio_file = open("au.mp3", "rb").read()
st.audio(audio_file)

