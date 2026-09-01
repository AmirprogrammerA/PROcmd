import os
import subprocess
import threading
import queue


class TerminalCore:
    """Executes shell commands on a background thread and streams
    results back through a thread-safe queue."""

    def __init__(self, result_queue):
        self.result_queue = result_queue
        self.cwd = os.getcwd()
        self._busy = threading.Lock()

    def execute(self, command_line):
        """Run a command in a daemon thread; returns immediately."""
        if command_line.strip():
            threading.Thread(target=self._run,
                             args=(command_line,), daemon=True).start()

    def _run(self, command_line):
        with self._busy:
            parts = command_line.split(maxsplit=1)
            head = parts[0].lower() if parts else ""

            # Built-in commands handled natively
            if head == "cd":
                self._handle_cd(parts[1] if len(parts) > 1 else "")
                return
            if head in ("cls", "clear"):
                self._emit(("clear", ""))
                return
            if head == "echo":
                self._emit(("out", parts[1] if len(parts) > 1 else ""))
                return

            try:
                proc = subprocess.Popen(
                    command_line, cwd=self.cwd,
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                    universal_newlines=True, shell=True)
                output, _ = proc.communicate()
                self._emit(("out", output or ""))
                if proc.returncode not in (0, None):
                    self._emit(("err", f"[exit code {proc.returncode}]"))
            except Exception as exc:
                self._emit(("err", f"Error: {exc}"))

    def _handle_cd(self, target):
        target = target.strip('"')
        if not target or target == ".":
            self._emit(("out", self.cwd))
            return
        new_path = os.path.abspath(os.path.join(self.cwd, target))
        if os.path.isdir(new_path):
            self.cwd = new_path
        else:
            self._emit(("err", f"Directory not found: {target}"))

    def _emit(self, message):
        """Thread-safe delivery of a (kind, text) tuple to the UI."""
        self.result_queue.put(message)