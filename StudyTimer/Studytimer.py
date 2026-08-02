import tkinter as tk
from tkinter import font as tkfont
import math


WORK_MINUTES = 25
SHORT_BREAK_MINUTES = 5
LONG_BREAK_MINUTES = 15
SESSIONS_BEFORE_LONG_BREAK = 4

BG = "#1e1e2e"
FG = "#f5f5f5"
ACCENT = "#89b4fa"
WORK_COLOR = "#f38ba8"
BREAK_COLOR = "#a6e3a1"
TRACK_COLOR = "#313244"
MUTED = "#6c7086"

MODES = {
    "work": ("Focus", WORK_MINUTES, WORK_COLOR),
    "short_break": ("Short Break", SHORT_BREAK_MINUTES, BREAK_COLOR),
    "long_break": ("Long Break", LONG_BREAK_MINUTES, BREAK_COLOR),
}


class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.configure(bg=BG)
        self.root.geometry("420x600")
        self.root.resizable(False, False)

        self.mode = "work"
        self.total_seconds = WORK_MINUTES * 60
        self.remaining_seconds = self.total_seconds
        self.running = False
        self.timer_job = None
        self.completed_sessions = 0

        self._build_ui()
        self._update_display()

    def _build_ui(self):
        title_font = tkfont.Font(family="Arial", size=20, weight="bold")
        mode_font = tkfont.Font(family="Arial", size=14, weight="bold")
        time_font = tkfont.Font(family="Arial", size=42, weight="bold")
        small_font = tkfont.Font(family="Arial", size=11)

        tk.Label(self.root, text="🍅 Pomodoro Timer", font=title_font,
                 bg=BG, fg=ACCENT).pack(pady=(25, 5))

        self.mode_label = tk.Label(
            self.root, text="", font=mode_font, bg=BG, fg=FG)
        self.mode_label.pack(pady=(0, 15))

        # Canvas for the circular progress ring
        self.canvas_size = 260
        self.canvas = tk.Canvas(
            self.root, width=self.canvas_size, height=self.canvas_size,
            bg=BG, highlightthickness=0
        )
        self.canvas.pack()

        pad = 15
        self.arc_bounds = (pad, pad, self.canvas_size -
                           pad, self.canvas_size - pad)
        self.canvas.create_oval(
            *self.arc_bounds, outline=TRACK_COLOR, width=14)
        self.progress_arc = self.canvas.create_arc(
            *self.arc_bounds, start=90, extent=0, style="arc",
            outline=WORK_COLOR, width=14
        )
        self.time_text = self.canvas.create_text(
            self.canvas_size / 2, self.canvas_size / 2,
            text="25:00", font=time_font, fill=FG
        )

        self.session_label = tk.Label(
            self.root, text="Sessions completed: 0", font=small_font, bg=BG, fg=MUTED
        )
        self.session_label.pack(pady=(15, 0))

        # Controls
        btn_frame = tk.Frame(self.root, bg=BG)
        btn_frame.pack(pady=25)

        self.start_button = tk.Button(
            btn_frame, text="Start", command=self.toggle_timer, font=("Arial", 13, "bold"),
            bg=ACCENT, fg="#1e1e2e", relief="flat", padx=25, pady=8, cursor="hand2"
        )
        self.start_button.grid(row=0, column=0, padx=6)

        self.reset_button = tk.Button(
            btn_frame, text="Reset", command=self.reset_timer, font=("Arial", 13),
            bg="#45475a", fg=FG, relief="flat", padx=20, pady=8, cursor="hand2"
        )
        self.reset_button.grid(row=0, column=1, padx=6)

        self.skip_button = tk.Button(
            btn_frame, text="Skip", command=self.skip_phase, font=("Arial", 13),
            bg="#45475a", fg=FG, relief="flat", padx=20, pady=8, cursor="hand2"
        )
        self.skip_button.grid(row=0, column=2, padx=6)

        mode_frame = tk.Frame(self.root, bg=BG)
        mode_frame.pack(pady=(5, 0))

        tk.Label(mode_frame, text="Jump to:", font=small_font, bg=BG, fg=MUTED).grid(
            row=0, column=0, columnspan=3, pady=(0, 8)
        )

        self.mode_buttons = {}
        for i, key in enumerate(MODES):
            label = MODES[key][0]
            b = tk.Button(
                mode_frame, text=label, font=("Arial", 10),
                bg="#313244", fg=FG, relief="flat", padx=12, pady=5, cursor="hand2",
                command=lambda k=key: self.set_mode(k, reset_running=True)
            )
            b.grid(row=1, column=i, padx=4)
            self.mode_buttons[key] = b

        self._highlight_mode_button()

    def set_mode(self, mode, reset_running=False):
        if reset_running:
            self.running = False
            if self.timer_job:
                self.root.after_cancel(self.timer_job)
                self.timer_job = None
            self.start_button.config(text="Start")

        self.mode = mode
        _, minutes, _ = MODES[mode]
        self.total_seconds = minutes * 60
        self.remaining_seconds = self.total_seconds
        self._highlight_mode_button()
        self._update_display()

    def _highlight_mode_button(self):
        for key, btn in self.mode_buttons.items():
            if key == self.mode:
                btn.config(bg=ACCENT, fg="#1e1e2e")
            else:
                btn.config(bg="#313244", fg=FG)

    def toggle_timer(self):
        if self.running:
            self.running = False
            self.start_button.config(text="Start")
            if self.timer_job:
                self.root.after_cancel(self.timer_job)
                self.timer_job = None
        else:
            self.running = True
            self.start_button.config(text="Pause")
            self._tick()

    def reset_timer(self):
        self.running = False
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None
        self.remaining_seconds = self.total_seconds
        self.start_button.config(text="Start")
        self._update_display()

    def skip_phase(self):
        self._advance_phase()

    def _tick(self):
        if not self.running:
            return
        if self.remaining_seconds <= 0:
            self._advance_phase()
            return
        self.remaining_seconds -= 1
        self._update_display()
        self.timer_job = self.root.after(1000, self._tick)

    def _advance_phase(self):
        self.running = False
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None
        self.start_button.config(text="Start")

        if self.mode == "work":
            self.completed_sessions += 1
            self.session_label.config(
                text=f"Sessions completed: {self.completed_sessions}")
            if self.completed_sessions % SESSIONS_BEFORE_LONG_BREAK == 0:
                next_mode = "long_break"
            else:
                next_mode = "short_break"
        else:
            next_mode = "work"

        self.set_mode(next_mode)
        self.root.bell()

    def _update_display(self):
        minutes, seconds = divmod(max(self.remaining_seconds, 0), 60)
        self.canvas.itemconfig(
            self.time_text, text=f"{minutes:02d}:{seconds:02d}")

        label, _, color = MODES[self.mode]
        self.mode_label.config(text=label, fg=color)

        fraction_done = 1 - (self.remaining_seconds /
                             self.total_seconds if self.total_seconds else 0)
        extent = -360 * fraction_done  # clockwise
        self.canvas.itemconfig(self.progress_arc, extent=extent, outline=color)


if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
