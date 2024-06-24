#!/usr/bin/env python

import random

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """
    ]
    return stages[tries]

def choose_word():
    word_list = ["bengkel", "pemantapan", "pengaturcaraan", "python", "asas","sains","komputer"]
    return random.choice(word_list).upper()

def hangman():
    word = choose_word()
    word_letters = set(word)
    alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    guessed_letters = set()
    tries = 6

    print("Selamat datang ke permainan Hangman!")
    print(display_hangman(tries))  # Papar tahap permulaan hangman
    print(" ".join(["_" for _ in word]))  # Papar garis bawah bagi setiap huruf dalam perkataan

    while len(word_letters) > 0 and tries > 0:
        guess = input("Teka satu huruf: ").upper()
        
        if guess in alphabet - guessed_letters:
            guessed_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
                print("Tebakan yang baik: {guess}")
            else:
                tries -= 1
                print("Tebakan salah: {guess}. Anda mempunyai {tries} percubaan lagi.")
        elif guess in guessed_letters:
            print("Anda sudah meneka huruf itu.")
        else:
            print("Input tidak sah. Sila masukkan huruf.")

        word_display = [letter if letter in guessed_letters else '_' for letter in word]
        print(display_hangman(tries))  # Papar tahap hangman semasa
        print(' '.join(word_display))  # Papar keadaan semasa perkataan yang diteka

    if tries == 0:
        print("Permainan Tamat! Perkataannya adalah {word}.")
    else:
        print("Tahniah! Anda berjaya meneka perkataan {word}!")

if __name__=="__main__":
        hangman()