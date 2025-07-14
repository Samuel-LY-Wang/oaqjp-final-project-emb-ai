'''
The server that actually runs this program
'''

from flask import Flask, render_template, request
from EmotionDetection import emotion_detection

app=Flask(__name__)

@app.route("/")
def index():
    '''
    Just renders everything needed to take in input, from index.html
    '''
    return render_template("index.html")

@app.route("/emotionDetector")
def display():
    '''
    Takes in the AI's analysis of the text and prints out what was found
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    out = emotion_detection.emotion_detector(text_to_analyze)
    out_str = f'''For the given statement, the system response is 'anger': {out['anger']},
     'disgust': {out['disgust']},
      'fear': {out['fear']},
       'joy': {out['joy']},
        'sadness': {out['sadness']}.
         The dominant emotion is <b>{out['dominant_emotion']}</b>.'''
    if out['dominant_emotion']:
        return out_str
    return "Invalid text! Please try again."

if __name__ == "__main__":
    app.run(debug=True)
