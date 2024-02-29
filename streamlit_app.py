import streamlit as st
from groq import Groq  # Stellen Sie sicher, dass Groq korrekt installiert und importiert wird

# Initialisieren des Groq-Clients
client = Groq()

# Funktion, die die Groq API aufruft
def get_response(user_input):
    completion = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[
            {
                "role": "system",
                "content": "Du bist ein freundlicher Assistent, der perfektes Deutsch spricht. \n\nAntworte immer in \"du-form\" und sprich den User mit Jens an. \n\n"
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        stream=False,  # Ändern Sie dies je nach Bedarf
        stop=None,
    )
    
    # Extrahieren der Antwort aus der Antwort des Modells
    response = ""
    for chunk in completion:
        response += chunk.choices[0].delta.content or ""
    return response

# Streamlit Benutzeroberfläche
user_input = st.text_input("Frage etwas:")
if user_input:
    response = get_response(user_input)
    st.write(response)
