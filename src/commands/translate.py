import json
from src.command import Command

class TranslateCommand(Command):
    def __init__(self, parser):
        super().__init__(parser)
        
        parser.add_argument("--text", help="The text in English you want to translate.")
        args = parser.parse_known_args()[0]
        text = args.text.lower()
        print(text)
        
        language_map = self.read_language_from_file()
        
        self.translate(language_map, text)
        

    def read_language_from_file(self):
        with open("out/language.json", "r") as file:
            input_string = file.read()
            try:
                return json.loads(input_string)
            except:
                print("Could not read \"out/language.json\". Have you run generate?")
                exit(1)
    
    def translate(self, language_map, text):
        words = text.split(" ")
        print(words)
        output = ""
        for word in words:
            new_word = language_map.get(word, "<UNKNOWN>")
            output += new_word + " "
        
        # Remove final space
        output = output[:-1]
        print(output)

