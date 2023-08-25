import unittest
from unittest.mock import patch
from guess_game import generate_random_number, compare_numbers, play_game

class TestGuessGame(unittest.TestCase):

    def test_generate_random_number(self):
        random_number = generate_random_number()
        self.assertTrue(random_number.isdigit())
        self.assertEqual(len(random_number), 4)

    def test_compare_numbers(self):
        secret_number = "1234"
        self.assertEqual(compare_numbers(secret_number, "5678"), "")
        self.assertEqual(compare_numbers(secret_number, "1243"), "XXOO")
        self.assertEqual(compare_numbers(secret_number, "1234"), "OOOO")
        self.assertEqual(compare_numbers(secret_number, "4321"), "XXXX")

    @patch('builtins.input', side_effect=['1234', '5678', 'q'])
    def test_play_game(self, mock_input):
        with patch('builtins.print') as mock_print:
            play_game()
            calls = [unittest.mock.call("Hints: XXOO"),
                     unittest.mock.call("Congratulations! You've guessed the number 1234 in 1 attempts.")]
            mock_print.assert_has_calls(calls)

if __name__ == '__main__':
    unittest.main()