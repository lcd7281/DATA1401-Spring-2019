class matrix:
    def __init__(self, M):
        self.M = M
    def num_row(self):
        r = len(self.M)
        return r
    def num_col(self):
        c = len(self.M[0])
        return c
    def shape(self):
        x = (self.num_row(),self.num_col())
        return x
    def nth_col(self,n):
        out = []
        for i in self.M:
            r = i[n]
            out.append(r)
        return out
    def nth_row(self,n):
        c = self.M[n]
        return c
    def const(self,c):
        list1 = list()
        for row in range(self.num_row()):
            list2 = []
            for col in range(self.num_col()):
                list2.append(float(c))
            list1.append(list2)
        return matrix(list1)
    def zeros(self):
        list3 = list()
        for i in range(self.num_row()):
            list3.append([])
            for j in range(self.num_col()):
                list3[-1].append(float(0))
        return matrix(list3)
    def ones(self):
        list4 = list()
        for i in range(self.num_row()):
            list4.append([])
            for j in range(self.num_col()):
                list4[-1].append(float(1))
        return matrix(list4)
    def eye(self):
        numCols = self.num_col()
        iden=[[0 for x in range(numCols)] for y in range(numCols)]
        for i in range(numCols):
            iden[i][i] = 1
        return iden
    def transpose(self):
        t = []
        for i in range(self.num_col()):
            cv = []
            for j in range(self.num_row()):
                cv.append(self.M[j][i])
                j = j + 1
            t.append(cv)
            i = i + 1
        return matrix(t)
    def scalarmult(self,c):
        t = []
        for i in range(self.num_row()):
            cv = []
            for j in range(self.num_col()):
                cv.append(c*self.M[i][j])
                j = j + 1
            t.append(cv)
            i = i + 1
        return matrix(t)
    def add(self, N):
        if self.shape() != N.shape():
            print "Can not add matrices with different sizes!" 
        t = []
        for i in range(self.num_row()):
            cv = []
            for j in range(self.num_col()):
                cv.append(N.M[i][j]+self.M[i][j])
                j = j + 1
            t.append(cv)
            i = i + 1
        return matrix(t)
    def sub(self, M):
        s = M.scalarmult(-1)
        a = self.add(s)
        return a
    def matmult(self, N):
        m = []
        for i in range(self.num_row()):
            cv = []
            for j in range(N.num_col()):
                sum = 0
                for k in range(N.num_row()):
                    sum+= self.M[i][k]*N.M[k][j]
                cv.append(sum)
            m.append(cv)
        return matrix(m) 