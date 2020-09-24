class Hangfish():

    def __init__(self, word):
        # Word to be guessed
        self.word = word

        # Stores the graphical strings of hangman progress.
        self.frames = Hangfish.getFrames("hangfish_states.txt")
        
        # Keeps track of characters guessed.
        self.guessed_indices = [False] * len(word)

        # Output of characters guessed
        self.graphical_progress_string = ""
        for i in range(len(word)):
            self.graphical_progress_string += "_"

        self.guesses = 10
        self.attempts = 0
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

        self.attempts += 1

        word_guessed = self.letters_guessed == len(self.word) or c == self.word
        out_of_guesses = self.attempts == self.guesses

        if word_guessed or out_of_guesses:
            self.running = False
        if word_guessed:
            self.status_message = "Word Guessed."
        elif out_of_guesses:
            self.status_message = "Out of Guesses."

    def getString(self):
        string = ""
        frame = self.frames.get("{}".format(self.attempts+1), None) 
        if frame is not None:
            for line in frame:
                string += line+'\n'
        
        string += "guesses left = {}\n".format(self.guesses-self.attempts) + self.graphical_progress_string + '\n'

        if not self.running: string += self.status_message
        return string

    @staticmethod
    def getFrames(filename):
        file_handle = open(filename)
        tag = ""
        frame = []
        frames = {}
        while True:
            line = file_handle.readline()
            if len(frame) > 0 and (not line.startswith("#") or line == ""):
                if tag == "":
                    tag = "Tag: {}".format(len(frames)+1)
                frames[tag] = frame
                tag = ""
                frame = []
            if line.startswith("!"):
                tag = line.strip()[1:]
            elif line.startswith("#"):
                frame.append(line.strip()[1:])
            if line == "": break
        return frames

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
