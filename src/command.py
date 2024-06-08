GENERATE_COMMAND="generate"
TRANSLATE_COMMAND="translate"

COMMANDS=[
    GENERATE_COMMAND,
    TRANSLATE_COMMAND
]

class Command:
    def __init__(self, parser):
        self.parser = parser