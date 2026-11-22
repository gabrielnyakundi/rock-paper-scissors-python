
import tkinter as tk
import random
player_score = 0
computer_score = 0
ties = 0

round_number = 0
max_rounds = 5  # Set the maximum number of rounds to play

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("800x700")
root.configure(bg="#151525")

game_frame = tk.Frame(
    root,
    bg="#151525"
)
round_label = tk.Label(
    game_frame,
    text=f"Round: 0 / {max_rounds}",
    font=("Arial", 14, "bold"),
    fg="#E2E8F0",
    bg="#151525"
)
round_label.pack(pady=5)

game_label = tk.Label(
    game_frame,
    text="",
    font=("Arial", 22, "bold"),
    fg="#FB7185",
    bg="#151525"
)
game_label.pack(pady=5)

menu_frame = tk.Frame(
    root,
    bg="#151525"
)
title_label = tk.Label(
    menu_frame,
    text="ROCK PAPER SCISSORS",
    font=("Arial", 24, "bold"),
    fg="#FBBF24",
    bg="#151525"
)
title_label.pack(pady=30)

welcome_label = tk.Label(
    menu_frame,
    text="Welcome! Ready to challenge the computer?",
    font=("Arial", 12),
    fg="white",
    bg="#151525"
)
welcome_label.pack(pady=10)

def add_hover_effect(button, hover_color):
    original_color = button["bg"]

    button.bind("<Enter>", lambda event: button.config(bg=hover_color))
    button.bind("<Leave>", lambda event: button.config(bg=original_color))


def show_rules():
    rules_window = tk.Toplevel(root)
    rules_window.title("How to Play")
    rules_window.geometry("450x350")
    rules_window.configure(bg="#1E1E2F")

    rules_title = tk.Label(
        rules_window,
        text="HOW TO PLAY",
        font=("Arial", 18, "bold"),
        fg="#F1C40F",
        bg="#1E1E2F"
    )
    rules_title.pack(pady=20)

    rules_text = tk.Label(
        rules_window,
        text="Rock beats Scissors\n"
              "Scissors beats Paper\n"
              "Paper beats Rock\n\n"
              "Choose your move and try to beat the computer!",
        font=("Arial", 12),
        fg="white",
        bg="#1E1E2F",
        justify="center"
    )
    rules_text.pack(pady=15)

    close_button = tk.Button(
        rules_window,
        text="Close",
        font=("Arial", 11, "bold"),
        width=15,
        bg="#E74C3C",
        fg="white",
        cursor="hand2",
        command=rules_window.destroy
    )
    close_button.pack(pady=15)
def start_countdown(player_choice):
    outcome_label.config(text="READY...", fg="#A78BFA")

    rock_button.config(state="disabled")
    paper_button.config(state="disabled")
    scissors_button.config(state="disabled")

    root.after(500, lambda: outcome_label.config(text="SET...", fg="#FBBF24"))

    root.after(1000, lambda: finish_countdown(player_choice))


def finish_countdown(player_choice):
    outcome_label.config(text="GO!", fg="#34D399")

    root.after(300, lambda: play_round(player_choice))
def restart_game():
    global player_score, computer_score, ties, round_number

    player_score = 0
    computer_score = 0
    ties = 0
    round_number = 0

    score_label.config(
        text="Player: 0     Computer: 0     Ties: 0"
    )

    round_label.config(
        text=f"Round: 0 / {max_rounds}"
    )
    player_choice_label.config(text="❔")
    player_move_label.config(text="WAITING")

    computer_choice_label.config(text="❔")
    computer_move_label.config(text="WAITING")

    outcome_label.config(text="")
    final_result_label.config(text="")

    game_label.config(text="")
    restart_button.pack_forget()

    rock_button.config(state="normal")
    paper_button.config(state="normal")
    scissors_button.config(state="normal")
    
def play_round(player_choice):
    global player_score, computer_score, ties, round_number

    choices = ("r", "p", "s")
    emojis = {"r": "✊", "p": "✋", "s": "✌"}

    computer_choice = random.choice(choices)
    round_number += 1

    round_label.config(text=f"Round: {round_number} / {max_rounds}")

    player_choice_label.config(
    text=emojis[player_choice]
)

    player_move_label.config(
        text=player_choice.upper() == "R" and "ROCK" or
        player_choice.upper() == "P" and "PAPER" or "SCISSORS"
)
    computer_choice_label.config(
    text=emojis[computer_choice]
)

    computer_move_label.config(
        text=computer_choice.upper() == "R" and "ROCK" or
            computer_choice.upper() == "P" and "PAPER" or "SCISSORS"
)


    if player_choice == computer_choice:
        outcome = "IT'S A TIE!"
        ties += 1

    elif (
        (player_choice == "r" and computer_choice == "s") or
        (player_choice == "p" and computer_choice == "r") or
        (player_choice == "s" and computer_choice == "p")
    ):
        outcome = "YOU WIN!"
        player_score += 1

    else:
        outcome = "YOU LOSE!"
        computer_score += 1

    if round_number < max_rounds:
        if outcome == "YOU WIN!":
            outcome_label.config(text=outcome, fg="#34D399")

        elif outcome == "YOU LOSE!":
            outcome_label.config(text=outcome, fg="#EF4444")

        else:
            outcome_label.config(text=outcome, fg="#FBBF24")

    else:
        outcome_label.config(text="")

    score_label.config(
        text=f"Player: {player_score}     Computer: {computer_score}     Ties: {ties}"
)
    
    if round_number >= max_rounds:
        game_label.config(text="GAME OVER!", fg="#FB7185")

        rock_button.config(state="disabled")
        paper_button.config(state="disabled")
        scissors_button.config(state="disabled")

        if player_score > computer_score:
            final_message = "YOU ARE THE WINNER!"
            final_result_label.config(fg="#34D399")

        elif computer_score > player_score:
            final_message = "COMPUTER WINS!"
            final_result_label.config(fg="#EF4444")

        else:
            final_message = "IT'S AN OVERALL TIE!"

        final_result_label.config(
            text=f"{final_message}"
                 
        )

        restart_button.pack(pady=15)

    else:
        rock_button.config(state="normal")
        paper_button.config(state="normal")
        scissors_button.config(state="normal")

