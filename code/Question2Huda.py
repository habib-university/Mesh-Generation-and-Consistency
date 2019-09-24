import math
import  numpy as np

class Vertex_Vect:
    def __init__(self, vertices):
        """
        :param vertices: tuple of co-ordinates
        """
        self.points = np.array(vertices)

    def ver_to_obj(self):
        v = 'v'
        for i in self.points:
            v+= ' ' + str(i)
        v+= '\n'
        return v

class Face:
    def __init__(self,f_ind):
        """
        :param f_ind: the vertex indexes which make up the face
        """
        self.ind = f_ind

    def f_to_obj(self):
        f = 'f'
        for i in self.ind:
            f += ' ' + str(i+1)
        f += '\n'
        return f

class Mesh:
    def __init__(self, in_file):
        """
        :param in_file: txt file taken as input
        """
        txt_file = open(in_file)
        self.vertices = [] # list of vertices
        self.faces = [] #list of faces
        #first line in txt file contains count of vertices & faces in order

        #self.count_vertices = int(txt_file.readline().strip().split())
        #self.count_faces = int(txt_file.readline().strip().split()[1])

        self.count_vertices, self.count_faces = (int(i) for i in txt_file.readline().strip().split())

        print (self.count_vertices, self.count_faces)
        for i in range(self.count_vertices):
            vertex = tuple(float(i) for i in txt_file.readline().strip().split())
            self.vertices.append(Vertex_Vect(vertex))

        for i in range(self.count_faces):
            f = tuple(int(i) for i in txt_file.readline().strip().split())
            self.faces.append(Face(f))  # f is the index of vertices in the face

    def parser(self):
        mesh_file = open('meramesh.obj', 'w')

        for i in range(self.count_vertices):
            mesh_file.write(self.vertices[i].ver_to_obj())

        for i in range(self.count_faces):
            mesh_file.write(self.faces[i].f_to_obj())


'''
        for i in range(self.count_faces):
            f = tuple(float(i) for i in txt_file.readline().strip().split())
            self.faces.append(Face(f)) #f is the index of vertices in the face
        '''

mesh1 = Mesh('validTriangleMesh.txt')
print (mesh1.parser())









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