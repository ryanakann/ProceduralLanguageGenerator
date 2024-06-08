from argparse import ArgumentParser

from src.command import COMMANDS, GENERATE_COMMAND, TRANSLATE_COMMAND
from src.commands.generate import GenerateCommand
from src.commands.translate import TranslateCommand

def main():
    parser = ArgumentParser(prog="plg")
    parser.add_argument("command", help="The command you want to run.", choices=COMMANDS)

    args = parser.parse_known_args()[0]

    subparsers = parser.add_subparsers(help="subparser help", dest="subparser")
    generate_parser = subparsers.add_parser(GENERATE_COMMAND, help="generate help")
    translate_parser = subparsers.add_parser(TRANSLATE_COMMAND, help="translate help")

    if args.command == GENERATE_COMMAND:
        GenerateCommand(generate_parser)
    elif args.command == TRANSLATE_COMMAND:
        TranslateCommand(translate_parser)
