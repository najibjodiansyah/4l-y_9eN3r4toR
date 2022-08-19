from .kamus import kamus
from ast import Str


class Alay:
    def __init__(self) -> Str:
        self.text = ""

    def besarkecil(self) -> str:
        text = self.text
        hasil = ""
        for alphabet, _ in enumerate(text):
            if alphabet % 2 == 0:
                hasil += text[alphabet].upper()
            else:
                hasil += text[alphabet].lower()
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
        for alphabet, _ in enumerate(text):
            if text[alphabet].lower() in kamus:
                hasil += kamus[text[alphabet]]
            else:
                hasil += text[alphabet]
        return hasil

    def vokal(self):
        text = self.text
        vocal = ['a', 'i', 'u' , 'e', 'o']
        for alphabet in text:
            if alphabet in vocal:
                text = text.replace(alphabet, "i")
        return text

    def konversi_kata(self):
        kata_pecah = self.text.split()
        hasil = []
        for kata in kata_pecah:
            if kata in kamus:
                kata = kamus[kata]
            hasil.append(kata)
        return ' '.join(hasil)

