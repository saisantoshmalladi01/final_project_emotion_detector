"""Emotion Detection application file"""

import json
import requests

def emotion_detector(text_to_analyze: str) -> str:
    """ 
    Run emotion detection using Watson NLP library.

    NOTE: 
    Currently, this code only works with IBM Cloud IDE!    
    Otherwise, ConnectionError occurs.
    """
    # Get emotion analysis using Watson NLP Library
    response = requests.post(
        url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict',  # pylint: disable=line-too-long
        headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
        json={"raw_document": {"text": text_to_analyze}},
        timeout=20
    )

    if response.status_code == 400:
        analysis_result = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        # Convert JSON to Dictionary
        response_text_dict = json.loads(response.text)

        # Extract set of emotions
        emotions = response_text_dict["emotionPredictions"][0]["emotion"]

        # Get Emotion-Key with highest score
        key_max_score = max(emotions, key=emotions.get)

        analysis_result = {
            'anger': emotions["anger"],
            'disgust': emotions["disgust"],
            'fear': emotions["fear"],
            'joy': emotions["joy"],
            'sadness': emotions["sadness"],
            'dominant_emotion': key_max_score
        }

    return analysis_result
