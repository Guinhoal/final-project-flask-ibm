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
        "joy": positive,
        "anger": negative * 0.6,
        "disgust": negative * 0.2,
        "fear": negative * 0.1,
        "sadness": negative * 0.1
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return json.dumps({
        "text": text_to_analyse,
        "dominantion": dominant_emotion
    })

def sentiment_analyzer_with_points(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)
    positive = formatted_response['documentSentiment']['sentimentMentions'][0]['sentimentprob']['positive']
    negative = formatted_response['documentSentiment']['sentimentMentions'][0]['sentimentprob']['negative']
    neutral = formatted_response['documentSentiment']['sentimentMentions'][0]['sentimentprob']['neutral']
    score = formatted_response['documentSentiment']["score"]
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