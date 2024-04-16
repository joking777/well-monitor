import logging
import logging.config
import json
import os

def setup_logging():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Load logging configuration from JSON file
    config_file_path = os.path.join(script_dir, 'logging_config.json')
    with open(config_file_path, 'r') as f:
        config = json.load(f)
        logging.config.dictConfig(config)

# Call the setup_logging function to initialize the logger
setup_logging()

# Get the logger instance
logger = logging.getLogger(__name__)