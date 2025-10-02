# Lottery Game

A simple console-based lottery game implemented in Python. Players can register (with age verification), top up their balance, and place bets on a lucky number between 10 and 99. The system generates a secure random number, and if it matches, the player wins 10 times their bet. This is a fun, text-based simulation of a lottery experience.

**Note:** Despite the repository name "Lottery Website," this is currently a terminal-based Python application. Future enhancements could include a web interface using frameworks like Flask or Django.

## Features

- **User  Verification:** Checks username length (must be >2 characters) and age (must be >18).
- **Balance Management:** Minimum top-up of $5000; each bet costs at least $1000.
- **Secure Random Generation:** Uses Python's `secrets` module for cryptographically secure random numbers (10-99 range).
- **Game Loop:** Play multiple rounds until balance is insufficient or user quits.
- **Win/Loss Logic:** Match the system number to win 10x the bet; otherwise, lose the bet.
- **Rules Display:** Option to view game rules before playing.

## Requirements

- Python 3.6+ (uses standard library modules: `secrets`, `sys` implicitly via input/output).
- No external dependencies.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/lottery-website.git
   cd lottery-website
   ```

2. Ensure Python is installed and run the script:
   ```
   python lottery_game.py
   ```
   (Rename your main Python file to `lottery_game.py` if needed.)

## How to Play

1. Run the script in your terminal.
2. Choose an option:
   - Enter `1` to read the rules.
   - Enter `2` to start playing.
3. If playing:
   - Enter your username (must be longer than 2 characters).
   - Enter your age (must be over 18).
   - Top up your balance (minimum $5000).
   - In each round:
     - View your current balance.
     - Enter a lucky number (10–99).
     - Enter your bet amount (minimum $1000, cannot exceed balance).
     - The system generates a random number.
     - If it matches, you win! Your balance increases by 10x the bet.
     - If not, you lose the bet.
   - Choose to continue (1) or quit (0) after each round.
4. Game ends when balance < $1000 or you quit. Final balance is displayed.

### Example Gameplay

```
Enter 1 to read rules or 2 to play game:> 2
Enter your name:> Alice
Enter your age:> 25
Welcome, Alice
Top-up money (min 5000):> 6000

Your balance: $ 6000
Enter your lucky number (10–99):> 42
Enter your bet (min 1000):> 1000
System Number is: 42
🎉 You WIN! 🎉
Your balance now: $ 6000

Enter 0 to quit or 1 to continue:> 0
Thanks for playing! Final Balance: $ 6000
```

## Game Rules

- **Age Requirement:** Must be older than 18.
- **Top-Up Minimum:** At least $5000 to start playing.
- **Bet Minimum:** Each play costs at least $1000.
- **Lucky Number Range:** 10–99.
- **Winning:** Exact match with the system's secure random number wins 10x your bet.
- **Losing:** No match means you lose your bet.
- **Balance Check:** Cannot bet more than your current balance. Game pauses if balance < $1000.

