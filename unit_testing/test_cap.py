import unittest
import cap # import any of the scripts you're working on

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        # the result got from "result" is 'Python'?
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')

    
if __name__ == '__main__':
    unittest.main()