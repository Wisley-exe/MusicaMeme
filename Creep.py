import time
from rich.console import Console

console = Console()

def sing_song():
    # Cada item = (texto, tempo_de_espera, cor)
    lines = [
        ("When you were here before,", 5.0, "green"),
        ("couldn't look you in the eye", 5.0, "green"),
        ("You're just like an angel,", 5.0, "green"),
        ("your skin makes me cry", 5.2, "blue"),
        ("You float like a feather", 5.5, "green"),
        ("in a beautiful world", 5.3, "green"),
        ("I wish I was special,", 5.3, "green"),
        ("you're so fuckin' special", 6.3, "green"),
        ("BUT I'M A CREEP,", 5.8, "red"),
        ("I'm a weirdo", 5.8, "red"),
        ("What the hell am I doin' here?", 5.3, "green"),
        ("I don't belong here...", 9.0, "green"),

    ]

    for text, delay, color in lines:
        console.print(text, style=color)
        time.sleep(delay)

if __name__ == "__main__":
    sing_song()
