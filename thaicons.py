import tkinter as tk
import random

# List of Thai consonants with their names
consonants = [
    ("ก", "gor kai"),
    ("ข", "khor khai"),
    ("ฃ", "khor khuat"),
    ("ค", "khor khon"),
    ("ฅ", "khor ra khang"),
    ("ฆ", "khor khon"),
    ("ง", "ngor ngu"),
    ("จ", "jor jan"),
    ("ฉ", "chor ching"),
    ("ช", "chor chang"),
    ("ซ", "sor so"),
    ("ฌ", "chor chao"),
    ("ญ", "yor ying"),
    ("ฎ", "dor chada"),
    ("ฏ", "tor phut"),
    ("ฐ", "thor than"),
    ("ฑ", "thor thung"),
    ("ฒ", "nor nen"),
    ("ณ", "nor nu"),
    ("ด", "dor dek"),
    ("ต", "tor tao"),
    ("ถ", "thor thang"),
    ("ท", "thor thong"),
    ("ธ", "thor thung"),
    ("น", "nor nu"),
    ("บ", "bor baimai"),
    ("ป", "por pla"),
    ("ผ", "phor phung"),
    ("ฝ", "for fang"),
    ("พ", "phor phak"),
    ("ฟ", "for fa"),
    ("ภ", "phor samphao"),
    ("ม", "mor ma"),
    ("ย", "yor yak"),
    ("ร", "ror rua"),
    ("ล", "lor ling"),
    ("ว", "wor waen"),
    ("ศ", "sor sala"),
    ("ษ", "sor rishi"),
    ("ส", "sor sua"),
    ("ห", "hor hi"),
    ("ฬ", "lor chu"),
    ("อ", "or ang"),
    ("ฮ", "hor nokhuk")
]

class FlashcardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")

        self.card_label = tk.Label(root, text="", font=("Helvetica", 40), width=10, height=5)
        self.card_label.pack(pady=50)

        self.flip_button = tk.Button(root, text="Flip", font=("Helvetica", 20), command=self.flip_card)
        self.flip_button.pack()

        self.show_consonant()

    def show_consonant(self):
        self.card_label.config(text=random.choice(consonants)[0])
        self.current_consonant = random.choice(consonants)

    def flip_card(self):
        self.card_label.config(text=self.current_consonant[1])

# Set up the Tkinter window
root = tk.Tk()
game = FlashcardGame(root)

# Start the Tkinter event loop
root.mainloop()
