# 0x10. HTTPS SSL

## Description
This project focuses on securing web applications using HTTPS and SSL/TLS protocols. It covers the concepts of encryption, certificates, and how to set up a secure web server.

## Learning Objectives
By the end of this project, you should be able to:
- Understand the importance of SSL/TLS in securing web traffic.
- Generate SSL certificates for testing purposes.
- Configure a web server to support HTTPS.

## File Descriptions
- **0-world_wide_web**: A script that explains the significance of the World Wide Web and the role of HTTPS.
- **1-haproxy_ssl_termination**: A configuration file demonstrating SSL termination using HAProxy.
- **100-redirect_http_to_https**: A script that sets up redirection from HTTP to HTTPS for a web server.

## Usage
- To generate a self-signed SSL certificate, use the following command:
```bash
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout key.pem -out cert.pem

