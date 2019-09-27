import math
import numpy as np
import  statistics

class Vector:
    def __init__(self, vertices):
        """
        :param vertices: tuple of co-ordinates
        """
        self.points = np.array(vertices)
        self.normal_points = (0,0,0)

    def vertex_to_obj(self):
        v = 'v'
        for i in self.points:
            v+= ' ' + str(i)
        v+= '\n'
        return v

    def cross_product(self,point2):
        self.normal_points = np.cross(self.points, point2.points)
        return Vector(self.normal_points)

    def normalize(self):
        return np.linalg.norm(self.normal_points)


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

    def face_normals(self,vertices):
        """
        :param vertices: list of vectors which make a face, for each face in the mesh
        :return: surface normal of the face
        """
        v1 = vertices[self.ind[0]]
        v2 = vertices[self.ind[1]]
        v3 = vertices[self.ind[2]]
        dsp1 = Vector(v1.points - v3.points)
        dsp2 = Vector(v2.points - v3.points)
        return dsp1.cross_product(dsp2)


class Mesh:
    def __init__(self, in_file):
        """
        :param in_file: txt file taken as input
        """
        txt_file = open(in_file)
        self.vertices = [] # list of vertices
        self.faces = [] # list of faces

        self.tuple_vertices = []

        # first line in txt file contains count of vertices & faces in order
        self.count_vertices, self.count_faces = (int(i) for i in txt_file.readline().strip().split())

        for i in range(self.count_vertices):
            vertex = tuple(float(i) for i in txt_file.readline().strip().split())
            self.tuple_vertices.append(vertex)
            self.vertices.append(Vector(vertex))

        for i in range(self.count_faces):
            f = tuple(int(i) for i in txt_file.readline().strip().split())
            self.faces.append(Face(f))  # f is the index of vertices in the face

    def parser(self):
        """
        :return obj file in the current directory
        """
        mesh_file = open('meramesh.obj', 'w')

        for i in range(self.count_vertices):
            mesh_file.write(self.vertices[i].vertex_to_obj())
        for i in range(self.count_faces):
            mesh_file.write(self.faces[i].f_to_obj())

    def center_of_mesh(self):
        x=[]
        y=[]
        z=[]
        for i in self.tuple_vertices:
            x.append(i[0])
            y.append(i[1])
            z.append(i[2])
        self.center = Vector([statistics.mean(x),statistics.mean(y),statistics.mean(z)])
        return self.center

    def vector_orientation(self, current_face, current_surface_normal):
        """
        dot product is >0 for outward pointing vectors and <0 for inward point vectors
        """
        vector_face = self.vertices[current_face.ind[0]] # fixing face vector to vector on first index of the face
        displacement_f_to_c = Vector(vector_face.points - self.center_of_mesh().points)
        return np.dot(displacement_f_to_c.points, current_surface_normal.points)

    def all_normals(self):
        all_normals = []
        for i in self.faces:
            all_normals.append(i.face_normals(self.vertices))
        return all_normals

    def inconsistent(self):
        """
        :return: True if mesh is consistently oriented, False otherwise
        """
        self.inconsistent_list = []
        out = [] # dot product > 0
        inw = [] # dot product < 0
        normals = self.all_normals()
        for i in range(len(normals)):
            dot_product = self.vector_orientation(self.faces[i],normals[i])
            if dot_product > 0:
                out.append(self.faces[i])
            elif dot_product < 0:
                inw.append(self.faces[i])

        if len(out) >= len(inw): # inw are inconsistent. even if equal then inw are inconsistent
            self.inconsistent_list = inw
            return False
        elif len(out) < len(inw): # out are inconsistent
            self.inconsistent_list = out
            return False
        elif len(out) == 0 or len(inw) == 0: # all consistent
            self.inconsistent_list = []
            return False


mesh1 = Mesh('geometry2.txt')
print(len(mesh1.inconsistent()))
#print(mesh1.vector_orientation())

def readTxtFile():
	return True


def computeArea():
	return 0.1