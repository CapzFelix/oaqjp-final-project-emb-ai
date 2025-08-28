''' This server file render a Web App using Flask to run Emotion Detection analysis '''
# Import Flask, render_template, request from the flask pramework package
# Import the emotion_detector function from the package created
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detection():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # Send GET request to receives text to analyze
    text_to_analyze = request.args.get('textToAnalyze')

    # Parse response from emotion_detector function
    response = emotion_detector(text_to_analyze)

    # Gather all the scores for different emotions
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return f"""For the given statement, the system response is 'anger': {anger_score},
            'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and 
            'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}"""

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
