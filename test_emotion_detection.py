from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        response1 = sentiment_analyzer("I am glad this happened")
        self.assertEqual(response1['dominant_emotion'], "joy")

        response2 = sentiment_analyzer("I am really mad about this")
        self.assertEqual(response2['dominant_emotion'], "anger")

        response3 = sentiment_analyzer("I feel disgusted just hearing about this")
        self.assertEqual(response3['dominant_emotion'], "disgust")

        response4 = sentiment_analyzer("I am so sad about this")
        self.assertEqual(response4['dominant_emotion'], "sadness")

        response5 = sentiment_analyzer("I am really afraid that this will happen")
        self.assertEqual(response5['dominant_emotion'], "fear")

unittest.main()

