from flask import Flask, render_template, request
from EmotionDetection import emotion_detection

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector")
def display():
    text_to_analyze = request.args.get("textToAnalyze")
    out = emotion_detection.emotion_detector(text_to_analyze)
    out_str = f'''For the given statement, the system response is 
    'anger': {out['anger']}, 
    'disgust': {out['disgust']}, 
    'fear': {out['fear']}, 
    'joy': {out['joy']}, 
    'sadness': {out['sadness']}. 
    The dominant emotion is <b>joy</b>.'''
    return out_str

if __name__ == "__main__":
    app.run(debug=True)