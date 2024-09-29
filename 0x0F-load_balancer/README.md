# 0x0F. Load Balancer

## Description
This project focuses on the concepts and implementation of load balancing in web applications. Load balancing helps distribute incoming network traffic across multiple servers to ensure reliability and performance.

## Learning Objectives
By the end of this project, you should be able to:
- Understand the purpose and types of load balancers.
- Set up and configure a load balancer for web applications.
- Implement health checks and routing strategies.

## File Descriptions
- **0-custom_http_response_header**: A script that demonstrates how to customize HTTP response headers using a load balancer.
- **1-install_load_balancer**: A guide for installing and configuring a basic load balancer.
- **2-puppet_custom_http_response_header.pp**: A Puppet manifest file that sets up a load balancer with custom HTTP response headers.

## Usage
- To install a load balancer, follow the instructions in `1-install_load_balancer`.
- Use the following command to check the status of your load balancer:
```bash
curl -I http://<your_load_balancer_IP>

