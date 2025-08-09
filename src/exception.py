'''
This is where we define costum exception classes
ie defining our own error instead of python build in exception like
ValueError, FileNotFound etc

simple words 
Read the python error and make it your own costume
'''


'''
*sys* This is used to interact with python runtime (time between run - finish)
1) Error/exception handling
2) Cheack running path
'''
import sys
import logging
from src.logger import logging #to lof the error

def error_message_detail(error,error_detail:sys): # error and error_detail is part of sys
    # error_detail.exc_info() will give us three types of information
    # But the 3rd one is usefull for us with has what error and which line
    _,_,exc_tb = error_detail.exc_info() #tb - traceback

    # so now we have on which file and what error is occured in exc_tb
    
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occured in in python scipt name [{0}], line number [{1}], error message[{2}]".format(
        file_name,
        exc_tb.tb_lineno,
        str(error)
    )

    return error_message

# So whenever error raises then call (error_massage_detail)

class ConstumException(Exception): #this Exception is from python
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message) # This is used to ensure the parent class (Exception) is properly inherited from python before moving further
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
    
if __name__=='__main__':
    try:
        1/0
    except Exception as e:
        logging.info("Diveded by zero error")
        raise ConstumException(e, sys)