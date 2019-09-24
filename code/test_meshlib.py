import numpy as np
from MeshLib import *




# Pytest requires its test functions to be prefixed with 'test_xxx' as shown below. https://docs.pytest.org/en/latest/. 
# Helper/private functions can be named in whatever way you like
def test_readTxtFile_invalidInputFile_returnsException():
	assert False == readTxtFile();

def test_readTxtFile_validFile_returnsSuccess():
 	assert True == readTxtFile();

# The following test cases only work for square matrices defined above
def test_computeArea():
    assert 0.1 == computeArea();