def start_game():
    title_label.pack_forget()
    welcome_label.pack_forget()
    menu_frame.pack_forget()

    game_frame.pack(pady=20)

result_frame = tk.Frame(
    game_frame,
    bg="#151525"
)
result_frame.pack(pady=20)   
# PLAYER CARD
player_card = tk.Frame(
    result_frame,
    bg="#252541",
    padx=25,
    pady=15,
    width=220
)
player_card.pack(side="left", padx=15)


player_title = tk.Label(
    player_card,
    text="YOU",
    font=("Arial", 12, "bold"),
    fg="#CBD5E1",
    bg="#252541"
)
player_title.pack(pady=5)


player_choice_label = tk.Label(
    player_card,
    text="❔",
    font=("Arial", 35),
    fg="white",
    bg="#252541"
)
player_choice_label.pack(pady=5)


player_move_label = tk.Label(
    player_card,
    text="WAITING",
    font=("Arial", 11, "bold"),
    fg="#34D399",
    bg="#252541",
)
player_move_label.pack(pady=5)

computer_card = tk.Frame(
    result_frame,
    bg="#252541",
    padx=25,
    pady=15,
    width=220
)
computer_card.pack(side="left", padx=15)


computer_title = tk.Label(
    computer_card,
    text="COMPUTER",
    font=("Arial", 12, "bold"),
    fg="#CBD5E1",
    bg="#252541"
)
computer_title.pack(pady=5)


computer_choice_label = tk.Label(
    computer_card,
    text="❔",
    font=("Arial", 35),
    fg="white",
    bg="#252541"
)
computer_choice_label.pack(pady=5)


computer_move_label = tk.Label(
    computer_card,
    text="WAITING",
    font=("Arial", 11, "bold"),
    fg="#FBBF24",
    bg="#252541"
)
computer_move_label.pack(pady=5)

outcome_label = tk.Label(
    game_frame,
    text="",
    font=("Arial", 24, "bold"),
    fg="#34D399",
    bg="#151525"
)
outcome_label.pack(pady=4)

score_label = tk.Label(
    game_frame,
    text="Player: 0     Computer: 0     Ties: 0",
    font=("Arial", 14, "bold"),
    fg="#E2E8F0",
    bg="#252541",
    padx=10,
    pady=6
)
score_label.pack(pady=5)

final_result_label = tk.Label(
    game_frame,
    text="",
    font=("Arial", 19, "bold"),
    fg="#FDE68A",
    bg="#252541",
    justify="center",
    padx=20,
    pady=12
)
final_result_label.pack(pady=8
                        )

rock_button = tk.Button(
    game_frame,
    text="✊ ROCK",
    font=("Arial", 13, "bold"),
    width=18,
    bg="#EF4444",
    fg="white",
    activebackground="#DC2626",
    activeforeground="white",
    cursor="hand2",
    relief="raised",
    command=lambda: start_countdown("r")
)
rock_button.pack(pady=3, ipady=3)
add_hover_effect(rock_button, "#DC2626")


paper_button = tk.Button(
    game_frame,
    text="✋ PAPER",
    font=("Arial", 13, "bold"),
    width=18,
    bg="#3B82F6",
    fg="white",
    activebackground="#2563EB",
    activeforeground="white",
    cursor="hand2",
    relief="flat",
    command=lambda: start_countdown("p")
)
paper_button.pack(pady=3, ipady=3)
add_hover_effect(paper_button, "#2563EB")


scissors_button = tk.Button(
    game_frame,
    text="✌ SCISSORS",
    font=("Arial", 13, "bold"),
    width=18,
    bg="#F59E0B",
    fg="white",
    activebackground="#D97706",
    activeforeground="white",
    cursor="hand2",
    relief="flat",
    command=lambda: start_countdown("s")

)
scissors_button.pack(pady=3, ipady=3)
add_hover_effect(scissors_button, "#D97706")

restart_button =tk.Button(
    game_frame,
    text="PLAY AGAIN",
    font=("Arial", 12, "bold"),
    width=15,
    bg="#10B981",
    fg="white",
    activebackground="#059669",
    activeforeground="white",
    cursor="hand2",
    command=restart_game
)
add_hover_effect(restart_button, "#059669")

start_button = tk.Button(
    menu_frame,
    text="Start Game",
    font=("Arial", 12, "bold"),
    width=20,
    bg="#4CAF50",
    fg="#ffffff",
    cursor="hand2",
    command=start_game
)
start_button.pack(pady=10)

how_to_play_button = tk.Button(
    menu_frame,
    text="How to Play",
    font=("Arial", 12, "bold"),
    width=20,
    bg="#3498DB",
    fg="#ffffff",
    cursor="hand2",
    command=show_rules
)
how_to_play_button.pack(pady=10)

exit_button = tk.Button(
    menu_frame,
    text="Exit Game",
    font=("Arial", 12, "bold"),
    width=20,
    bg="#E74C3C",
    fg="#ffffff",
    cursor="hand2",
    command=root.destroy
)
exit_button.pack(pady=10)

menu_frame.pack(pady=20)

root.mainloop()
