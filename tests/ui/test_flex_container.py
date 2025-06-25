import unittest
import tkinter as tk
from ui.components.FlexContainer import FlexContainer

class TestFlexContainer(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.root.withdraw()

    def tearDown(self):
        self.root.destroy()

    def test_add_horizontal_buttons(self):
        container = FlexContainer(self.root, direction="row")
        
        btn1 = tk.Button(container, text="1")
        btn2 = tk.Button(container, text="2")
        container.add(btn1)
        container.add(btn2)

        self.assertEqual(btn1.pack_info()['side'], 'left')
        self.assertEqual(btn2.pack_info()['side'], 'left')

    def test_add_vertical_buttons(self):
        container = FlexContainer(self.root, direction="column")

        btn1 = tk.Button(container, text="1")
        btn2 = tk.Button(container, text="2")
        container.add(btn1)
        container.add(btn2)
        self.assertEqual(btn1.pack_info()['side'], 'top')
        self.assertEqual(btn2.pack_info()['side'], 'top')

        

if __name__ == "__main__":
    unittest.main()


