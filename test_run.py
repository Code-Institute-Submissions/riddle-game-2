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
        
    # Test if answers with different capitalization are accepted
    def test_if_answer_is_accepted(self):
        answer1 = run.answer_to_lowercase('KEYBOARD')
        answer2 = run.answer_to_lowercase('KeYbOaRd')
        riddle_answer = run.riddles_data[2]['answer'].lower()
        self.assertEqual(answer1, riddle_answer)
        self.assertEqual(answer2, riddle_answer)
        
    # Test if answer is a word - only alphabetic characters
    def test_if_answer_is_a_word(self):
        answer1 = run.answer_is_a_word('dfshajfh')
        answer2 = run.answer_is_a_word('dsf3sdga')     
        answer3 = run.answer_is_a_word('dfsasd-sf')
        self.assertTrue(answer1)
        self.assertFalse(answer2)
        self.assertFalse(answer3)