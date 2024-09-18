import tkinter as tk
from interface import Interface
from graphbrain import GraphBrain


def main():
    root = tk.Tk()
    root.title("Pixela Automation")
    root.geometry("700x700")

    brain = GraphBrain()
    app_interface = Interface(root, brain)

    root.mainloop()


if __name__ == "__main__":
    main()
