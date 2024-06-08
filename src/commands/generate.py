from src.command import Command
from data.ira_sounds import IRA_SOUNDS
from data.words import WORDS
import re
from random import randint
import json
import os

class GenerateCommand(Command):
    def __init__(self, parser):
        super().__init__(parser)
        output = self.generate()
        self.write_language_to_file(output)

    # This is a really naive and goofy "language" generator.
    # Just getting some code out there, will enhance a LOT from here.
    # Does not obey sonority sequencing and does not preserve like-words.
    # For instance, "pen" might map to "vdiunth" and "pencil" to "pqttiot". Pretty bad.
    def generate(self):
        output = {}
        for word in WORDS:
            # I don't want to deal with goofy words at the moment
            # Filter out everything non-alphabetical
            if re.match("^[a-z]+$", word) is not None:
                length = randint(1, 10)
                new_word = ""
                for _ in range(length):
                    # randint is inclusive on both ends
                    index = randint(0, len(IRA_SOUNDS) - 1)
                    new_word += IRA_SOUNDS[index]
                output[word] = new_word
        return output
    
    def write_language_to_file(self, output):
        if not os.path.exists("out"):
            os.makedirs("out")
        with open("out/language.json", "w") as file:
            output_string = json.dumps(output)
            file.write(output_string)
