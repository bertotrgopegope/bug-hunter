markdown
<div align="center">
  <img src="94faef9a35ff42e55c12a6aaf5503697.jpg" alt="Bug Hunter Preview" width="100%">
  
  # Bug Hunter Recon Tool
  **A simple Python-based subdomain enumeration and HTTP probing tool designed for Termux/Android and Linux.**
  
  ![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white)
  ![Termux](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux-black?style=flat-square&logo=linux)
  ![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)
</div>

---

## 🚀 Features
- **Subdomain Enumeration:** Resolves common subdomains via `socket`.
- **HTTP/HTTPS Probe:** Checks live status codes and extracts page titles.
- **Multi-threading:** Fast scanning using `ThreadPoolExecutor`.
- **Custom Terminal UI:** Renders an ASCII image and colored output (Blue theme).

## 🛠️ Installation

1. Update Termux packages and install dependencies:
   ```bash
   pkg update && pkg upgrade -y
   pkg install python chafa -y
```

2. Install required Python libraries:
   ```bash
   pip install requests colorama urllib3
   ```
3. Clone this repository:
   ```bash
   git clone https://github.com/bertotrgopegope/bug-hunter.git
   cd bug-hunter
   ```

⚙️ Configuration

Before running, ensure you have the background image set in the script.

1. Put your image in /storage/emulated/0/avg/ (or any path).
2. Open bug_hunter.py and edit the BG_IMAGE variable:
   ```python
   BG_IMAGE = "/storage/emulated/0/avg/your_image.jpg"
   ```

💻 Usage

Run the script followed by the target domain:

```bash
python bug_hunter.py <domain>
```

Example:

```bash
python bug_hunter.py hackerone.com
```

⚠️ Disclaimer

This tool is for educational purposes and authorized bug bounty testing only. Do not use it on targets without written permission. The author is not responsible for any misuse or damage caused by this program.
