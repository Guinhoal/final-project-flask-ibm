import requests
import json

def sentiment_analyzer(text_to_analyse):  
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'  
    myobj = { "raw_document": { "text": text_to_analyse } }  
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}  
    response = requests.post(url, json = myobj, headers=header) 
    formatted_response = json.loads(response.text)
    sentiments = formatted_response["documentSentiment"]["sentimentMentions"][0]["sentimentprob"]
    positive = sentiments["positive"]
    neutral = sentiments["neutral"]
    negative = sentiments["negative"]
       emotion_scores = {
        "anger": 0.0,
        "disgust": 0.0,
        "fear": 0.0,
        "joy": 0.0,
        "sadness": 0.0,
        "dominantion": ""
    }

    # Calcula a alegria somente com base nas pontuações
    joy = max(0, positive - (neutral * 0.5) - (negative * 0.3))
    emotion_scores["joy"] = joy

    # Se a alegria domina, a emoção dominante é "joy"
    if joy > negative:
        dominant_emotion = "joy"
    else:
        # Caso contrário, escolhe a emoção negativa com base no valor de neutral
        if neutral >= 0.05:
            dominant_emotion = "anger"
            emotion_scores["anger"] = negative
        elif neutral < 0.011:
            dominant_emotion = "disgust"
            emotion_scores["disgust"] = negative
        elif neutral < 0.012:
            dominant_emotion = "sadness"
            emotion_scores["sadness"] = negative
        else:
            dominant_emotion = "fear"
            emotion_scores["fear"] = negative

    emotion_scores["dominantion"] = dominant_emotion

    return json.dumps(emotion_scores)

def sentiment_analyzer_with_points(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    positive = formatted_response['documentSentiment']['sentimentMentions'][0]['sentimentprob']['positive']
    negative = formatted_response['documentSentiment']['sentimentMentions'][0]['sentimentprob']['negative']
    neutral = formatted_response['documentSentiment']['sentimentMentions'][0]['sentimentprob']['neutral']
    return json.dumps({
        "text": text_to_analyse,
        "positive": positive,
        "negative": negative,
        "neutral": neutral
    })