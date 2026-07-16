import tkinter as tk
import random
import time

# Random paragraphs, you can add your own if you want (;
paragraphs = [
    "Learning Python is fun and helps you build amazing projects.",
    "Typing games improve your speed and accuracy while making practice enjoyable.",
    "Tkinter is a simple and powerful library for creating desktop applications."
]


class TypingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Game")

        self.start_time = None
        self.selected_text = random.choice(paragraphs)

        # Display paragraph
        self.text_label = tk.Label(
            root, text=self.selected_text, wraplength=500, font=("Arial", 14))
        self.text_label.pack(pady=20)

        # Input box
        self.input_box = tk.Text(root, height=5, width=60, font=("Arial", 14))
        self.input_box.pack()

        self.start_button = tk.Button(
            root, text="Start", command=self.start_game, font=("Arial", 12))
        self.start_button.pack(pady=10)

        # Result label
        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def start_game(self):
        self.start_time = time.time()
        self.result_label.config(text="Typing started...")

        self.root.bind("<Return>", self.finish_game)

    def finish_game(self, event):
        end_time = time.time()
        typed_text = self.input_box.get("1.0", tk.END).strip()

        time_taken = end_time - self.start_time
        words = len(typed_text.split())
        wpm = round((words / time_taken) * 60)

        correct = 0
        for a, b in zip(typed_text, self.selected_text):
            if a == b:
                correct += 1
        accuracy = round((correct / len(self.selected_text)) * 100)

        self.result_label.config(
            text=f"Time: {round(time_taken, 2)} sec | WPM: {wpm} | Accuracy: {accuracy}%"
        )

        return "break"


root = tk.Tk()
game = TypingGame(root)
root.mainloop()
