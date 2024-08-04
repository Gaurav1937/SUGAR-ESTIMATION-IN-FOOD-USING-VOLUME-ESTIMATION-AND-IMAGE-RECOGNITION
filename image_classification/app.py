import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv() #loading all environment variable
from PIL import Image

# get api key from https://makersuite.google.com/ and save it in .env file
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt, image):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input_prompt,image[0]])
    return response.text

def input_image_setup(uploaded_file):
    #check whether file uploaded or not
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        #read file into bytes

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


#Initalize streamlit app Front end

st.set_page_config(page_title="Food recognision")

st.header("Health App using Gemini")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption= "uploaded Image.",use_column_width=True)

submit=st.button("Calculate Calories") 

input_prompt = """
You are an expert in nutritionist where you need to see the food items from the image
               and tell the sugar per gram, also provide the details of every food items
               in below format

               1. Item 1 - item name
               2. Item 2 - suger content per gram
               3. density of food.
"""

if submit:
    image_data = input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data)
    st.header("The response is")
    st.write(response)
