from argparse import ArgumentParser

from src.command import COMMANDS, GENERATE_COMMAND, TRANSLATE_COMMAND
from src.commands.generate import GenerateCommand
from src.commands.translate import TranslateCommand

def main():
    parser = ArgumentParser(prog='plg')
    parser.add_argument('command', help="The command you want to run.", choices=COMMANDS)
    args = parser.parse_args()
    
    if args.command == GENERATE_COMMAND:
        GenerateCommand(parser)
    elif args.command == TRANSLATE_COMMAND:
        TranslateCommand(parser)
