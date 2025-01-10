import sys
import logging

def error_message_detail(error: Exception, error_detail: sys) -> str :
    # Extract traceback details (exception information)
    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    # Create a formatted error message string with file name, line number, and the actual error
    line_number = exc_tb.tb_lineno

    error_message = f"Error message occured in python script: [{file_name}] at the line  number [{line_number}]"

    # log the error message
    logging.error(error_message)

    return(error_message)


class MyException(Exception):
    def __init__(self, error_message: str, error_detail: sys):
      # Call the base class constructor with the error message
        super().__init__(error_message)
        
        self.error_message = error_message_detail(error_message,error_detail)


    def __str__(self):
         return self.error_message 