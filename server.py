"""Module do servidor Flask para análise de emoções."""

import json
from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import sentiment_analyzer_total


app = Flask(__name__)


@app.route("/")
def index():
    """Renderiza a página index."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector():
    """Processa a análise de emoções e retorna uma mensagem formatada."""
    text = request.args.get('textToAnalyze')
    response = sentiment_analyzer_total(text)
    response_json = json.loads(response)

    if response_json.get("dominantEmotion") is None:
        return "Texto inválido! Por favor, tente novamente!"

    if "error" in response_json:
        return jsonify(response_json)

    message = (
        f"Para a afirmação dada, a resposta do sistema é 'anger': {response_json['anger']}, "
        f"'disgust': {response_json['disgust']}, "
        f"'fear': {response_json['fear']}, "
        f"'joy': {response_json['joy']} e "
        f"'sadness': {response_json['sadness']} "
        f"dominated emotion is {response_json['dominantEmotion']}."
    )
    return message


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
