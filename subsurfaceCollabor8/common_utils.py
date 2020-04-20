import os


def create_filepath_if_not_exists(filepath):
    """
    Creates the given filepath path if not existing
    """
    dirname=os.path.dirname(filepath)
    #check if it exists or not
    if os.path.exists(dirname)==False:
        os.makedirs(dirname)