import tkinter as tk
import random
import time

# Random paragraphs, you can add your own if you want (;
paragraphs = [
    "Learning Python is fun and helps you build amazing projects.",
    "Typing games improve your speed and accuracy while making practice enjoyable.",
    "Tkinter is a simple and powerful library for creating desktop applications.",
    "Practice makes perfect, so keep typing every single day.",
    "The quick brown fox jumps over the lazy dog near the river.",
]

BG = "#1e1e2e"
FG = "#f5f5f5"
ACCENT = "#89b4fa"
GOOD = "#a6e3a1"
BAD = "#f38ba8"
MUTED = "#6c7086"


class TypingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Game")
        self.root.configure(bg=BG)
        self.root.geometry("650x420")
        self.root.resizable(False, False)

        self.start_time = None
        self.timer_job = None
        self.running = False
        self.selected_text = ""

        title = tk.Label(
            root, text="⌨  Typing Speed Test", font=("Arial", 20, "bold"),
            bg=BG, fg=ACCENT
        )
        title.pack(pady=(20, 10))

        self.text_label = tk.Label(
            root, text="Press Start to begin...", wraplength=550,
            font=("Arial", 14), bg=BG, fg=FG, justify="left"
        )
        self.text_label.pack(pady=(0, 15), padx=20)

        self.input_box = tk.Text(
            root, height=5, width=60, font=("Arial", 13),
            bg="#313244", fg=FG, insertbackground=FG,
            wrap="word", state="disabled", relief="flat", padx=10, pady=10
        )
        self.input_box.pack(padx=20)

        btn_frame = tk.Frame(root, bg=BG)
        btn_frame.pack(pady=15)

        self.start_button = tk.Button(
            btn_frame, text="Start", command=self.start_game, font=("Arial", 12, "bold"),
            bg=ACCENT, fg="#1e1e2e", relief="flat", padx=20, pady=5, cursor="hand2"
        )
        self.start_button.grid(row=0, column=0, padx=5)

        self.finish_button = tk.Button(
            btn_frame, text="Finish (Enter)", command=self.finish_game, font=("Arial", 12),
            bg="#45475a", fg=FG, relief="flat", padx=20, pady=5, cursor="hand2",
            state="disabled"
        )
        self.finish_button.grid(row=0, column=1, padx=5)

        self.restart_button = tk.Button(
            btn_frame, text="Restart", command=self.reset_game, font=("Arial", 12),
            bg="#45475a", fg=FG, relief="flat", padx=20, pady=5, cursor="hand2"
        )
        self.restart_button.grid(row=0, column=2, padx=5)

        self.timer_label = tk.Label(
            root, text="Time: 0.0s", font=("Arial", 12), bg=BG, fg=MUTED
        )
        self.timer_label.pack(pady=(5, 0))

        self.result_label = tk.Label(
            root, text="", font=("Arial", 14, "bold"), bg=BG, fg=GOOD
        )
        self.result_label.pack(pady=10)

        self.root.bind("<Return>", self._handle_enter)
        self.reset_game()

    def reset_game(self):
        self.running = False
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None

        self.selected_text = random.choice(paragraphs)
        self.text_label.config(text=self.selected_text, fg=FG)

        self.input_box.config(state="normal")
        self.input_box.delete("1.0", tk.END)
        self.input_box.config(state="disabled")

        self.result_label.config(text="")
        self.timer_label.config(text="Time: 0.0s")
        self.start_button.config(state="normal")
        self.finish_button.config(state="disabled")

    def start_game(self):
        self.running = True
        self.start_time = time.time()

        self.input_box.config(state="normal")
        self.input_box.delete("1.0", tk.END)
        self.input_box.focus_set()

        self.start_button.config(state="disabled")
        self.finish_button.config(state="normal")
        self.result_label.config(text="")
        self._tick()

    def _tick(self):
        if not self.running:
            return
        elapsed = time.time() - self.start_time
        self.timer_label.config(text=f"Time: {elapsed:.1f}s")
        self.timer_job = self.root.after(100, self._tick)

    def _handle_enter(self, event):
        if self.running and str(self.root.focus_get()) == str(self.input_box):
            self.finish_game()
            return "break"

    def finish_game(self, event=None):
        if not self.running:
            return

        self.running = False
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None

        end_time = time.time()
        typed_text = self.input_box.get("1.0", tk.END).strip()
        time_taken = max(end_time - self.start_time, 0.01)  # avoid div-by-zero

        self.input_box.config(state="disabled")
        self.start_button.config(state="normal")
        self.finish_button.config(state="disabled")
        self.timer_label.config(text=f"Time: {time_taken:.1f}s")

        
        wpm = round((len(typed_text) / 5) / (time_taken / 60)) if typed_text else 0

        
        typed_words = typed_text.split()
        target_words = self.selected_text.split()
        correct = sum(1 for t, o in zip(typed_words, target_words) if t == o)
        total = len(target_words) if target_words else 1
        accuracy = round((correct / total) * 100)

        color = GOOD if accuracy >= 80 else (ACCENT if accuracy >= 50 else BAD)
        self.result_label.config(
            text=f"⏱ {time_taken:.2f}s   |   🚀 {wpm} WPM   |   🎯 {accuracy}% accuracy",
            fg=color
        )


if __name__ == "__main__":
    root = tk.Tk()
    game = TypingGame(root)
    root.mainloop()
