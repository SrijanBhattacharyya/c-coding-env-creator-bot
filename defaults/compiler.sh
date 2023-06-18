#!/bin/bash

# Check if the program.c file exists
if [ -f "program.c" ]; then
    # Compile the program.c file
    gcc program.c -o output

    # Check if the compilation was successful
    if [ $? -eq 0 ]; then
        echo -e "\033[1;32m[+] Compilation successful.\033[0m"
        echo "Running the program..."
        
        # Execute the compiled program
        ./output
    else
        echo -e "\033[1;31m[-] CompilationError: Compilation failed. Please check your code.\033[0m"
    fi
else
    echo -e "\033[1;31m[-] FileNotFoundError: No such file or directory: program.c\033[0m"
fi