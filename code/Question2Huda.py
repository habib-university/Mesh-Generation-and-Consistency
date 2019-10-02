import math
import numpy as np
import statistics


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
        v += '\n'
        return v

    def cross_product(self,point2):
        self.normal_points = np.cross(self.points, point2.points)
        return Vector(self.normal_points)

    def normalize(self):
        return np.linalg.norm(self.points)


class Face:
    def __init__(self,f_ind):
        """
        :param f_ind: the vertex indexes which make up the face
        """
        self.ind = np.array(f_ind)

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
        v1 = vertices[self.ind[0]] # A
        v2 = vertices[self.ind[1]] # B
        v3 = vertices[self.ind[2]] # C
        dsp1 = Vector(v1.points - v3.points) #CA
        dsp2 = Vector(v2.points - v3.points) #CB
        return dsp1.cross_product(dsp2) # CA cross CB

    def face_consistent(self):
        """ order or cross product changes the orientation of the surface (direction of normal)"""
        # CA cross CB is now CB cross CA. Swap indexes of vertices of A & B
        self.ind[0], self.ind[1] = self.ind[1], self.ind[0]

    def area_of_face(self,vertices):
        if len(vertices) == 3: #if triangle
            # a = np.array(self.face_normals(vertices))
            # print (a.normalize())
            return 0.5 * self.face_normals(vertices).normalize()
        else: #quadrilateral
            return self.face_normals(vertices).normalize()

    def check_vertex_in_face(self,i):
        return i in self.ind


class Mesh:
    def __init__(self, in_file):
        """
        :param in_file: txt file taken as input
        """
        txt_file = open(in_file)
        self.vertices = [] # list of vertices
        self.faces = [] # list of faces

        self.tuple_vertices = []
        self.inconsistent_list = []
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
        Assumption: all faces are co-planar
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
            return inw
        elif len(out) < len(inw): # out are inconsistent
            return out
        elif len(out) == 0 or len(inw) == 0:  # all consistent
            return []

    def all_faces_consistent(self):
        inconsistent_list = self.inconsistent()
        for i in inconsistent_list:
            self.faces[i].face_consistent()

    def find_all_edges(self):
        all_edges = {}
        for i in self.faces:
            face_ind = i.ind
            for j in range(len(face_ind)):
                if j == len(face_ind)-1:
                    edge = (face_ind[j],face_ind[0])
                else:
                    edge = (face_ind[j],face_ind[j+1])

                if edge in all_edges:
                    all_edges[edge].append(i)
                else:
                    all_edges[edge] = [i]
        return all_edges

    def nonmanifold_edges(self):
        """
        mesh should be consistent, all edges belong to 2 triangles and all vertices have a single continuous set of triangles around them.
        :return: a tuple. At index 0 it returns True if mesh is a manifold, False otherwise. At index 1 it return the list of non-manifold edges.
        """
        all_edges = self.find_all_edges()
        non_manifold_edges = []
        for i in all_edges:
            if len(all_edges[i]) != 2:
                non_manifold_edges.append(i)

        if len(self.inconsistent()) == 0 and len(non_manifold_edges) == 0: #if mesh is a manifold
            return True,non_manifold_edges
        else:
            return False,non_manifold_edges

    def faces_connected_to_vertex(self):
        vertices_dict = {}
        for i in range(self.count_vertices):
            vertices_dict[i] = []  # all vertices indexes must be in the dict
            for j in range(self.count_faces):
                face_to_check = self.faces[j]
                if face_to_check.check_vertex_in_face(i):
                    vertices_dict[i].append(j)
        return vertices_dict
    
    def area_of_mesh(self):
        sum = 0
        for i in self.faces:
            sum = sum + i.area_of_face(self.vertices)
        return sum
