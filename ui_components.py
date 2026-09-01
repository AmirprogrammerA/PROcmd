import queue
import tkinter as tk
from tkinter import ttk

from settings import APP_TITLE, COLORS, FONT_CONSOLE, FONT_HEADER, FONT_STATUS
from terminal_core import TerminalCore
from editor import BatchEditor


class MainWindow(tk.Tk):
    """Top-level application window with tabbed terminal and editor."""

    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry("900x600")
        self.configure(bg=COLORS["bg"])
        self._style_widgets()

        self.result_queue = queue.Queue()
        self.core = TerminalCore(self.result_queue)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=6, pady=6)

        self._build_terminal_tab()
        self._build_editor_tab()
        self._build_status_bar()
        self.after(100, self._poll_queue)

    def _style_widgets(self):
        style = ttk.Style(self)
        style.theme_use("clam")          # consistent look on Windows 7
        style.configure("TNotebook", background=COLORS["bg"], borderwidth=0)
        style.configure("TNotebook.Tab", background=COLORS["tab_bg"],
                        foreground=COLORS["tab_fg"], font=FONT_HEADER, padding=(14, 6))
        style.map("TNotebook.Tab", background=[("selected", COLORS["accent"])])

    def _build_terminal_tab(self):
        tab = tk.Frame(self.notebook, bg=COLORS["bg"])
        self.notebook.add(tab, text=" Terminal ")
        self.output = tk.Text(tab, height=20, state=tk.DISABLED, wrap="word",
                              relief=tk.FLAT, bg=COLORS["entry_bg"],
                              fg=COLORS["entry_fg"], font=FONT_CONSOLE)
        scroll = tk.Scrollbar(tab, command=self.output.yview)
        self.output.configure(yscrollcommand=scroll.set)
        self.output.pack(fill=tk.BOTH, expand=True, padx=4, pady=(4, 0))
        self.output.tag_configure("err", foreground=COLORS["error"])
        self.output.tag_configure("prompt", foreground=COLORS["prompt"])

        entry_row = tk.Frame(tab, bg=COLORS["bg"])
        entry_row.pack(fill=tk.X, padx=4, pady=4)
        tk.Label(entry_row, text="$", bg=COLORS["bg"], fg=COLORS["prompt"],
                 font=FONT_CONSOLE).pack(side=tk.LEFT)
        self.entry = tk.Entry(entry_row, bg=COLORS["entry_bg"],
                              fg=COLORS["entry_fg"], relief=tk.FLAT,
                              insertbackground=COLORS["entry_fg"], font=FONT_CONSOLE)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=6)
        self.entry.bind("<Return>", self._on_enter)
        self.entry.focus_set()

    def _build_editor_tab(self):
        self.editor = BatchEditor(self.notebook, status_callback=self.set_status)
        self.notebook.add(self.editor, text=" Batch Editor ")

    def _build_status_bar(self):
        self.status = tk.Label(self, text="Ready", anchor="w",
                               bg=COLORS["status_bg"], fg=COLORS["status_fg"],
                               font=FONT_STATUS, padx=8, pady=3)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    def set_status(self, text):
        self.status.config(text=text)

    def _on_enter(self, _event=None):
        command = self.entry.get().strip()
        if command:
            self.entry.delete(0, tk.END)
            self._append("prompt", f"$ {command}\n")
            self.core.execute(command)

    def _poll_queue(self):
        """Drain worker-thread results without blocking the UI."""
        try:
            while True:
                kind, text = self.result_queue.get_nowait()
                if kind == "clear":
                    self.output.config(state=tk.NORMAL)
                    self.output.delete("1.0", tk.END)
                    self.output.config(state=tk.DISABLED)
                else:
                    self._append(kind, text)
        except queue.Empty:
            pass
        self.after(100, self._poll_queue)

    def _append(self, tag, text):
        self.output.config(state=tk.NORMAL)
        self.output.insert(tk.END, text, tag if tag in ("err", "prompt") else None)
        self.output.see(tk.END)
        self.output.config(state=tk.DISABLED)