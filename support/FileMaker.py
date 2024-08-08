import os
from datetime import datetime

def GetFileNames():
    timestamp = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    # Current file path
    current_file    = os.path.abspath(__file__)
    # Base directories
    base_directory  = os.path.dirname(os.path.dirname(current_file))
    log_directory   = os.path.join(base_directory, 'logs')
    # End directories
    error_directory = os.path.join(log_directory, 'error')
    exec_directory  = os.path.join(log_directory, 'execution')
    file_directory  = os.path.join(base_directory, 'files')

    # Create files paths
    file_error = os.path.join(error_directory, "er." + timestamp + ".csv"   )
    file_exec  = os.path.join(exec_directory,  "ex." + timestamp + ".csv"   )
    file_name1 = os.path.join(file_directory,  "1.responseCompressed.json"  )
    file_name2 = os.path.join(file_directory,  "2.responseDecompressed.json")
    file_name3 = os.path.join(file_directory,  "3.responseFormated.csv"     )
    file_name4 = os.path.join(file_directory,  "4.responseFormatedFixed.csv")
    file_name5 = os.path.join(file_directory,  "5.requestData.csv"          )

    # Check if every directory exists and if not, create it
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    if not os.path.exists(error_directory):
        os.makedirs(error_directory)
    if not os.path.exists(exec_directory):
        os.makedirs(exec_directory)
    if not os.path.exists(file_directory):
        os.makedirs(file_directory)
    
    # Create files
    open(file_error, 'w').close()
    open(file_exec,  'w').close()
    open(file_name1, 'w').close()
    open(file_name2, 'w').close()
    open(file_name3, 'w').close()
    open(file_name4, 'w').close()
    open(file_name5, 'w').close()
        
    return [
        file_error,
        file_exec,
        file_name1,
        file_name2,
        file_name3,
        file_name4,
        file_name5
    ]