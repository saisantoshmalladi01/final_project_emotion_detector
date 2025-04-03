import requests
import json
def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = input_json, headers=header)
    response_text_dict = json.loads(response.text)
    # Extract set of emotions
    emotions = response_text_dict["emotionPredictions"][0]["emotion"]
    # Get Emotion-Key with highest score
    key_max_score = max(emotions, key = emotions.get)
    analysis_result = {
            'anger': emotions["anger"],
            'disgust': emotions["disgust"],
            'fear': emotions["fear"],
            'joy': emotions["joy"],
            'sadness': emotions["sadness"],
            'dominant_emotion': key_max_score
        }

    return analysis_result
    