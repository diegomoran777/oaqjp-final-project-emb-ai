import requests

def emotion_detector(text_to_analyse):
    if text_to_analyse is None or text_to_analyse.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }, 400


    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    myobj = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    response = requests.post(url, json = myobj, headers = header)
    formatted_response = response.json()
    
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key = emotions.get)

    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }, 200