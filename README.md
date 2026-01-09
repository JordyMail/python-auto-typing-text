# python-auto-typing-text

A Python program designed to type paragraphs automatically, character by character. It mimics manual human typing by incorporating natural speed variations and patterns.

## Prerequisites

Before running the program, ensure your system meets the following requirements:

* **Python:** Version 3.6 or later.
* **Library:** `pyautogui`

Check your Python version:

```bash
python --version

```

## Installation

1. **Clone the Repository**
```bash
git clone [repository-url]
cd [repository-name]

```


2. **Install Required Module**
```bash
pip install pyautogui

```


3. **Manual Setup (Optional)**
Copy the `type_paragraph.py` file to your desired directory and prepare a text file if you intend to use the file-reading feature.

---

## How to Use

### Interactive Mode (Recommended)

Run the following command in your terminal:

```bash
python type_paragraph.py

```

**Steps within the program:**

1. **Select Text Source:**
* Option 1: Manual keyboard input (press Enter twice to finish).
* Option 2: Read from a text file (enter the filename, e.g., `text.txt`).


2. **Select Speed:**
Choose between Slow, Medium, or Fast typing modes.
3. **Set Repetitions:**
Specify how many times the text should be typed (default is 1).
4. **Prepare Target Application:**
The program will provide a 5-second countdown. Switch immediately to your target application (e.g., Notepad, Browser, or a chat app).

---

## Speed Configuration

| Mode | Min Delay | Max Delay | Error Chance | Description |
| --- | --- | --- | --- | --- |
| **Slow** | 0.05s | 0.25s | 2% | Mimics a beginner's manual typing |
| **Medium** | 0.03s | 0.15s | 1% | Standard typing speed |
| **Fast** | 0.01s | 0.08s | 0.5% | Rapid yet remains natural |

---

## Safety Guidelines

### Before Running

* Ensure the cursor is active in the target application.
* Back up any important data in the target application.
* Close unnecessary applications.
* Save any ongoing work.

### During the Process

* Monitor the typing process to ensure accuracy.
* Do not touch the mouse or keyboard while the program is active.
* **Emergency Stop:** Press `Ctrl+C` in the terminal to stop the program immediately.

---

## Troubleshooting

| Issue | Cause | Solution |
| --- | --- | --- |
| ModuleNotFoundError | Module not installed | Run `pip install pyautogui` |
| Program is not typing | Inactive cursor | Click on the input area of the target app |
| Strange characters appear | Incorrect keyboard layout | Ensure keyboard layout is set to EN/US |
| File cannot be loaded | File not found | Ensure the text file is in the same folder |

---

## Practical Usage Examples

**1. Sending Long Messages (WhatsApp/Telegram)**

* Select: File Mode (2)
* File: `message.txt`
* Speed: Medium (2)

**2. Filling Recurring Forms**

* Select: Keyboard Mode (1)
* Speed: Fast (3)
* Repeat: 10

---

Would you like me to add a section for "Environment Variables" or perhaps a more detailed "Technical Specifications" section?
