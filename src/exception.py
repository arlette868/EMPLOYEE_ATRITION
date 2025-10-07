import sys
import logging

def error_message_detail(error, error_detail: sys):
    """
    Extracts detailed information about an exception:
    - File name where the error occurred
    - Line number of the error
    - The actual error message
    """
    _, _, exc_tb = error_detail.exc_info()           # Extract traceback info
    file_name = exc_tb.tb_frame.f_code.co_filename   # File name where the error happened
    line_number = exc_tb.tb_lineno                   # Line number
    error_message = (
        f"Error occurred in script [{file_name}] "
        f"at line [{line_number}] — message: [{str(error)}]"
    )
    return error_message


class CustomException(Exception):
    """
    Custom Exception class for capturing and formatting detailed error information
    throughout the project.
    """

    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
