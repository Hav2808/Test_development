import pytest

from main_1 import YaUploader, token
import os

def test_1(): # тест на наличие папки
    path = 'test.txt'
    os.path.exists(path)

def test_2():
    uploader = YaUploader(token)
    etalon = 200
    result = uploader.get_files_list()
    assert result == etalon

def test_3():
    uploader = YaUploader(token)
    etalon = 201
    result = uploader.upload(path = 'path', file_name ='../test.txt')
    assert result == etalon

@pytest.mark.parametrize('result',[(200), (201), (301), (404)])

def test_4(result):
    uploader = YaUploader(token)
    res = uploader.upload(path='path', file_name='test.txt')
    assert res == result