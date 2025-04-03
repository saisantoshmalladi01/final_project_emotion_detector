"""Server for Web Deployment"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Create the Flask app
app = Flask("Emotion Detection")

@app.route('/')
def render_homepage():
    """ Render homepage """
    return render_template("index.html")

@app.route('/emotionDetector', methods=["GET"])
def emotion_analysis() -> str:
    """ Analyze text and return emotion detection (analysis result) """
    text_to_analyze = request.args.get("textToAnalyze", "").strip()

    # Check for blank input
    if not text_to_analyze:
        return "Invalid text! Please try again!"

    analysis_result = emotion_detector(text_to_analyze)

    # Check if analysis failed or input was bad
    if analysis_result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    
    # Build response
    response = "For the given statement, the system response is"

    for key, value in analysis_result.items():
        if key != "dominant_emotion":
            response += f" '{key}': {value},"

    # Replace last comma with period
    last_comma_index = response.rfind(",")
    if last_comma_index != -1:
        response = response[:last_comma_index] + '.' + response[last_comma_index + 1:]

    response += f" The dominant emotion is {analysis_result['dominant_emotion']}."

    return response

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
