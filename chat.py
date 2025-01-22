import sys
# Uncomment the following lines if the g4f package is not detected automatically
# print(sys.executable)
# sys.path.append(r"C:\Users\<active_user_name>\AppData\Roaming\Python\<Python_venv_version>\site-packages")

import g4f
import streamlit as st

st.title('Chatbot GUI')

inp = st.text_area('Hello! How can I help you? Write your desired text or ask your question below:')

ok = st.button('Press to Chat')

if inp != "" and ok:
    response = g4f.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "user", "content": inp}],
        stream=True
    )

    response_placeholder = st.empty()  # Placeholder for streaming response

    full_response = ""
    for message in response:
        full_response += "".join(message)
        # Update the placeholder dynamically
        response_placeholder.markdown(full_response)
    
    # Final display of the response (remove duplicate display)
    response_placeholder.markdown(full_response)  # Only use the placeholder
