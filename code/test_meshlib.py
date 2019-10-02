import numpy as np
from MeshLib import *

# vq = Mesh('validQuadrilateralMesh.txt')
# vt = Mesh('validTriangleMesh.txt')
# vtq = Mesh('validTriQuadMesh.txt')
# g1 = Mesh('geometry1.txt')
g2 = Mesh('geometry2.txt')
# g3 = Mesh('geometry3.txt')
# g4 = Mesh('geometry4.txt')
# g5 = Mesh('geometry5.txt')
# g6 = Mesh('geometry6.txt')


# def test__conversion_to_obj():
# 	assert True == vq.parser('validQuadrilateralMesh')
# 	assert True == vt.parser('validTriangleMesh')
# 	assert True == vtq.parser('validTriQuadMesh')
# 	assert True == g1.parser('geometry1')
# 	assert True == g2.parser('geometry2')
# 	assert True == g3.parser('geometry3')
# 	assert True == g4.parser('geometry4')
# 	assert True == g5.parser('geometry5')
# 	assert True == g6.parser('geometry6')

# def test__area_of_mesh():
# 	assert 11.5 == round(vt.area_of_mesh(), 1)
# 	assert 17207.8 == round(g4.area_of_mesh(), 1)
# 	assert 17207.8 == round(g5.area_of_mesh(),1)

# def test__inconsistent():
	# assert [] == vq.inconsistent()
	# assert [] == vt.inconsistent()
	# assert [] == vtq.inconsistent()
	# assert 0 != len(g1.inconsistent())
	# assert [] = len(g2.inconsistent())
	# assert [] = len(g3.inconsistent())
	# assert 0 != len(g4.inconsistent())
	# assert 0 != len(g5.inconsistent())
	# assert 0 != len(g6.inconsistent())

# def test__nonmanifold():
# 	assert True == vt.nonmanifold_edges()[0]
# 	assert True == vq.nonmanifold_edges()[0]
# 	assert True == vtq.nonmanifold_edges()[0]
# 	assert False == g1.nonmanifold_edges()[0]
# 	assert True == g2.nonmanifold_edges()[0]
# 	assert True == g3.nonmanifold_edges()[0]
# 	assert False == g4.nonmanifold_edges()[0]
# 	assert False == g5.nonmanifold_edges()[0]
# 	assert False == g6.nonmanifold_edges()[0]

def test__validverticesdict():
	# assert len(vt.vertices) == len(vt.faces_connected_to_vertex())
	# assert len(vq.vertices) == len(vq.faces_connected_to_vertex())
	# assert len(vtq.vertices) == len(vtq.faces_connected_to_vertex())
	# assert len(g1.vertices) == len(g1.faces_connected_to_vertex())
	assert len(g2.vertices) == len(g2.faces_connected_to_vertex())
	# assert len(g3.vertices) == len(g3.faces_connected_to_vertex())
	# assert len(g4.vertices) == len(g4.faces_connected_to_vertex())
	# assert len(g5.vertices) == len(g5.faces_connected_to_vertex())
	# assert len(g6.vertices) == len(g6.faces_connected_to_vertex())

# Pytest requires its test functions to be prefixed with 'test_xxx' as shown below. https://docs.pytest.org/en/latest/.
# Helper/private functions can be named in whatever way you like
# def test_readTxtFile_invalidInputFile_returnsException():
# 	assert False == readTxtFile();
#
# def test_readTxtFile_validFile_returnsSuccess():
#  	assert True == readTxtFile();
#
# # The following test cases only work for square matrices defined above
# def test_computeArea():
#     assert 0.1 == computeArea();
