from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    # Здесь будет логика для обработки вопроса с использованием языковой модели
    answer = "Ответ на ваш вопрос"  # Замените на реальный ответ
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)