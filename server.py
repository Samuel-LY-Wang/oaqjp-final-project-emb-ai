from flask import Flask
from EmotionDetection import emotion_detection

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector/<textToAnalyze>")
def display(textToAnalyze):
    out = emotion_detection.emotion_detector(textToAnalyze)
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