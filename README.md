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
