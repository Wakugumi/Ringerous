import unittest
import tkinter as tk
from unittest.mock import Mock
from ui.Label import Label


class TestLabel(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()

    def tearDown(self):
        self.root.destroy()

    def test_label_text(self):
        label = Label(self.root, text="Test")

        self.assertEqual(label.label['text'], "Test")


if __name__ == "__main__":
    unittest.main()


