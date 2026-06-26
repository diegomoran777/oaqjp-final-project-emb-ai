from EmotionDetection.emotion_detection import emotion_detector 
import unittest

class EmotionDetectionTest(unittest.TestCase):

    
    def test_emotion_detection(self):
        statement_joy = "I am glad this happened"
        statement_anger = "I am really mad about this"
        statement_disgust = "I feel disgusted just hearing about this"
        statement_sadness = "I am so sad about this"
        statement_fear = "I am really afraid that this will happen"

        self.assertEqual(emotion_detector(statement_joy)["dominant_emotion"], "joy")
        self.assertEqual(emotion_detector(statement_anger)["dominant_emotion"], "anger")
        self.assertEqual(emotion_detector(statement_disgust)["dominant_emotion"], "disgust")
        self.assertEqual(emotion_detector(statement_sadness)["dominant_emotion"], "sadness")
        self.assertEqual(emotion_detector(statement_fear)["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()