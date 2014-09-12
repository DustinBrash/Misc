__name__ = "Matrix"
import copy
class Matrix(object):

    def __init__(self, two_d_array):
        self.matrix = two_d_array
        self.rows = len(self.matrix[0])
        self.columns = len(self.matrix)

    def __repr__(self):
        out = ''
        for row in self.matrix:
            out += str(row) + '\n'
        return out

    def get_deter(self):
        old_col = self.columns
        new_matrix = copy.copy(self.matrix)
        test_pos = []
        test_neg = []
        total = 0
        if old_col == 2:
            return new_matrix[0][0] * new_matrix[1][1] - new_matrix[0][1] * new_matrix[1][0]
        else:
            for n in range(old_col):
                for N in range(old_col):
                    new_matrix[n].append(new_matrix[n][N])
            new_col = len(new_matrix)
            self.test = new_matrix
            
            for n in range(old_col):
                pos_sum = 1
                neg_sum = 1
                for nI in range(old_col):
                    print n, nI
                    print n, -1 - nI - n
                    pos_sum =  pos_sum * new_matrix[nI][nI + n]                    
                    neg_sum = neg_sum * new_matrix[nI][-1 - nI - n]                    
                test_pos.append(pos_sum)
                test_neg.append(neg_sum)
                total += pos_sum - neg_sum
            return total

test = [[1, 1, 1,1], [1, 1, 1,1], [1, 1,1,1], [1,1,1,1]]

Mat = Matrix(test)
print Mat.get_deter()
