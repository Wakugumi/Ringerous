import unittest
import tkinter as tk
from unittest.mock import Mock
from ui.components.RadioGroup import RadioGroup

class TestRadioGroup(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()

    def tearDown(self):
        self.root.destroy()


    def test_default_selection(self):
        opts = ['a', 'b', 'c']

        default = 'a'

        radio = RadioGroup(self.root, options = opts, default = default)

        self.assertEqual(radio.get_value(), 'a')

    def test_set_value(self):
        radio = RadioGroup(self.root, options = ['a', 'b'], default = 'a')
        radio.set_value('b')

        self.assertEqual(radio.get_value(), 'b')
    
    def test_command_called(self):
        mock_callback = Mock()
        radio = RadioGroup(self.root, options = ['a', 'b'], command = mock_callback)

        radio.set_value('b')
        radio._on_change()

        mock_callback.assert_called_with('b')

if __name__ == "__main__":
    unittest.main()
