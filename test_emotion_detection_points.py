from EmotionDetection import sentiment_analyzer, sentiment_analyzer_with_points
import json

print("Unit Test for Emotion Detection")
joy = json.loads(sentiment_analyzer_with_points("I am glad this happened")) # Expected output: "joy"
anger = json.loads(sentiment_analyzer_with_points("I am really mad about this")) # Expected output: "anger"
disgust = json.loads(sentiment_analyzer_with_points("I feel disgusted just hearing about this")) # Expected output: "disgust"
sadness = json.loads(sentiment_analyzer_with_points("I am so sad about this")) # Expected output: "sadness"
fear = json.loads(sentiment_analyzer_with_points("I am really afraid that this will happen")) # Expected output: "fear"

print(joy)
print(anger)
print(disgust)
print(sadness)
print(fear)
