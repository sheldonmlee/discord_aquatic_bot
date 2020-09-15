class Hangfish():
    discord_instances = {}
    
    def __init__(self, word):
        # Word to be guessed
        self.word = word

        # Stores the graphical string of hangman progress.
        self.graphical_string = ""
        
        # Keeps track of characters guessed.
        self.guessed_indices = [False] * len(word)

        # Output of characters guessed
        self.graphical_progress_string = ""
        for i in range(len(word)):
            self.graphical_progress_string += "_"

        self.guesses = 26
        self.letters_guessed = 0

        # Game state
        self.running = True
        self.status_message = ""

    def guess(self, c):
        if not self.running: return
        if len(c) == 1:
            for i in range(len(self.word)):
                if self.word[i] == c:
                    if not self.guessed_indices[i]:
                        self.letters_guessed += 1
                        temp_list = list(self.graphical_progress_string)
                        temp_list[i] = c
                        self.graphical_progress_string = ''.join(temp_list)
                    self.guessed_indices[i] = True

        self.guesses -= 1

        word_guessed = self.letters_guessed == len(self.word) or c == self.word
        out_of_guesses = self.guesses == 0

        if word_guessed or out_of_guesses:
            self.running = False
        if word_guessed:
            self.status_message = "Word Guessed."
        elif out_of_guesses:
            self.status_message = "Out of Guesses."

    def getString(self):
        string = ""
        string += self.graphical_string + 'guesses left = {}\n'.format(self.guesses) + self.graphical_progress_string + '\n'
        if not self.running: string += self.status_message
        return string


def main():
    hangfish = Hangfish("Gen")

    print(hangfish.getString())
    while (hangfish.running):
        try:
            letter = str(input("Enter Letter\n"))[0]
            hangfish.guess(letter)
            print(hangfish.getString())
        except IndexError:
            print("Please enter a letter.")

if __name__ == "__main__":
    main()
