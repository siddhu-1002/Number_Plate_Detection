import streamlit as st
import cv2
import os
from Numberplate import process


# Giving title in our web app
st.title("Number plate Detection for 4-wheelers")

# Detect characters on the Number Plate
def detect(image_path):
    if st.button("Detect"):
        try:
            text = process(image_path)
            st.write(text)
        except Exception:
            st.write("Could not detect")


# Save the uploaded files in our data
def save_uploadedfile(uploadedfile):
    with open(os.path.join("Number plates/", uploadedfile.name),"wb") as f:
        f.write(uploadedfile.getbuffer())
    return


file = st.file_uploader(label="Select the image", accept_multiple_files=False)

if file is not None:
    
#     if file.name not in os.listdir("Number plates"):
    save_uploadedfile(file)
    st.write("File Saved successfully")
    st.image("Number plates/" + file.name)
    detect("Number plates/" + file.name)
#     else:
#         st.image("Number plates/" + file.name)
#         detect("Number plates/" + file.name)
