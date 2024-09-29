# 0x02. Shell, I/O Redirections and Filters

## Description
This project focuses on input/output redirections, filtering, and manipulating text files through the shell. You'll learn how to redirect output, combine commands, and manipulate file content using standard Unix commands.

## File Descriptions
- **0-hello_world**: Prints "Hello, World" followed by a new line to the standard output.
- **1-confused_smiley**: Displays a confused smiley `"(Ôo)'`.
- **2-hellofile**: Displays the content of the `/etc/passwd` file.
- **3-twofiles**: Displays the content of `/etc/passwd` and `/etc/hosts`.
- **4-lastlines**: Displays the last 10 lines of `/etc/passwd`.
- **5-firstlines**: Displays the first 10 lines of `/etc/passwd`.
- **6-third_line**: Displays the third line of the file `iacta`.
- **7-file**: Creates a file named `\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)` with the content `Best School` inside.
- **8-cwd_state**: Writes the result of the command `ls -la` into a file called `ls_cwd_content`.
- **9-duplicate_last_line**: Duplicates the last line of the file `iacta`.
- **10-no_more_js**: Deletes all regular files with a `.js` extension in the current directory and its subfolders.
- **11-directories**: Counts the number of directories and sub-directories in the current directory.
- **12-newest_files**: Displays the 10 newest files in the current directory.
- **13-unique**: Takes a list of words as input and prints only the words that appear exactly once.
- **14-findthatword**: Displays lines containing the pattern "root" from the file `/etc/passwd`.
- **15-countthatword**: Displays the number of lines that contain the pattern "bin" in the file `/etc/passwd`.
- **16-whatsnext**: Displays lines containing the pattern "root" and 3 lines after them in the file `/etc/passwd`.
- **17-hidethisword**: Displays all the lines in the file `/etc/passwd` that do not contain the pattern "bin".
- **18-letteronly**: Displays all lines of the file `/etc/ssh/sshd_config` starting with a letter.
- **19-AZ**: Replaces all characters `A` and `c` in input with `Z` and `e`, respectively.
- **20-hiago**: Removes all letters `c` and `C` from input.
- **21-reverse**: Reverses its input.
- **22-users_and_homes**: Displays all users and their home directories, sorted by users, based on the `/etc/passwd` file.
- **100-empty_casks**: Finds all empty files and directories in the current directory and subdirectories.
- **101-gifs**: Lists all files with a `.gif` extension in the current directory and its sub-directories.
- **103-the_biggest_fan**: Parses the log file and displays IPs with the highest requests.

## Usage
To run a script:
```bash
./<script_name>

