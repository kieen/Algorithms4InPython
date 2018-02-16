class QuickFindUF:
    def __init__(self, N):
        self.id = list(range(N+1))
        self.N=N
    def conncected(self, x, y):
        return self.id[x] == self.id[y]
    def union(self, x, y):
        idx=self.id[x]
        idy=self.id[y]
        for i in range(len(self.id)):
            if self.id[i] == idx:
                self.id[i] = idy
if __name__ == '__main__':
    uf = QuickFindUF(9)
    print(uf.id)
    uf.union(4, 3)
    uf.union(3, 8)
    print(uf.conncected(4, 8))