import time
from rich.console import Console

console = Console()

def sing_song():
    
    lines = [
        ("When you were here before,", 5.0, "green"),
        ("couldn't look you in the eye", 5.0, "green"),
        ("You're just like an angel,", 5.0, "green"),
        ("your skin makes me cry 💧", 5.2, "cyan"),
        ("You float like a feather", 5.3, "green"),
        ("in a beautiful world", 5.3, "green"),
        ("I wish I was special,", 5.2, "yellow"),
        ("you're so fuckin' special", 5.12, "magenta"),
        ("BUT I'M A CREEP,", 4.9, "red"),
        ("I'm a weirdo", 4.9, "red"),
        ("What the hell am I doin' here?", 5.5, "green"),
        ("I don't belong here...", 12.0, "white"),

    ]

    for text, delay, color in lines:
        console.print(text, style=color)
        time.sleep(delay)

if __name__ == "__main__":
    sing_song()
