import tkinter as tk
import random
import json

with open("words.json", "r") as file:
    word_categories = json.load(file)

# Words
words = ['pakistan', 'china', 'russia', 'india', 'iran']

# Game variables
word = random.choice(words)
display = ["_"] * len(word)
attempts = 6
guessed_letters = []

# 🎨 Colors
bg_color = "#1e1e2f"
text_color = "#ffffff"
accent_color = "#4CAF50"
wrong_color = "#ff4d4d"

# 🎯 Guess function
def guess_letter():
    global attempts

    letter = entry.get().lower()
    entry.delete(0, tk.END)
    if len(letter) != 1 or not letter.isalpha():
        result_label.config(text="Enter ONE letter only!", fg="yellow")
        return

    if letter == "":
        result_label.config(text="Enter a letter!", fg="yellow")
        return

    if letter in guessed_letters:
        result_label.config(text="Already guessed!", fg="orange")
        return

    guessed_letters.append(letter)

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                display[i] = letter
        result_label.config(text="Correct!", fg=accent_color)
    else:
        attempts -= 1
        result_label.config(text="Wrong!", fg=wrong_color)

    word_label.config(text=" ".join(display))
    attempts_label.config(text=f"Attempts Left: {attempts}")
    guessed_label.config(text="Guessed: " + ", ".join(guessed_letters))

    if "_" not in display:
        result_label.config(text="🎉 You Win!", fg=accent_color)
        guess_btn.config(state="disabled")

    elif attempts == 0:
        result_label.config(text=f"💀 Game Over! Word: {word}", fg=wrong_color)
        guess_btn.config(state="disabled")

# 🔄 Restart function
def restart_game():
    global word, display, attempts, guessed_letters

    word = random.choice(words)
    display = ["_"] * len(word)
    attempts = 6
    guessed_letters = []

    word_label.config(text=" ".join(display))
    attempts_label.config(text=f"Attempts Left: {attempts}")
    guessed_label.config(text="Guessed: ")
    result_label.config(text="")

    guess_btn.config(state="normal")

# 🖥️ Window
root = tk.Tk()
root.title("Hangman Game 🎮")
root.geometry("500x400")
root.configure(bg=bg_color)

# 🧱 Title
title = tk.Label(root, text="HANGMAN GAME", font=("Helvetica", 22, "bold"),
                 bg=bg_color, fg=accent_color)
title.pack(pady=10)

# 🔤 Word display
word_label = tk.Label(root, text=" ".join(display),
                      font=("Courier", 28, "bold"),
                      bg=bg_color, fg=text_color)
word_label.pack(pady=15)

# ⌨ Input
entry = tk.Entry(root, font=("Arial", 16), justify="center")
entry.pack(pady=5)

# 🎯 Guess button
guess_btn = tk.Button(root, text="Guess",
                      font=("Arial", 12, "bold"),
                      bg=accent_color, fg="white",
                      width=10, command=guess_letter)
guess_btn.pack(pady=10)

# 📊 Attempts
attempts_label = tk.Label(root, text=f"Attempts Left: {attempts}",
                          font=("Arial", 12),
                          bg=bg_color, fg=text_color)
attempts_label.pack()

# 🔠 Guessed letters
guessed_label = tk.Label(root, text="Guessed: ",
                         font=("Arial", 11),
                         bg=bg_color, fg="#cccccc")
guessed_label.pack(pady=5)

# 📢 Result
result_label = tk.Label(root, text="",
                        font=("Arial", 14, "bold"),
                        bg=bg_color)
result_label.pack(pady=10)

# 🔄 Restart button
restart_btn = tk.Button(root, text="Restart",
                        font=("Arial", 12),
                        bg="#2196F3", fg="white",
                        command=restart_game)
restart_btn.pack(pady=10)

# ▶ Run
root.mainloop()