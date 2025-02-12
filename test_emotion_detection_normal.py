from EmotionDetection import sentiment_analyzer_with_points, sentiment_analyzer, sentiment_normal
import json

print("Unit Test for Emotion Detection")
joy = json.loads(sentiment_normal("I am glad this happened")) # Expected output: "joy"
anger = json.loads(sentiment_normal("I am really mad about this")) # Expected output: "anger"
disgust = json.loads(sentiment_normal("I feel disgusted just hearing about this")) # Expected output: "disgust"
sadness = json.loads(sentiment_normal("I am so sad about this")) # Expected output: "sadness"
fear = json.loads(sentiment_normal("I am really afraid that this will happen")) # Expected output: "fear"

##print(joy)
print(anger)
##print(disgust)
##print(sadness)
##print(fear)
