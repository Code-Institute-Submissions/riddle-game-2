import unittest
import run

class TestRiddle(unittest.TestCase):
    # Test for checking if username already exists
    def test_check_username_already_exists(self):
        check1 = run.check_if_username_already_exists('tjasa')
        check2 = run.check_if_username_already_exists('hgfsjkdgf')
        self.assertEqual(check1, True)
        self.assertEqual(check2, False)
        
    # Test if scores in top_scores are sorted in descending order
    def test_if_top_scores_sorted(self):
        top_scores = run.get_top_scores()
        scores = []
        for line in top_scores:
            scores.append(line[0])      
        def test_if_scores_sorted(a, b):
            return True if a >= b else False               
        scores_sorted1 = test_if_scores_sorted(scores[2], scores[5])
        scores_sorted2 = test_if_scores_sorted(scores[7], scores[3])
        self.assertTrue(scores_sorted1)
        self.assertFalse(scores_sorted2)
