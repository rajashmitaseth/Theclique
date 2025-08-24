import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Water Safety Checker")
        screen_height = self.winfo_screenheight()
        screen_width = self.winfo_screenwidth()
        window_width = 1600
        window_height = 900
        window_position_left = screen_width//2 - window_width//2
        window_position_top = screen_height//2 - window_height//2
        self.geometry(f'{window_width}x{window_height}+{window_position_left}+{window_position_top}')
        self.minsize(900, 500)

if __name__ == "__main__":
    App().mainloop()