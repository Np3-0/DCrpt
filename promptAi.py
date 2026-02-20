from google import genai

def promptAI(client, text, data):
    
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=text + "\n" + "\n".join(data),
    )
    return response.text
