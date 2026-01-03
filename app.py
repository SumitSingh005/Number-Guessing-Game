from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Required for sessions


def reset_game():
    session["number"] = random.randint(1, 50)
    session["attempts"] = 3


@app.route("/", methods=["GET", "POST"])
def home():

    # Initialize game if not started
    if "number" not in session:
        reset_game()

    message = ""

    if request.method == "POST":

        # Validate input
        guess_value = request.form.get("guess", "").strip()

        if not guess_value.isdigit():
            message = "Please enter a valid number."
            return render_template("index.html",
                                   message=message,
                                   attempts=session["attempts"])

        guess = int(guess_value)

        # Use existing attempts
        session["attempts"] -= 1

        if guess == session["number"]:
            message = "Very Good! You guessed the correct number!"
            reset_game()

        else:
            if guess < session["number"]:
                message = "Too low! Try again."
            else:
                message = "Too high! Try again."

            # Game Over
            if session["attempts"] == 0:
                message = f"Game Over! The correct number was {session['number']}."
                reset_game()

    return render_template("index.html",
                           message=message,
                           attempts=session["attempts"])


if __name__ == "__main__":
    app.run(debug=True)
