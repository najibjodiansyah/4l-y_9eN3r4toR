
from ast import Str


class Alay:
    def __init__(self) -> Str:
        self.text = ""

    def besarkecil(self) -> str:
        text = self.text
        hasil = ""
        for i, _ in enumerate(text):
            if i % 2 == 0:
                hasil += text[i].upper()
            else:
                hasil += text[i].lower()
        return hasil

    def gabungangka(self):
        text = self.text
        hasil = ""
        kamus = {
            "a": "4",
            "b": "8",
            "e": "3",
            "g": "6",
            "i": "!",
            "o": "0",
            "s": "5",
            "j ": "7",
        }
        for i, _ in enumerate(text):
            if text[i].lower() in kamus:
                hasil += kamus[text[i]]
            else:
                hasil += text[i]
        return hasil