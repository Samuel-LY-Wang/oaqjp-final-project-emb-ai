import requests

url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
header={
    'Content-Type': 'application/json',
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}

def get_dominant_emotion(in_dict):
    max_val=max(in_dict.values())
    for key in in_dict.keys():
        if in_dict[key] == max_val:
            return key
    return None

def emotion_detector(input_text):
    API_input={"raw_document": {"text": input_text}}
    response = requests.post(url, headers=header, json=API_input).json()['emotionPredictions'][0]['emotion']
    out = {
        'anger': response['anger'],
        'disgust': response['disgust'],
        'fear': response['fear'],
        'joy': response['joy'],
        'sadness': response['sadness'],
        'dominant_emotion': get_dominant_emotion(response)
    }
    return out