from gui.gui_interface import OthelloGUI
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = OthelloGUI(root)
    root.mainloop()