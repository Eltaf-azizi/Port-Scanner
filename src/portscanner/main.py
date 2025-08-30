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



def configure_logging():
    logconf = os.path.join(os.path.dirname(__file__), '..', '..', 'config', 'logging.conf')
    logconf = os.path.abspath(logconf)
    if os.path.exists(logconf):
        logging.config.fileConfig(logconf, disable_existing_loggers=False)
    else:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s: %(message)s')


def run_cli():
    configure_logging()
    parser = build_parser()
    args = parser.parse_args()
    settings = load_settings()

    if args.command == 'scan':
        try:
            run_scan(args, settings)
        except KeyboardInterrupt:
            print("\nScan interrupted.")
            sys.exit(1)


if __name__ == "__main__":
    run_cli()