# 0x00-shell_basics

## Description
This project introduces the basics of shell commands and operations. It covers navigation, file manipulation, and basic scripting concepts in a Unix-like environment.

## File Descriptions
- **0-current_working_directory**: A script that prints the absolute path name of the current working directory.
- **1-listit**: Displays the contents of the current directory.
- **2-bring_me_home**: Changes the working directory to the user's home directory.
- **3-listfiles**: Lists files in long format.
- **4-listmorefiles**: Lists all files, including hidden files, in long format.
- **5-listfilesdigitonly**: Lists files with numeric user and group IDs.
- **6-firstdirectory**: Creates a directory named `my_first_directory` in the `/tmp/` directory.
- **7-movethatfile**: Moves a file named `betty` from `/tmp/` to `/tmp/my_first_directory/`.
- **8-firstdelete**: Deletes the file `betty`.
- **9-firstdirdeletion**: Deletes the directory `my_first_directory` in the `/tmp/` directory.
- **10-back**: Changes the working directory to the previous one.
- **11-lists**: Lists files in the current, parent, and `/boot/` directories.
- **12-file_type**: Prints the type of the file named `iamafile` located in the `/tmp/` directory.
- **13-symbolic_link**: Creates a symbolic link to `/bin/ls`, named `__ls__`, in the current working directory.
- **14-copy_html**: Copies all HTML files from the current directory to the parent directory, but only copies files that didn't exist or were newer than the versions in the parent directory.
- **100-lets_move**: Moves all files beginning with an uppercase letter to the directory `/tmp/u`.
- **101-clean_emacs**: Deletes all files in the current working directory that end with the character `~`.
- **102-tree**: Creates directories `welcome/`, `welcome/to/`, and `welcome/to/school/` in the current directory.
- **103-commas**: Lists files and directories, separated by commas.

## Usage
To execute each script, use the following command structure:

```bash
./<script_name>

