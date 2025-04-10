import time
import sys
import os
import logging
import subprocess

# Set up logging to both the terminal and the log file
log_formatter = logging.Formatter('%(asctime)s - %(message)s')

# Create a logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# File handler for logging to file
file_handler = logging.FileHandler('cron_job.log')
file_handler.setFormatter(log_formatter)
logger.addHandler(file_handler)

# Stream handler for logging to terminal (stdout)
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)

# Add the correct scripts folder to the sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Time interval in seconds (e.g., every 5 minutes)
INTERVAL = 300  

while True:
    try:
        logger.info("Calling fetch_google_sheets_docs.py...")

        # Run the script using subprocess to capture stdout and stderr
        result = subprocess.run(['python', 'fetch_google_sheets_docs.py'], capture_output=True, text=True)
        
        # Log the standard output and standard error of the script
        if result.stdout:
            logger.info("Output of fetch_google_sheets_docs.py:\n" + result.stdout)
        if result.stderr:
            logger.error("Error output of fetch_google_sheets_docs.py:\n" + result.stderr)
        
        logger.info("fetch_google_sheets_docs.py executed successfully.")
        
    except Exception as e:
        logger.error(f"Error while running fetch_google_sheets_docs.py: {e}")

    logger.info(f"Sleeping for {INTERVAL} seconds...\n")
    time.sleep(INTERVAL)
