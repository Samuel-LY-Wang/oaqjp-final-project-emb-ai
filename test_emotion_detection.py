from EmotionDetection import emotion_detection

in_dict = {
    "I am glad this happened": "joy",
    "I am really mad about this": "anger",
    "I feel disgusted just hearing about this": "disgust",
    "I am so sad about this": "sadness",
    "I am really afraid that this will happen": "fear"
}

class Test_emotion_detection:
    def __init__(self):
        self.answer_key=in_dict
    
    def test_detection(self):
        for key in self.answer_key.keys():
            assert emotion_detection.emotion_detector(key)['dominant_emotion'] == self.answer_key[key]

tester = Test_emotion_detection()
tester.test_detection()