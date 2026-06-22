# WaterFast.Exe

A fun desktop application that creates water splashing effects on your screen!

## Features

🌊 **Water Splash Effect** - Creates infinite water splash animations across your screen
⚠️ **Safety Warnings** - Double confirmation dialogs before launching
💫 **Random Splashes** - Each splash appears at random locations with random sizes

## Downloads

### Latest Release
- **[Download WaterFast.Exe (Windows)](https://github.com/ballercookie607-glitch/WaterFast.Exe/releases)** - Standalone executable
- **[Download Source Code](https://github.com/ballercookie607-glitch/WaterFast.Exe/archive/refs/heads/main.zip)** - Python source files

### Requirements
- Windows 7 or later
- No installation needed - just run the .exe file!

## How to Use

### Option 1: Run the Python Script
```bash
python WaterFast.exe.py
```

### Option 2: Create an Executable

To convert this to a standalone `.exe` file on Windows, use PyInstaller:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed WaterFast.exe.py
```

The executable will be created in the `dist/` folder.

## Warnings

⚠️ When you launch the app, you'll see TWO warnings:
1. **First Warning**: "Are you sure you wanna run this app?"
2. **Final Warning**: "THIS IS YOUR LAST WARNING DO NOT OPEN IT"

Click "Yes" on both to start the water splash effect!

## How It Works

- Water splashes appear randomly across all Windows (not websites)
- Each splash is a blue animated window with circular water effects
- Splashes appear infinitely until you close all windows or force quit the application
- Each splash auto-closes after a random duration (0.5-2 seconds)

## System Requirements

- Python 3.6+
- tkinter (usually included with Python)
- Windows/Linux/macOS

## Warning

This is a fun proof-of-concept application. Be aware that:
- It creates many windows on your screen
- You may need to force-quit (Alt+F4 or Task Manager) to stop it
- Use at your own risk!
