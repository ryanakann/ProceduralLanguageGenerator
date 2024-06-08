from src.command import Command

class TranslateCommand(Command):
    def __init__(self, parser):
        super().__init__(parser)
        print("Running Translate")
