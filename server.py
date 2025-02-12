from flask import Flask, request, jsonify, render_template
import json
from EmotionDetection.emotion_detection import sentiment_analyzer, sentiment_analyzer_total

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector")
def emotionDetector():
    text = request.args.get('textToAnalyze')
    response = sentiment_analyzer_total(text)
    response_json = json.loads(response)
    
    formatted_response = (
        f"Para a afirmação dada, a resposta do sistema é "
        f"'anger': {response_json['anger']}, "
        f"'disgust': {response_json['disgust']}, "
        f"'fear': {response_json['fear']}, "
        f"'joy': {response_json['joy']} e "
        f"'sadness': {response_json['sadness']}. "
        f"A emoção dominante é {response_json['dominantion']}."
    )
    
    return jsonify({"message": formatted_response})

if __name__ == "__main__":
    app.run(host="localhost", port=5000)