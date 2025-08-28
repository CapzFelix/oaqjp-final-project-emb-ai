import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL for the emotion detection API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Set the header with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Make a POST request to the API with the payload and header
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # Parse the specific emotion score into a dictionary
    emotion_results = {
        'anger': formatted_response['emotionPredictions'][0]['emotion']['anger'],
        'disgust': formatted_response['emotionPredictions'][0]['emotion']['disgust'],
        'fear': formatted_response['emotionPredictions'][0]['emotion']['fear'],
        'joy': formatted_response['emotionPredictions'][0]['emotion']['joy'],
        'sadness': formatted_response['emotionPredictions'][0]['emotion']['sadness']
        }

    # Find the emotion with the highest score
    max_key = max(emotion_results, key=emotion_results.get)

    # Append the dominant emotion into the dictionary
    emotion_results['dominant_emotion'] = max_key

    # Return the dictionary result
    return emotion_results