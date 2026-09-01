APP_NAME = "PROcmd"
APP_VERSION = "3.1"
APP_TITLE = f"{APP_NAME} v{APP_VERSION}"

# --- Window geometry ---
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
SPLASH_SECONDS = 10          # graphical loading sequence duration

# --- Fonts (Guaranteed present on Windows 7) ---
FONT_CONSOLE = ("Consolas", 11)
FONT_EDITOR = ("Consolas", 11)
FONT_HEADER = ("Segoe UI", 12, "bold")
FONT_SPLASH = ("Segoe UI", 28, "bold")
FONT_STATUS = ("Segoe UI", 9)

# --- Dark theme ---
COLORS = {
    "bg":        "#1e1e1e",
    "fg":        "#d4d4d4",
    "accent":    "#0a7d32",
    "entry_bg":  "#121212",
    "entry_fg":  "#00e676",
    "tab_bg":    "#2d2d2d",
    "tab_fg":    "#ffffff",
    "status_bg": "#007acc",
    "status_fg": "#ffffff",
    "error":     "#f14c4c",
    "prompt":    "#4fc1ff",
}

# --- Terminal behavior ---
PROMPT_TEXT = "$ "
MAX_HISTORY = 100

def get_setting(key, default=None):
    """Safe lookup for any configuration value."""
    return globals().get(key, default)