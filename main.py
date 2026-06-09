#Import some requried libraries
import tkinter as tk
import random
import json


with open("words.json", "r") as file:
    word_categories = json.load(file)


# Game variables
category = random.choice(list(word_categories.keys()))
word = random.choice(word_categories[category])
current_category = category

display = ["_"] * len(word)
attempts = 6
guessed_letters = []

hint_count = 0

def show_hint():
    global hint_count

    if hint_count == 0:
        result_label.config(text=f"Hint: First letter of the word is '{word[0]}'", fg="yellow")

    elif hint_count == 1:
        if len(word) > 1:
            result_label.config(text=f"Hint: Second letter of the word is '{word[1]}'", fg="yellow")
        else:
            result_label.config(text="Hint not available", fg="orange")

    elif hint_count == 2:
        if len(word) > 2:
            result_label.config(text=f"Hint: Third letter of the word is '{word[2]}'", fg="yellow")
        else:
            result_label.config(text="Hint not available", fg="orange")

    elif hint_count == 3:
        if len(word) > 3:
            result_label.config(text=f"Hint: Fourth letter of the word is '{word[3]}'", fg="yellow")
        else:
            result_label.config(text="Hint not available", fg="orange")
            

    else:
        result_label.config(text="No hints left!", fg="orange")
        hint_btn.config(state="disabled")
        return

    hint_count += 1

# These colors are in used
bg_color = "#0f172a"      # navy 
card_color = "#1e293b"    # light navy
text_color = "#e2e8f0"    # white 
accent_color = "#22c55e"  # green
wrong_color = "#ef4444"   # red
highlight_color = "#38bdf8"  # sky blue

# Guess function
def guess_letter():
    global attempts

    letter = entry.get().lower()
    entry.delete(0, tk.END)
    if len(letter) != 1 or not letter.isalpha():
        result_label.config(text="Enter ONE letter only!", fg="yellow")
        return

    # if letter == "":
    #     result_label.config(text="Enter a letter!", fg="yellow")
    #     return

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
        hint_btn.config(state="disabled")

    elif attempts == 0:
        result_label.config(text=f"💀 Game Over! Word: {word}", fg=wrong_color)
        guess_btn.config(state="disabled")
        hint_btn.config(state="disabled")

# Restart function
def restart_game():
    global word, display, attempts, guessed_letters, hint_count, current_category, category
    category = random.choice(list(word_categories.keys()))
    word = random.choice(word_categories[category])
    current_category = category

    display = ["_"] * len(word)
    attempts = 6
    guessed_letters = []
    hint_count = 0

    word_label.config(text=" ".join(display))
    attempts_label.config(text=f"Attempts Left: {attempts}")
    guessed_label.config(text="Guessed: ")
    result_label.config(text="")

    guess_btn.config(state="normal")
    hint_btn.config(state="normal")
    category_label.config(text=f"Category: {current_category}")

# Window
root = tk.Tk()
root.title("Word Guessing Game 🎮")
root.geometry("500x430")
root.configure(bg=bg_color)

# Title
title = tk.Label(root, text="Word Guessing Game", font=("Helvetica", 22, "bold"),
                 bg=bg_color, fg=accent_color)
title.pack(pady=10)

# Word display
word_label = tk.Label(root, text=" ".join(display),
                      font=("Courier", 28, "bold"),
                      bg=bg_color, fg=text_color)
word_label.pack(pady=10)

# Input Feild
entry = tk.Entry(root, font=("Arial", 14), justify="center", )
entry.pack(pady=5)

# placeholder_text = "Enter the guess..."
# entry.insert(0, placeholder_text)
# entry.config(fg="grey")

# Guess button
guess_btn = tk.Button(root, text="Guess Letter",
                      font=("Arial", 12, "bold"),
                      bg=accent_color, fg="white",
                      width=10, command=guess_letter, relief="flat")   # remove sharp border
guess_btn.pack(pady=10)

hint_btn = tk.Button(root, text="Check Hint",
                     font=("Arial", 12),
                     bg="#FFC107", fg="black",
                     command=show_hint)
hint_btn.pack(pady=5)

category_label = tk.Label(root, text=f"Category: {current_category}",
                          bg=bg_color, fg=highlight_color)
category_label.pack()

#  Total Remaining Attempts
attempts_label = tk.Label(root, text=f"Attempts Left: {attempts}",
                          font=("Arial", 12),
                          bg=bg_color, fg=text_color)
attempts_label.pack()

# Guessed letters
guessed_label = tk.Label(root, text="Already Guessed Letters: ",
                         font=("Arial", 11),
                         bg=bg_color, fg="#cccccc")
guessed_label.pack(pady=5)

# Result
result_label = tk.Label(root, text="",
                        font=("Arial", 14, "bold"),
                        bg=bg_color)
result_label.pack(pady=5)

# Restart button
restart_btn = tk.Button(root, text="Restart",
                        font=("Arial", 12),
                        bg="#2196F3", fg="white",
                        command=restart_game)
restart_btn.pack(pady=10)

# ▶ Run
root.mainloop()