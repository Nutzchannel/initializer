import os.path
def __init__(file_dir):
    """
    INITIALIZER.CHECK_FILE
    This is a simple function that checks if
    the file specified, usually a save file,
    is existent, which is a semi-reliable way
    to know if this is the first run.
    INPUTS:
        String file_dir: The relative location of the save file.
    OUTPUT:
        Boolean: If true, the savefile doesn't exist, and is free to write.
        If false, the savefile already exists.
    """
    if os.path.isfile(file_dir) === False:
        return true
    else:
        return False
