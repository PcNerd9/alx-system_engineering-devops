# 0x04. Loops, Conditions, and Parsing

## Description
This project explores loops, conditional statements, and parsing in the shell. It covers the use of `while`, `until`, `for` loops, as well as `if`, `else`, and `case` conditions to control the flow of shell scripts. The project also introduces parsing techniques using shell utilities.

## Learning Objectives
By the end of this project, you should be able to explain the following concepts:
- How to create and use loops (for, while, until)
- How to use conditional statements (if, else, elif, case)
- How to parse a file using `cut`, `awk`, `sed`, and `grep`
- The difference between file descriptors and streams (stdout, stderr)
- How to handle special files like `/dev/null` in shell scripts

## File Descriptions
- **0-RSA_public_key.pub**: A public RSA key generated as part of the project.
- **1-for_best_school**: Displays "Best School" 10 times using a `for` loop.
- **2-while_best_school**: Displays "Best School" 10 times using a `while` loop.
- **3-until_best_school**: Displays "Best School" 10 times using an `until` loop.
- **4-if_9_say_hi**: Displays "Best School" and checks if the ninth iteration outputs "Hi" using an `if` statement.
- **5-4_bad_luck_8_is_your_chance**: Loops from 1 to 10 and displays "bad luck" for 4, "good luck" for 8, and the iteration number otherwise.
- **6-superstitious_numbers**: Displays numbers from 1 to 20, printing "bad luck from China" for 4, "bad luck from Japan" for 9, and "bad luck from Italy" for 17.
- **7-clock**: Displays the time in `HH:MM:SS` format every second for 12 hours.
- **8-for_ls**: Displays the content of the current directory using a `for` loop.
- **9-to_file_or_not_to_file**: Gives information about the `school` file.
- **10-fizzbuzz**: A shell version of the classic FizzBuzz problem. Prints numbers from 1 to 100, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".
- **100-read_and_cut**: Displays the username, home directory, and user ID of each user in `/etc/passwd` using `cut`.
- **101-tell_the_story_of_passwd**: Displays the content of `/etc/passwd` in a structured format.
- **102-lets_parse_apache_logs**: Parses an Apache log file and displays IP addresses and the number of requests from each IP.
- **103-dig_the-data**: Parses an Apache log file and displays the number of occurrences of each status code.

## Usage
To run any script:
```bash
./<script_name>

