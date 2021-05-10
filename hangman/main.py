from random import choice
from resources import words, HANGMANPICS

word_game = choice(words)
hidden_word = [' _ ' for n in word_game]
num_guess = 0
print(''.join(hidden_word))

while num_guess <= 5:
    user_input = input(f'[{num_guess}/5]Take a guess. ')

    if user_input in word_game:
        indexes = [i for i in range(len(word_game)) if word_game[i] == user_input]
        for index in indexes:
            hidden_word[index] = user_input
    else:
        num_guess += 1

    if ' _ ' not in hidden_word:
        print(f"{HANGMANPICS[num_guess]}\n"
              f"{word_game}\n"
              f"You've won. :D")
        break

    print(HANGMANPICS[num_guess])
    print(''.join(hidden_word))

if num_guess > 5:
    print(f"You've lost. D: The word was {word_game}.")


