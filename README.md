# cbot - C Coding Environment Creator Bot

cbot is a Python-based program that creates a basic C coding environment for users. It automates the process of setting up a directory structure and creating essential files for starting a C programming project.

## Features

- Creates a directory with the specified name and path provided by the user.
- Generates a `program.c` file with a basic code to print "Hello, World!".
- Generates a `settings.json` file to store project-related information such as the project name, version, and creator's name.
- Provides an output file to execute the `program.c` code.
- Provides an `compiler.sh` script for compiling and running the `program.c` file

## Getting Started
### Prerequisites

- Python 3.x
- GCC (GNU Compiler Collection) for C compilation

### Installation

1. Clone the cbot repository:
    ```bash
    git clone https://github.com/SrijanBhattacharyya/c-coding-env-creator-bot.git
2. First run:
    ```bash
    python3 c-coding-env-creator-bot/main.py
## Usage
1. Run the cbot.py script:
    ```bash
    cbot
2. Follow the on-screen instructions to provide the project name, path, and other details.
3. cbot will create the project directory, generate the necessary files, and set up the basic C coding environment.

## Directory Structure
- `compiler.sh`: Shell script to compile and run the `program.c` file
- `program.c`: Sample C program to print "Hello, World!"
- `settings.json`: Project settings file

## Configuration
The `settings.json` file allows you to customize certain aspects of the cbot program. You can modify the following parameters:

- `"project_name"`: The name of the project.
- `"version"`: The version number of the project.
- `"creator_name"`: Your name or the creator's name.

## Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contributing
Contributions to the `cbot` project are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

## NOTE:
- Please make sure to change the `"creator_name"` tag which is present at `c-coding-env-creator-bot/defaults/settings.json` to your name. By default it has my name "Srijan Bhattacharyya".
- Please run the `compiler.sh` after each and every time you edit the `program.c` file with the command
    ```bash
    ./compiler.sh
