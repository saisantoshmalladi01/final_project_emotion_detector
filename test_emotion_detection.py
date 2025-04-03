"""Tests for emotion_detection.py"""


import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """All test cases for emotion_detection.py"""
    def test_dominant_emotion_joy(self):
        """ Test dominant emotion: joy """
        emotions = emotion_detector("I am glad this happened")
        self.assertEqual(emotions["dominant_emotion"], "joy")

    def test_dominant_emotion_anger(self):
        """ Test dominant emotion: anger """
        emotions = emotion_detector("I am really mad about this")
        self.assertEqual(emotions["dominant_emotion"], "anger")

    def test_dominant_emotion_disgust(self):
        """ Test dominant emotion: disgust """
        emotions = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(emotions["dominant_emotion"], "disgust")

    def test_dominant_emotion_sadness(self):
        """ Test dominant emotion: sadness """
        emotions = emotion_detector("I am so sad about this")
        self.assertEqual(emotions["dominant_emotion"], "sadness")

    def test_dominant_emotion_fear(self):
        """ Test dominant emotion: fear """
        emotions = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(emotions["dominant_emotion"], "fear")


# To make sure that the unittest file only runs when the script is executed
# directly (not imported as a module)
if __name__ == '__main__':
    unittest.main()