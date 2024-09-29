# 0x03. Shell, init files, variables and expansions

## Description
This project dives into shell initialization files, variables (both local and global), and various shell expansions (arithmetic, brace, and parameter expansion). You will learn how to manipulate shell variables and perform operations using expansions.

## Learning Objectives
At the end of this project, you should be able to explain the following concepts without needing help:
- What happens when you type `$ ls -l *.txt`
- Shell initialization files
- Variables (local and global)
- Expansions (Arithmetic, Variable, Shell Arithmetic)
- Shell Arithmetic and alias commands

## File Descriptions
- **0-alias**: Creates an alias named `ls` with the value `rm *`.
- **1-hello_you**: Prints `hello user`, where `user` is the current Linux user.
- **2-path**: Adds `/action` to the `PATH`. `/action` should be the last directory the shell looks into when searching for a program.
- **3-paths**: Counts the number of directories in the `PATH`.
- **4-global_variables**: Lists environment variables.
- **5-local_variables**: Lists all local variables, environment variables, and functions.
- **6-create_local_variable**: Creates a new local variable `BEST` with the value `School`.
- **7-create_global_variable**: Creates a new global variable `BEST` with the value `School`.
- **8-true_knowledge**: Prints the result of the addition of 128 with the value stored in the environment variable `TRUEKNOWLEDGE`.
- **9-divide_and_rule**: Prints the result of `POWER` divided by `DIVIDE`, where `POWER` and `DIVIDE` are environment variables.
- **10-love_exponent_breath**: Displays the result of `BREATH` to the power of `LOVE`, where `BREATH` and `LOVE` are environment variables.
- **11-binary_to_decimal**: Converts a binary number stored in the environment variable `BINARY` to decimal.
- **12-combinations**: Prints all possible combinations of two letters, except `oo`.
- **13-print_float**: Prints a float stored in the environment variable `NUM`.
- **100-decimal_to_hexadecimal**: Converts a number stored in the environment variable `DECIMAL` to hexadecimal.
- **101-rot13**: Encodes and decodes text using the rot13 encryption.
- **102-odd**: Prints every other line from the input, starting with the first line.
- **103-water_and_stir**: Adds two numbers stored in the environment variables `WATER` and `STIR` and prints the result. The numbers are given in the form of base `water` and `stir`.

## Usage
To run a script:
```bash
./<script_name>

