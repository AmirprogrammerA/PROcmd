![Version](https://img.shields.io/badge/Version-3.1-blue)
![OS](https://img.shields.io/badge/OS-Windows%207%20(32--bit)-orange)
![Python](https://img.shields.io/badge/Python-3.8-green)

# PROcmd v3.1
**Professional Modular Terminal for Windows 7**
PROcmd website:

https://amirprogrammera.github.io/PROcmd/

> Developed by: **amir-93**
Developed & Tested natively on Windows 7 32-bit hardware.”
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
# PROcmd v3.1

![Version](https://img.shields.io/badge/Version-3.1-blue)
![OS](https://img.shields.io/badge/OS-Windows%207%20(32--bit)-orange)
![Python](https://img.shields.io/badge/Python-3.8-green)

Professional modular terminal emulator for Windows 7 (32-bit).

---

## 🇮🇷 Persian Documentation (مستندات فارسی)

### معرفی
پروژه **PROcmd** یک شبیه‌ساز ترمینال گرافیکی سبک است که به صورت اختصاصی برای محیط ویندوز 7 (32 بیتی) توسعه یافته است. این برنامه به عنوان یک رابط کاربری مدرن روی هسته `cmd.exe` عمل می‌کند و قابلیت‌های مدیریت دستورات را به شکلی بهینه ارائه می‌دهد.

### ویژگی‌های کلیدی
- **معماری ماژولار:** ساختار تمیز و قابل توسعه برای افزودن قابلیت‌های جدید.
- **دسترسی خودکار ادمین:** درخواست خودکار سطح دسترسی مدیریت (UAC) در زمان اجرا.
- **رابط کاربری غیرمسدود (Non-blocking):** اجرای دستورات در پس‌زمینه بدون هنگ کردن پنجره برنامه.
- **ویرایشگر فایل‌های بچ:** ابزار داخلی برای مدیریت و ویرایش فایل‌های `.bat`.

### پیش‌نیازها
1. پایتون 3.8 (بهینه برای معماری 32 بیتی).
2. فعال بودن گزینه **Add to PATH** در زمان نصب پایتون.
3. سیستم عامل ویندوز 7 (32 بیتی).

### راهنمای اجرا
1. به پوشه پروژه بروید.
2. روی فایل `PROcmd.cmd` دبل‌کلیک کنید.
3. **نکته مهم:** برنامه به صورت خودکار دسترسی ادمین را درخواست می‌کند. در صورت باز شدن پنجره UAC ویندوز، حتماً گزینه **'Yes'** را انتخاب کنید.

---

## 📂 Project Structure (ساختار پروژه)
```text
PROcmd/
├── PROcmd.cmd        # فایل بوت‌لودر برای اجرای سریع
├── main.py           # هسته اصلی و مدیریت دسترسی‌های سیستمی
├── terminal_core.py  # موتور اجرای دستورات (subprocess)
├── ui_components.py  # لایه گرافیکی برنامه (Tkinter)
├── editor.py         # بخش ویرایشگر فایل‌های بچ
└── settings.py       # تنظیمات پیکربندی
