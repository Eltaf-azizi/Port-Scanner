import os
import sys
import logging
import logging.config
import yaml

from portscanner.cli.parser import build_parser
from portscanner.cli.commands import run_scan


def load_settings() -> dict:
    config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'settings.yaml')
    config_path = os.path.abspath(config_path)
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or {}
    return {}