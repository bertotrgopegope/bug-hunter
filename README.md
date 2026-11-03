# Bug Hunter Recon Tool

A simple Python-based subdomain enumeration and HTTP probing tool designed for Termux/Android and Linux.

![Bug Hunter Preview](preview.jpg)

## Features
- **Subdomain Enumeration:** Resolves common subdomains via `socket`.
- **HTTP/HTTPS Probe:** Checks live status codes and extracts page titles.
- **Multi-threading:** Fast scanning using `ThreadPoolExecutor`.
- **Custom Terminal UI:** Renders an ASCII image and colored output (Blue theme).

## Installation

1. Update Termux packages and install dependencies:
   ```bash
   pkg update && pkg upgrade -y
   pkg install python chafa -y
