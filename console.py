#!/usr/bin/python3

"""
"""

import herware
import readline
import getpass
import cmd
from models import storage

class Console(cmd.Cmd):
    """
    Console class for interacting with the Herware device.
    
    This class provides a command-line interface (CLI) for users to interact with
    the Herware device. It includes commands for connecting to and disconnecting
    from devices, sending commands, and viewing command history.
    """

    intro = "Welcome to Herware Console!"

    def __init__(self):
        """
        Initialize the Console object.
        
        This method sets up the command prompt and initializes the Herware device.
        """
        super().__init__()
        self.prompt = "herware> "

        # Initialize Herware device
        self.device = herware.Herware()

    def do_exit(self, arg):
        """Exit the console application."""
        print("Exiting Herware Console. Goodbye!")
        return True

    def do_connect(self, arg):
        """
        Connect to a device.
        
        Args:
            arg (str): The name of the device to connect to.
        """
        device_name = arg
        try:
            self.device.connect(device_name)
            print(f"Connected to {device_name}")
        except Exception as e:
            print(f"Failed to connect to {device_name}: {str(e)}")

    def do_disconnect(self, arg):
        """Disconnect from the current device."""
        try:
            self.device.disconnect()
            print("Disconnected from the current device.")
        except Exception as e:
            print(f"Failed to disconnect: {str(e)}")

    def do_send_command(self, arg):
        """
        Send a command to the connected device.
        
        Args:
            arg (str): The command to send to the device.
        """
        try:
            response = self.device.send_command(arg)
            print(f"Response from device: {response}")
        except Exception as e:
            print(f"Error sending command: {str(e)}")

    def do_history(self, arg):
        """Show the command history."""
        self.stdout.write("Command history:\n")
        for i, line in enumerate(readline.get_history()):
            self.stdout.write("%d: %s\n" % (i, line))

    def emptyline(self):
        """Execute the last command from history on empty line."""
        if readline.get_history_item(0) != '':
            return readline.get_history_item(0)
        return None

    def postloop(self):
        """Write command history to the console application."""
        self.write_history_file()

    def preloop(self):
        """Authenticate user before starting the console application."""
        if not self.auth():
            print("Authentication failed. Exiting the console.")
            return False

    def auth(self):
        """Authenticate user with a password."""
        prompt = "Enter password: "
        password = getpass.getpass(prompt)
        return password == "password"


if __name__ == "__main__":
    console = Console()
    console.preloop()
    console.cmdloop()
    console.postloop()
