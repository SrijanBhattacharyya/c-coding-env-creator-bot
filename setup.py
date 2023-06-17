import os, sys


def setup (mainDir: os.path):
    # Get the user's home directory
    home_dir = os.path.expanduser ("~")

    # Define the alias
    python_path = sys.executable
    command = f"{python_path} {mainDir}"
    alias = f"alias cbot='{command}'"

    # Build the full path to the .bashrc file
    bashrc_path = os.path.join (home_dir, ".bashrc")


    # Check if the alias already exists in the .bashrc file
    with open (bashrc_path, "r") as file:
        bashrc_content = file.read ()
        if alias not in bashrc_content:
            # Open the .bashrc file in append mode and write the alias
            with open (bashrc_path, "a") as file:
                file.write (alias + "\n")