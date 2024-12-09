import shutil
import os

def copy_file(source, destination):
    """
    Copies a file from source to destination
    :param source: file to be copied
    :param destination: copy path
    :return:
    """
    shutil.copyfile(source, destination)


def clear_file(file_name):
    """
    Deletes all content of a file
    :param file_name: the name of the file whose content will be deleted
    :return:
    """
    with open(file_name, "w") as file:
        file.write("")
