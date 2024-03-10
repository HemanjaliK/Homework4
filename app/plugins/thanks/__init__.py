import logging
from app.commands import Command


class ThanksCommand(Command):
    def execute(self):
        logging.info("Thank you!")
        print("Thank you!")