import google.generativeai as genai

genai.configure(api_key="KEY HERE")  # Replace with your actual key

try:
    models = genai.list_models()
    for model in models:
        print(model.name)  # List all available models
except Exception as e:
    print(f"Error: {str(e)}")
