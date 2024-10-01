import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers = header)
    json_response = json.loads(response.text)
    # json.loads returns required dictionary within a list within the dictionary. Extract using list position. 
    formatted_response = json_response['emotionPredictions'][0]
    # If a valid response is returned:
    if response.status_code == 200:
        # Find required values and allocate to variables.
        anger_score = formatted_response['emotion']['anger']
        disgust_score = formatted_response['emotion']['disgust']
        fear_score = formatted_response['emotion']['fear']
        joy_score = formatted_response['emotion']['joy']
        sadness_score = formatted_response['emotion']['sadness']
        # Build requested dictionary format with key names and corresponding values returned above.
        emotions_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        }
        # Find highest emotion score in dectionary and set to variable dom_emotion.
        dom_emotion = max(emotions_dict, key=emotions_dict.get)
        # Append key 'dominant emotion' with value of dom_emotion variable to dictionary.
        emotions_dict['dominant_emotion'] = dom_emotion
        # Return dictionary in requested format.
        return emotions_dict

