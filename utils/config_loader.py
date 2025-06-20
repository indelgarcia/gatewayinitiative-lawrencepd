import os
import json

def load_config():
    # Get current working directory (where notebook was launched from)
    cwd = os.getcwd()

    # Look for config.json one level up
    config_path = os.path.join(cwd, '..', 'config.json')
    config_path = os.path.abspath(config_path)

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Could not find config.json at: {config_path}")

    with open(config_path, 'r') as f:
        config = json.load(f)

    return config
