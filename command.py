WHITESPACES = [' ', '\t', '\n']

class Command:
    command_prefix = '$'
    __callbacks = {}

    @staticmethod
    def __getWords(string):
        words = []
        # Add whitespace to accept last word
        string += " "
        word = ""
        for c in string:
            if c in WHITESPACES and len(word) > 0:
                words.append(word)
                word = ""
            elif c not in WHITESPACES:
                word = word + c
        return words

    @staticmethod
    def __getCommand(string):
        words = Command.__getWords(string);
        if words[0].startswith(Command.command_prefix):
            return words[0][1:]
        return ""

    @staticmethod
    def __getArgs(string):
        words = Command.__getWords(string);
        return words[1:]

    @staticmethod
    def registerCallback(command, callback):
        Command.__callbacks[command] = callback

    @staticmethod
    def call(command):
        func = Command.__callbacks.get(Command.__getCommand(command), None)
        if func is not None:
            return func(*tuple(Command.__getArgs(command)))
        return None

