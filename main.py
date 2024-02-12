import google.generativeai as genai

genai.configure(api_key="YOUR API KEY")
model = genai.GenerativeModel('gemini-pro')

def gemini(promt):
    response = model.generate_content(contents=prompt)
    return response.text

gemini("How to center a Div in CSS?")

