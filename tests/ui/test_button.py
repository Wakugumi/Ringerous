import unittest
import tkinter as tk
from unittest.mock import Mock
from ui.components.Button import Button

class TestButton(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()

    def tearDown(self):
        self.root.destroy()

    def test_button_text(self):
        btn = Button(self.root, text="Test")

        self.assertEqual(btn.button['text'], "Test")

    def test_button_command(self):
        mock_cmd = Mock()

        btn = Button(self.root, text="click", action = mock_cmd)

        btn.button.invoke()
        mock_cmd.assert_called_once()

if __name__ == "__main__":
    unittest.main()
