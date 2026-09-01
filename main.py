# admin check
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    # این کد باعث می‌شود ویندوز دوباره برنامه را با دسترسی Admin باز کند
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit() # برنامه فعلی را می‌بندد تا نسخه ادمین باز شود
# -------



import tkinter as tk

from settings import (APP_NAME, APP_VERSION, SPLASH_SECONDS,
                      COLORS, FONT_SPLASH, FONT_STATUS)
from ui_components import MainWindow


class SplashScreen(tk.Tk):
    """Graphical loading sequence with a smooth progress bar."""

    def __init__(self, seconds=SPLASH_SECONDS):
        super().__init__()
        self.overrideredirect(True)
        w, h = 480, 220
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry(f"{w}x{h}+{(sw - w) // 2}+{(sh - h) // 2}")
        self.configure(bg=COLORS["bg"])

        tk.Label(self, text=APP_NAME, bg=COLORS["bg"],
                 fg=COLORS["entry_fg"], font=FONT_SPLASH).pack(pady=(45, 0))
        tk.Label(self, text=f"Version {APP_VERSION} - loading modules...",
                 bg=COLORS["bg"], fg=COLORS["fg"],
                 font=FONT_STATUS).pack(pady=(2, 18))

        self.bar = tk.Canvas(self, width=360, height=14, bg=COLORS["entry_bg"],
                             highlightthickness=0)
        self.bar.pack()
        self.fill = self.bar.create_rectangle(0, 0, 0, 14,
                                              fill=COLORS["accent"], width=0)

        self._steps = 100
        self._interval = int(seconds * 1000 / self._steps)
        self._step = 0
        self.after(self._interval, self._advance)

    def _advance(self):
        self._step += 1
        width = int(360 * self._step / self._steps)
        self.bar.coords(self.fill, 0, 0, width, 14)
        if self._step < self._steps:
            self.after(self._interval, self._advance)
        else:
            self.destroy()
            self._launch()

    def _launch(self):
        MainWindow().mainloop()


def main():
    SplashScreen().mainloop()


if __name__ == "__main__":
    main()