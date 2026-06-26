"""
Flask server application for emotion detection.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detection():
    """Analyze text and return detected emotions."""

    text_to_analyze = request.args.get('textToAnalyze')
    emotions, status_code = emotion_detector(text_to_analyze)

    if emotions['dominant_emotion'] is None and status_code == 400:
        return "¡Texto inválido! ¡Por favor, intenta de nuevo!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']} and "
        f"'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(debug=True)
