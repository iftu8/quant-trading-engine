import os
import google.generativeai as genai

# GitHub er Environment variables theke API key ta tene nibe
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("Error: API Key pawa jayni! GitHub Secrets thik ache kina check korun.")
else:
    # Gemini ke API key diye configure kora
    genai.configure(api_key=api_key)
    print("Gemini API successfully connected!")

# Ebar er nicha theke apnar baki Pandas, Numpy ba Trading er code gulo thakbe...
