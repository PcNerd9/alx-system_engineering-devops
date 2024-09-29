# 0x0B. SSH

## Description
This project covers Secure Shell (SSH), a protocol for secure remote login and other secure network services over an insecure network. It provides the basics of SSH configuration, key management, and best practices for secure connections.

## Learning Objectives
By the end of this project, you should be able to:
- Understand the purpose and functionality of SSH.
- Generate and manage SSH keys.
- Configure SSH for secure access to remote systems.

## File Descriptions
- **0-use_a_private_key**: A script that demonstrates how to use a private SSH key for authentication when connecting to a remote server.
- **1-create_ssh_key_pair**: A guide on how to create an SSH key pair and configure it for use.
- **100-puppet_ssh_config.pp**: A Puppet manifest file that configures SSH settings on a system.
- **2-ssh_config**: An example SSH configuration file demonstrating various options for SSH connections.

## Usage
- To connect to a remote server using SSH, use the following command:
```bash
ssh -i <private_key> <user>@<host>

