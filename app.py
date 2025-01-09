from flask import Flask, render_template_string
import random

app = Flask(__name__)

def roll_stat():
    """Rolls 4d6 and drops the lowest die."""
    rolls = [random.randint(1, 6) for _ in range(4)]
    rolls.remove(min(rolls))
    return sum(rolls)

def roll_character_stats():
    """Generates six ability scores for a D&D 5e character."""
    return [roll_stat() for _ in range(6)]

def evaluate_stats(stats):
    """Evaluates the stats and gives feedback."""
    total = sum(stats)
    avg_monster_stat = 12 * 6
    if total >= avg_monster_stat:
        return "This would be good! Your character is stronger than a typical D&D monster."
    elif total < avg_monster_stat - 20:
        return "Oh no! Your character might struggle against monsters."
    else:
        return "This character is about average—good enough to go adventuring."

@app.route("/")
def home():
    stats = roll_character_stats()
    feedback = evaluate_stats(stats)
    return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>D&D 5e Character Stat Roller</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin: 50px; }
                button { padding: 10px 20px; font-size: 16px; }
                .stats { font-size: 18px; margin-top: 20px; }
            </style>
        </head>
        <body>
            <h1>D&D 5e Character Stat Roller</h1>
            <p>Click the button below to roll your character stats:</p>
            <button onclick="window.location.reload()">Roll Stats</button>
            <div class="stats">
                <p>Your stats are: {{ stats }}</p>
                <p>{{ feedback }}</p>
            </div>
        </body>
        </html>
    """, stats=", ".join(map(str, stats)), feedback=feedback)

if __name__ == "__main__":
    app.run(debug=True)
