import sys
from src.ML_Project.logger import logging

def error_msg_details(error,details:sys):
    # exc_info() returns 3 values
    # (1) Exception type (2)Exception value (3)Traceback obj - where the error happened
    _,_,exc_tb = details.exc_info()
    # exc_tb.tb_frame.f_code.co_filename - Gets the filename of python scripts where the error occured
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_msg = "Error occured in python script name [{0}] line number [{1}] error message".format(
        file_name,exc_tb.tb_lineno,str(error))
    
    return error_msg


class CustomException(Exception):
    def __init__(self,error_msg,error_details:sys):
        super().__init__(error_msg)
        self.error_msg = error_msg_details(error_msg,error_details)

    def __str__(self):
        return self.error_msg