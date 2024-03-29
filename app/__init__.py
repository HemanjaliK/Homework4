from app.commands import CommandHandler
from app.commands.exit import ExitCommand
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand
from app.commands.cool import coolCommand
from app.commands.thanks import thanksCommand

class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()
        # Register commands here


    def start(self):
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("cool", coolCommand())
        self.command_handler.register_command("thanks", thanksCommand())

        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Process, Loop
            self.command_handler.execute_command(input(">>> ").strip())



