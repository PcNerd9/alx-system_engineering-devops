# 0x01-shell_permissions

## Description
This project covers various file permissions and operations related to users, groups, and file access control in a Unix-like operating system. It introduces basic concepts such as changing ownership and modifying permissions of files and directories.

## File Descriptions
- **0-iam_betty**: Changes the current user to `betty`.
- **1-who_am_i**: Prints the effective username of the current user.
- **2-groups**: Prints all the groups the current user is part of.
- **3-new_owner**: Changes the owner of the file `hello` to the user `betty`.
- **4-empty**: Creates an empty file called `hello`.
- **5-execute**: Adds execute permission to the owner of the file `hello`.
- **6-multiple_permissions**: Adds execute permission to the owner, group, and other users for the file `hello`.
- **7-everybody**: Adds execution permission to the owner, group, and others for the file `hello`.
- **8-James_Bond**: Sets permissions for the file `hello` so that the owner has no permission, the group has no permission, and others have all permissions.
- **9-John_Doe**: Sets the mode of the file `hello` to `-rwxr-x-wx`.
- **10-mirror_permissions**: Mirrors the permissions of `olleh` to `hello`.
- **11-directories_permissions**: Adds execute permission to all subdirectories of the current directory for the owner, group, and others.
- **12-directory_permissions**: Creates a directory named `my_dir` with permissions 751 in the working directory.
- **13-change_group**: Changes the group owner of the file `hello` to `school`.
- **100-change_owner_and_group**: Changes the owner to `vincent` and the group owner to `staff` for all files and directories in the working directory.
- **101-symbolic_link_permissions**: Changes the owner and the group of `_hello` to `vincent` and `staff` without affecting the symlink target.
- **102-if_only**: Changes the owner of the file `hello` to `betty` only if it is owned by `guillaume`.
- **103-Star_Wars**: Plays the Star Wars IV episode in the terminal.

## Usage
To execute each script, use the following command structure:

```bash
./<script_name>

