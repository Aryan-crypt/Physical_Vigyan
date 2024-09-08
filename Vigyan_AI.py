from flask import Flask, request, jsonify
import google.generativeai as genai

# Configure the API key for Google Generative AI
genai.configure(api_key="AIzaSyBNyvD_iXX21_bFEJBdXoGgU1EZWaTj1Uc")

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    # Get the message from ESP8266
    user_input = request.json.get('message')

    # Configure the AI model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 0,
        "max_output_tokens": 8192,
    }

    # Initialize the conversation
    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest", generation_config=generation_config)
    convo = model.start_chat(history=[])
    convo.send_message(user_input)
    
    # Get the AI's response
    response_text = convo.last.text

    # Return the AI response back to ESP8266
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
