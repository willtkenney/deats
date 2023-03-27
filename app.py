import os
import openai
from flask import Flask, request, jsonify

app = Flask(__name__)
openai.api_key = "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"

def is_vegetarian(text):
    prompt = f"Is the menu item '{text}' typically vegetarian?"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=10,
        n=1,
        stop=None,
        temperature=0.5,
    )

    answer = response.choices[0].text.strip()
    return answer.lower() == "yes"

@app.route('/menu_items/vegetarian', methods=['POST'])
def get_vegetarian_items():

    menu_items = request.json.get('menu_items', [])
    print("Received request with the following menu items:")
    print(menu_items)

    vegetarian_items = [item for item in menu_items if is_vegetarian(item)]

    print("Returning the following vegetarian menu items:")
    print(vegetarian_items)

    return jsonify(vegetarian_items)

if __name__ == '__main__':
    app.run(debug=True)
