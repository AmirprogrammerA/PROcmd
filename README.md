# PROcmd v3.1
**Professional Modular Terminal for Windows 7**

> Developed by: **amir-93**

---

## Introduction
PROcmd is a lightweight, GUI-based terminal emulator designed specifically for **Windows 7 (32-bit)** systems, powered by Python 3.8. It serves as a modern wrapper for the standard Windows Command Prompt (cmd.exe), offering a modular architecture and a non-blocking interface.

## Key Features
*   **Modular Architecture:** Easy to maintain and expand codebase.
*   **Auto-Elevation:** Automatically requests Administrator privileges on startup.
*   **Non-Blocking UI:** Runs commands in a background thread to prevent UI freezing.
*   **Built-in Editor:** Integrated tool for creating and editing `.bat` files.

## Prerequisites
Before running the application, ensure the following are installed:
1.  **Python 3.8:** Optimized for 32-bit architecture.
2.  **System PATH:** Ensure Python is added to your system PATH during installation.
3.  **Windows 7 (32-bit):** The target environment for this project.

## How to Run
1.  Navigate to the project directory.
2.  Double-click the **`PROcmd.cmd`** launcher.
3.  **Note:** The application uses self-elevation logic. If a Windows UAC (User Account Control) prompt appears, please click **'Yes'** to grant the necessary permissions.

## Project Structure
*   `PROcmd.cmd` : The bootloader script.
*   `main.py` : Entry point and Auto-Elevation logic.
*   `terminal_core.py` : Backend command execution engine.
*   `ui_components.py` : Tkinter GUI interface logic.
*   `editor.py` : Batch (.bat) file editor.
*   `settings.py` : Configuration settings.

---
*Developed by amir-93 | Optimized for legacy Windows 7 systems.*
-----------
============================================================
ترمینال ماژولار PROcmd نسخه 3.1
توسعه‌دهنده: amir-93
هدف: ویندوز 7 (32 بیتی) | پایتون 3.8
============================================================

