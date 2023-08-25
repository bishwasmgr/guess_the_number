import unittest
from guess_the_number import GuessTheNumberGame

class TestGuessTheNumberGame(unittest.TestCase):
    def setUp(self):
        self.game = GuessTheNumberGame()

    def test_generate_random_number(self):
        random_number = self.game.generate_random_number()
        self.assertIsInstance(random_number, str)
        self.assertTrue(1000 <= int(random_number) <= 9999)

    # def test_get_feedback(self):
    #     feedback = self.game.get_feedback("1234")
    #     self.assertEqual(feedback, "xxxx")

    #     feedback = self.game.get_feedback("4321")
    #     self.assertEqual(feedback, "oooo")

    #     feedback = self.game.get_feedback("1243")
    #     self.assertEqual(feedback, "ooox")


if __name__ == '__main__':
    unittest.main()
