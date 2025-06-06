# Guess the Number Game

A simple number guessing game built with Python's `tkinter` library. Players select a difficulty level (Easy, Medium, or Hard) and try to guess a randomly generated number within the chosen range. Visual feedback (arrows or a correct sign) and a color-changing try counter enhance the experience.

## Features
- **Difficulty Levels**:
  - Easy: 0–50
  - Medium: 0–100
  - Hard: 0–200
- **Visual Feedback**: Displays images to indicate if the guess is too high, too low, or correct.
- **Try Counter**: Tracks attempts with color changes:
  - White: 0 tries
  - Green: 1–4 tries
  - Yellow: 5–10 tries
  - Red: 10+ tries
- **User Interface**: Built with `tkinter`, featuring buttons, radio buttons, an entry field, and labels.
- **Resource Path Handling**: Supports standalone executables via PyInstaller for image loading.

## Screenshots
![Game Interface](screenshots/game_screenshot.png)

## Prerequisites
- Python 3.x
- `tkinter` (included with standard Python installations)
- Image files: `uparrow.png`, `downarrow.png`, `correct.png`, `dice.png` (included in the repository)
