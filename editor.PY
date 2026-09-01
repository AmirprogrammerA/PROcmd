import tkinter as tk
from tkinter import filedialog, messagebox

from settings import COLORS, FONT_EDITOR


class BatchEditor(tk.Frame):
    """A tabbed-panel editor for .bat / .cmd scripts."""

    def __init__(self, master, status_callback=None):
        super().__init__(master, bg=COLORS["bg"])
        self.status_callback = status_callback
        self.file_path = None
        self.modified = False

        bar = tk.Frame(self, bg=COLORS["tab_bg"])
        bar.pack(fill=tk.X)
        for label, cmd in (("New", self.new_file), ("Open", self.open_file),
                           ("Save", self.save_file)):
            tk.Button(bar, text=label, command=cmd, bg=COLORS["tab_bg"],
                      fg=COLORS["tab_fg"], relief=tk.FLAT).pack(side=tk.LEFT, padx=2, pady=3)
        self.counter = tk.Label(bar, text="0 chars", bg=COLORS["tab_bg"],
                                fg=COLORS["fg"], font=FONT_EDITOR)
        self.counter.pack(side=tk.RIGHT, padx=8)

        frame = tk.Frame(self, bg=COLORS["bg"])
        frame.pack(fill=tk.BOTH, expand=True)
        self.text = tk.Text(frame, wrap="none", undo=True, relief=tk.FLAT,
                            bg=COLORS["entry_bg"], fg=COLORS["entry_fg"],
                            insertbackground=COLORS["entry_fg"], font=FONT_EDITOR)
        ysb = tk.Scrollbar(frame, command=self.text.yview)
        xsb = tk.Scrollbar(frame, command=self.text.xview, orient=tk.HORIZONTAL)
        self.text.configure(yscrollcommand=ysb.set, xscrollcommand=xsb.set)
        self.text.grid(row=0, column=0, sticky="nsew")
        ysb.grid(row=0, column=1, sticky="ns")
        xsb.grid(row=1, column=0, sticky="ew")
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        self.text.bind("<<Modified>>", self._on_modified)

    def new_file(self):
        if self._confirm_discard():
            self.text.delete("1.0", tk.END)
            self.file_path = None
            self._set_modified(False)

    def open_file(self):
        if not self._confirm_discard():
            return
        path = filedialog.askopenfilename(
            filetypes=[("Batch files", "*.bat *.cmd"), ("All files", "*.*")])
        if path:
            try:
                with open(path, "r", encoding="utf-8", errors="replace") as fh:
                    self.text.delete("1.0", tk.END)
                    self.text.insert("1.0", fh.read())
                self.file_path = path
                self._set_modified(False)
            except OSError as exc:
                messagebox.showerror("Open failed", str(exc))

    def save_file(self):
        path = self.file_path or filedialog.asksaveasfilename(
            defaultextension=".bat", filetypes=[("Batch files", "*.bat")])
        if not path:
            return
        try:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(self.text.get("1.0", tk.END))
            self.file_path = path
            self._set_modified(False)
        except OSError as exc:
            messagebox.showerror("Save failed", str(exc))

    def _confirm_discard(self):
        if self.modified:
            answer = messagebox.askyesnocancel(
                "Unsaved changes", "Save changes before continuing?")
            if answer is None:
                return False
            if answer:
                self.save_file()
                return not self.modified
        return True

    def _on_modified(self, _event=None):
        self.text.edit_modified(False)   # fire once per change
        count = len(self.text.get("1.0", tk.END)) - 1
        self.counter.config(text=f"{count} chars")
        self._set_modified(True)

    def _set_modified(self, value):
        self.modified = value
        if self.status_callback:
            mark = " *" if value else ""
            self.status_callback(f"Editor: {self.file_path or 'untitled.bat'}{mark}")