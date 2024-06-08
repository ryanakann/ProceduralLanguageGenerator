from src.command import Command

class GenerateCommand(Command):
    def __init__(self, parser):
        super().__init__(parser)
        print("Running Generate")
