# 🎮 Hangman Game in Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)
![Project](https://img.shields.io/badge/Project-Hangman-green)
![Internship](https://img.shields.io/badge/Internship-CodeAlpha-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Project Overview

The **Hangman Game** is a command-line word-guessing game developed using Python as part of the CodeAlpha Python Programming Internship.

The program randomly selects a secret word from a predefined list. The player must guess the hidden word by entering one letter at a time. The game provides feedback for each guess and ends when the player successfully guesses the word or reaches the maximum number of incorrect guesses.

## ✨ Features

* 🎲 **Random Word Selection:** Selects a secret word randomly from a predefined list.
* 🔤 **Hidden Word Display:** Displays unguessed letters as underscores.
* ✅ **Correct Guess Detection:** Reveals correctly guessed letters.
* ❌ **Incorrect Guess Tracking:** Tracks incorrect guesses.
* 🔁 **Duplicate Guess Prevention:** Prevents letters from being guessed repeatedly.
* 🛡️ **Input Validation:** Rejects invalid inputs, including numbers and multiple characters.
* 🏆 **Win Condition:** Announces success when the player guesses the entire word.
* 💀 **Game-Over Condition:** Ends the game after six incorrect guesses and reveals the secret word.

## 🛠️ Technologies Used

* **Programming Language:** Python 3
* **Module:** Python `random` module
* **Code Editor:** Visual Studio Code
* **Terminal:** PowerShell

## 📂 Project Structure

```text
CodeAlpha_Hangman_Game/
│
├── hangman.py
└── README.md
```

## ⚙️ Requirements

* Python 3 installed on your computer.
* A terminal or command prompt.
* Visual Studio Code or another Python-compatible editor (optional).

No external Python packages are required.

## 🚀 Installation and Execution

### Step 1: Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/NIKHIL21-V/CodeAlpha_Hangman_Game.git
```

### Step 2: Navigate to the Project Folder

```bash
cd CodeAlpha_Hangman_Game
```

### Step 3: Run the Game

```bash
python hangman.py
```

If your system uses the `python3` command, run:

```bash
python3 hangman.py
```

### Step 4: Play the Game

1. The program displays a hidden word.
2. Enter one letter when prompted.
3. The game reveals correctly guessed letters.
4. Incorrect guesses increase the error count.
5. You win by guessing all the letters before reaching six incorrect guesses.

## 🎯 Example Gameplay

```text
===== WELCOME TO HANGMAN =====
Guess the hidden word one letter at a time!
You have 6 incorrect guesses.

Word: _ _ _ _ _ _
Incorrect guesses: 0 / 6
Enter a letter: o
Correct guess!

Word: _ o _ _ _ _
Incorrect guesses: 0 / 6
Enter a letter: p
Wrong guess!
```

*Note: The secret word and gameplay output vary because the program selects a word randomly.*

## 🧠 Concepts Demonstrated

This project demonstrates the practical application of fundamental Python programming concepts:

* Variables and data types
* Lists
* Random selection
* `while` loops and `for` loops
* Conditional statements (`if`, `else`)
* User input and output
* String manipulation
* Input validation
* Membership testing
* Game logic and control flow

## 📚 Learning Outcomes

Through this project, I practiced:

* Developing an interactive Python application.
* Implementing logical conditions and loops.
* Handling user input and invalid entries.
* Tracking game state and user progress.
* Organizing a simple software project.
* Using Git and GitHub for version control and project sharing.

## 🔮 Future Improvements

Potential enhancements include:

* Adding difficulty levels.
* Introducing hints for difficult words.
* Displaying visual stages of the hangman.
* Organizing words into different categories.
* Tracking scores and consecutive wins.
* Creating a graphical user interface.
* Adding automated tests.

## 👨‍💻 Internship Information

**Program:** CodeAlpha Python Programming Internship
**Project:** Task 1 — Hangman Game
**Domain:** Python Programming

## 👤 Author

**NIKHIL21-V**

GitHub: [NIKHIL21-V](https://github.com/NIKHIL21-V)

## 📄 License

This project is available for educational and portfolio purposes. A formal open-source license can be added if the project is intended for redistribution.

---

⭐ If you find this project interesting, feel free to explore the repository and its source code.
