# 0x05. Processes and Signals

## Description
This project covers the basics of processes and signals in Linux. You will learn how to list, manage, and terminate processes, as well as how to handle signals in a Linux environment. The project introduces concepts such as process IDs, signal handling, and how to kill or stop processes.

## Learning Objectives
By the end of this project, you should be able to explain the following concepts:
- What is a process and how processes are created
- What are PID and PPID
- How to display information about processes (e.g., `ps`, `top`)
- How to kill a process using signals (`kill`, `pkill`, `killall`)
- What is a signal and how to send it
- How to handle signals in Bash scripts

## File Descriptions
- **0-what-is-my-pid**: A script that prints the process ID (PID) of the current shell.
- **1-list_your_processes**: Displays a list of currently running processes along with their PID, owner, and command.
- **2-show_your_bash_pid**: A script that displays the PID of the current Bash shell.
- **3-show_your_bash_pid_made_easy**: A script that gets the PID of the current shell using a command pipeline.
- **4-to_infinity_and_beyond**: A script that displays "I am alive" indefinitely every 2 seconds until it receives a `SIGTERM` signal.
- **5-dont_stop_me_now**: A script that stops the process started by `4-to_infinity_and_beyond` using the `kill` command.
- **6-stop_me_if_you_can**: A script that stops the process started by `4-to_infinity_and_beyond` only when receiving a `SIGKILL` or `SIGSTOP` signal.
- **7-highlander**: A script that starts an infinite loop that traps `SIGTERM` and displays a message when the signal is received.
- **8-beheaded_process**: A script that kills the process with a specific PID.

- **100-process_and_pid_file**: A script that creates a file named `/var/run/my_process.pid` containing its own PID, and then waits indefinitely.

## Usage
To run any of the scripts:
```bash
./<script_name>

