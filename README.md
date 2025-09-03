<h1 align="center">Port-Scanner</h1>

A high-performance, extensible Port Scanner built with Python, supporting multiple backends (socket, nmap, scapy) and output formats (JSON, HTML, text).
This project is designed for learning network basics, penetration testing workflows, and scalable CLI tool development.


## ✨ Features

 - Scan single hosts or entire ranges
 - Multiple scanning engines:
   - ⚡ Socket (lightweight, built-in Python)
   - 📡 Nmap (leveraging Nmap capabilities via python-nmap)
   - 🔬 Scapy (custom packet crafting & analysis)
 - Parallel scanning with configurable workers
 - Export reports:
   - JSON
   - HTML
   - Text
 - Clean project structure with logging, utils, and reporting


## Project Structure

       port-scanner/
       ├── README.md
       ├── requirements.txt
       ├── src/
       │   ├── main.py             # CLI entry point
       │   ├── scanner.py          # Core scanning logic
       │   ├── engines/            # Engines (socket, nmap, scapy)
       │   │   ├── socket_engine.py
       │   │   ├── nmap_engine.py
       │   │   └── scapy_engine.py
       │   ├── reporting/          # Reporting formats
       │   │   ├── json_report.py
       │   │   ├── html_report.py
       │   │   └── text_report.py
       │   ├── utils/
       │   │   ├── logger.py
       │   │   └── validators.py
       │   └── config.py           # Config constants
       └── tests/                  # Unit tests


## 🚀 Installation

1. Clone the repo:
```
git clone https://github.com/yourusername/port-scanner.git
cd port-scanner
```

2. Create a virtual environment and install dependencies:
```
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. (Optional) Install Nmap:

 - Linux: sudo apt install nmap

 - Mac: brew install nmap

 - Windows: Download Nmap


## 🛠 Usage
### Basic Scan
```
python src/main.py scan --target scanme.nmap.org --ports 1-100
```
### Choose Engine
```
python src/main.py scan --target 192.168.1.1 --ports 20-80 --engine nmap
```
