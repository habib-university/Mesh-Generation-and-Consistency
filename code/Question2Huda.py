import math
import  numpy

class Vertex:
    def __init__(self, points):



class Face:

class Mesh:
    def __init__(self, in_file):
        txt_file = open(in_file)
        self.vertices = [] # list of vertices
        self.count_faces = [] #list of faces
        #first line in txt file countains count of vertices & faces in order
        self.count_vertices = txt_file.readline().strip().split()[0]
        self.count_faces = txt_file.readline().strip().split()[1]

        for i in range(self.count_vertices):
            vertex = tuple(float(i) for i in txt_file.readline().strip().split())
            self.vertices.append(vertex)

        for i in range(self.count_faces):
            f = tuple(float(i) for i in txt_file.readline().strip().split())
            self.faces.append(f)










'''
def txt_to_obj(in_file):
    txt_file = open(in_file)
    vertices = [] # list of vertices
    count_faces = [] #list of faces
    #first line in txt file countains count of vertices & faces in order
    count_vertices = txt_file.readline().strip().split()[0]
    count_faces = txt_file.readline().strip().split()[1]

    for i in range(count_vertices):
        vertex = tuple(float(i) for i in txt_file.readline().strip().split())
        vertices.append(vertex)

    for i in range(count_faces):
        f = tuple(float(i) for i in txt_file.readline().strip().split())
        faces.append(f)

    mesh_file = open('validmesh.obj', 'w')
    for i in range(count_vertices):
        vertex =
'''

def readTxtFile():
	return True;


def computeArea():
	return 0.1;