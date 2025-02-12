from EmotionDetection import sentiment_analyzer

print("Unit Test for Emotion Detection")
sentiment_analyzer("I am glad this happened") # Expected output: "joy"
sentiment_analyzer("I am really mad about this") # Expected output: "anger"
sentiment_analyzer("I feel disgusted just hearing about this") # Expected output: "disgust"
sentiment_analyzer("I am so sad about this") # Expected output: "sadness"
sentiment_analyzer("I am really afraid that this will happen") # Expected output: "fear"
