import os
import re
# import sys
# current_dir = os.path.abspath(os.path.dirname(__file__))
# sys.path.append(current_dir)
# sys.path.append("..")
from MyException import MyException
def get_files(source_path):
    """

    :param source_path: 文件绝对路径
    :return: 获取文件名字,如果没有路径则报错
    """
    if not exist_file(source_path):
        raise MyException.FileErrorException('no file found,please check your source_path')
    return [os.path.join(source_path,file)for file in next(os.walk(source_path))[2]]


def get_folder_names(source_path):
    """

    :param source_path: 文件绝对路径
    :return: 获取文件上级目录,如果没有路径则报错
    """
    if not exist_file(source_path):
        raise MyException.FileErrorException('no file found,please check your source_path')
    return [os.path.join(source_path,file)for file in next(os.walk(source_path))[1]]


def get_files_by_extension(source_path='.', extension_name='pdf'):
    """
    寻找目录下指定格式的文件
    :source_path 需要搜索的目录:
    :extension_name 文件扩展名字符串:
    :return: 文件列表
    """
    if not exist_file(source_path):
        raise MyException.FileErrorException('no file found,please check your source_path')
    pattern=r'.+?\.'+extension_name
    filename=get_files(source_path)
    return [os.path.join(source_path, file) for file in filename if re.match(pattern, file)]


def get_father_path(filename):
    return os.path.dirname(filename)


def get_curdir():
    """
    :return: 获取当前目录
    """
    return os.getcwd()
def check_extension(file_path,extension_name='pdf'):
    """

    :param file_path: 文件路径
    :param extension_name: 扩展名
    :return: 如果符合扩展名则返回True
    """
    pattern = r'.+?\.' + extension_name
    if re.match(pattern,file_path):
        return True
    return False
def exist_file(file_path):
    return os.path.exists(file_path)
