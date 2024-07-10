from typing import Optional
from logs.create_logs import create_info_logger, create_error_logger, create_debug_logger, create_warning_logger


class BirdLogger:
    """
    A custom logger class for managing and logging messages with different log levels.

    Attributes:
        info_logger (logging.Logger): Logger for INFO level messages.
        error_logger (logging.Logger): Logger for ERROR level messages.
        debug_logger (logging.Logger): Logger for DEBUG level messages.
        warning_logger (logging.Logger): Logger for WARNING level messages.
    """

    # Create and configure shared loggers for all instances
    info_logger = create_info_logger("shared_info_logger")
    error_logger = create_error_logger("shared_error_logger")
    debug_logger = create_debug_logger("shared_debug_logger")
    warning_logger = create_warning_logger("shared_warning_logger")

    def __init__(self, name: str = 'default'):
        """
        Initialize a custom logger instance with a given name.

        Args:
            name (str, optional): The name associated with this logger instance. Default is 'default'.
        """
        self.name = name

    def info(self, message: str) -> None:
        """
        Log an INFO level message.

        Args:
            message (str): The message to be logged.
        """
        BirdLogger.info_logger.info(f"{self.name} - {message}")

    def error(self, message: str, code: Optional[str] = None) -> None:
        """
        Log an ERROR level message.

        Args:
            message (str): The message to be logged.
            code (Optional[str], optional): The error code. Default is None.
        """
        if code:
            BirdLogger.error_logger.error(
                f"{self.name} -  {code}: {message}")
        else:
            BirdLogger.error_logger.error(f"{self.name} - {message}")

    def debug(self, message: str) -> None:
        """
        Log a DEBUG level message.

        Args:
            message (str): The message to be logged.
        """
        BirdLogger.debug_logger.debug(f"{self.name} - {message}")

    def warning(self, message: str) -> None:
        """
        Log a WARNING level message.

        Args:
            message (str): The message to be logged.
        """
        BirdLogger.warning_logger.warning(f"{self.name} - {message}")
