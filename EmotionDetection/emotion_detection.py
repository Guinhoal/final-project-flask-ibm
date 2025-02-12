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
        "domination": 0.0
    }


    emotion_scores["joy"] = max(0, positive - (neutral * 0.5) - (negative * 0.3))

    anger_base = 0.4
    disgust_base = 0.2
    fear_base = 0.2
    sadness_base = 0.2

    if negative > positive:
        anger_base = 0.4
        disgust_base = 0.2
        fear_base = 0.2
        sadness_base = 0.2

    if neutral > 0.05:
        disgust_base += neutral * 2  
        fear_base -= neutral  
        sadness_base += neutral * 1.5  

    total = anger_base + disgust_base + fear_base + sadness_base
    anger_base /= total
    disgust_base /= total
    fear_base /= total
    sadness_base /= total

    emotion_scores["anger"] = negative * anger_base
    emotion_scores["disgust"] = negative * disgust_base
    emotion_scores["fear"] = negative * fear_base
    emotion_scores["sadness"] = negative * sadness_base

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
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
    score = formatted_response['documentSentiment'][score]
    return json.dumps({
        "text": text_to_analyse,
        "positive": positive,
        "negative": negative,
        "neutral": neutral,
        "score": score
    })

def sentiment_normal(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    return json.dumps(formatted_response)