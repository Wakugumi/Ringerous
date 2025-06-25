import unittest
import tkinter as tk
from ui.components.GridContainer import GridContainer

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert class TestGridContainer(unittest.TestCase): def setUp(self): self.root = tk.Tk() self.root.withdraw() def tearDown(self): self.root.destroy() def test_add_widgets_to_grid(self): container = GridContainer(self.root, columns = 2) w1 = tk.Label(container, text="test") w2 = tk.Label(container, text="test") w3 = tk.Label(container, text="test") container.add(w1) container.add(w2) container.add(w3) self.assertEqual(w1.grid_info()['row'], 0) self.assertEqual(w1.grid_info()['column'], 0) self.assertEqual(w2.grid_info()['row'], 0) self.assertEqual(w2.grid_info()['column'], 1) self.assertEqual(w3.grid_info()['row'], 1) self.assertEqual(w3.grid_info()['column'], 0) def test_gap_is_applied(self): container = GridContainer(self.root, columns = 2, gap=12) w = tk.Label(container, text="test") container.add(w) self.assertEqual(int(w.grid_info()['padx']), 12) if __name__ == "__main__": unittest.main()
