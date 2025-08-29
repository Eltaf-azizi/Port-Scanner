from setuptools import setup, find_packages

setup(
    name="portscanner",
    version="0.1.0",
    description="Extensible Port Scanner (Sockets, Scapy, Nmap)",
    author="Your Name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "python-nmap>=0.7.1",
        "scapy>=2.5.0",
        "PyYAML>=6.0",
        "Jinja2>=3.1",
    ],
    entry_points={
        "console_scripts": [
            "portscan=portscanner.main:run_cli",
        ]
    },
    python_requires=">=3.8",
)
