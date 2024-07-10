import os
import logging
import datetime

# Get today's date
today: datetime.date = datetime.date.today()
# Format today's date as YYYY-MM-DD
time :str = today.strftime('%Y-%m-%d')

# Create a root log directory if it doesn't exist
log_root_dir: str = 'logs'
# Create a root log directory if it doesn't exist
if not os.path.exists(log_root_dir):
    os.makedirs(log_root_dir)

# Define log format
log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

def create_info_logger(name: str) -> logging.Logger:
    # Create and configure an info logger
    info_logger = logging.getLogger(name)
    info_logger.setLevel(logging.INFO)

    # Create a FileHandler for info logs and set the format
    info_log_dir = os.path.join(log_root_dir, 'info')
    # Create a root log directory if it doesn't exist
    os.makedirs(info_log_dir, exist_ok=True)
    
    # Create a log file with today's date
    info_log_path = os.path.join(info_log_dir, f'{time}.log')
    # Create a FileHandler for info logs and set the format
    info_file_handler = logging.FileHandler(info_log_path)
    # Set the format
    info_file_handler.setFormatter(log_format)
    # Add the FileHandler to the logger
    info_logger.addHandler(info_file_handler)

    # Add a StreamHandler to print logs to the terminal
    info_stream_handler = logging.StreamHandler()
    # Set the format
    info_stream_handler.setFormatter(log_format)
    # Add the StreamHandler to the logger
    info_logger.addHandler(info_stream_handler)

    return info_logger

def create_error_logger(name: str) -> logging.Logger:
    # Create and configure an error logger
    error_logger = logging.getLogger(name)
    error_logger.setLevel(logging.ERROR)

    # Create a FileHandler for error logs and set the format
    error_log_dir = os.path.join(log_root_dir, 'error')
    # Create a root log directory if it doesn't exist
    os.makedirs(error_log_dir, exist_ok=True)
    
    # Create a log file with today's date
    error_log_path = os.path.join(error_log_dir, f'{time}.log')
    # Create a FileHandler for error logs and set the format
    error_file_handler = logging.FileHandler(error_log_path)
    # Set the format
    error_file_handler.setFormatter(log_format)
    # Add the FileHandler to the logger
    error_logger.addHandler(error_file_handler)

    # Add a StreamHandler to print logs to the terminal
    error_stream_handler = logging.StreamHandler()
    # Set the format
    error_stream_handler.setFormatter(log_format)
    # Add the StreamHandler to the logger
    error_logger.addHandler(error_stream_handler)

    return error_logger

def create_debug_logger(name: str) -> logging.Logger:
    # Create and configure a debug logger
    debug_logger = logging.getLogger(name)
    debug_logger.setLevel(logging.DEBUG)

    # Create a FileHandler for debug logs and set the format
    debug_log_dir = os.path.join(log_root_dir, 'debug')
    # Create a root log directory if it doesn't exist
    os.makedirs(debug_log_dir, exist_ok=True)
    
    # Create a log file with today's date
    debug_log_path = os.path.join(debug_log_dir, f'{time}.log')
    # Create a FileHandler for debug logs and set the format
    debug_file_handler = logging.FileHandler(debug_log_path)
    # Set the format
    debug_file_handler.setFormatter(log_format)
    # Add the FileHandler to the logger
    debug_logger.addHandler(debug_file_handler)

    # Add a StreamHandler to print logs to the terminal
    debug_stream_handler = logging.StreamHandler()
    # Set the format
    debug_stream_handler.setFormatter(log_format)
    # Add the StreamHandler to the logger
    debug_logger.addHandler(debug_stream_handler)

    return debug_logger

def create_warning_logger(name: str) -> logging.Logger:
    # Create and configure a warning logger
    warning_logger = logging.getLogger(name)
    warning_logger.setLevel(logging.WARNING)

    # Create a FileHandler for warning logs and set the format
    warning_log_dir = os.path.join(log_root_dir, 'warning')
    # Create a root log directory if it doesn't exist
    os.makedirs(warning_log_dir, exist_ok=True)
    
    # Create a log file with today's date
    warning_log_path = os.path.join(warning_log_dir, f'{time}.log')
    # Create a FileHandler for warning logs and set the format
    warning_file_handler = logging.FileHandler(warning_log_path)
    # Set the format
    warning_file_handler.setFormatter(log_format)
    # Add the FileHandler to the logger
    warning_logger.addHandler(warning_file_handler)

    # Add a StreamHandler to print logs to the terminal
    warning_stream_handler = logging.StreamHandler()
    # Set the format
    warning_stream_handler.setFormatter(log_format)
    # Add the StreamHandler to the logger
    warning_logger.addHandler(warning_stream_handler)

    return warning_logger

# Example usage:
if __name__ == "__main__":
    info_logger = create_info_logger("info_logger")
    error_logger = create_error_logger("error_logger")
    debug_logger = create_debug_logger("debug_logger")

    info_logger.info("This is an info message.")
    error_logger.error("This is an error message.")
    debug_logger.debug("This is a debug message.")
