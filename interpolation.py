from math import factorial as F
from terminaltables import SingleTable as Table

def calculate_multiplication_coeff(p,n):
    temp = p
    for i in range(1,n-1):
        temp = temp * (p+i)
    return temp

class Interpolation:
    def __init__(self, x_values, y_values, x):
        self.x = float(x)
        self.x_values = x_values
        self.y_values = y_values
        self.n = len(self.x_values)
        self.diff_table = self.create_diff_table()
        self.print_diff_table()
        self.result = self.calculate_interpolation(self.diff_table[-1])
        print('Y(%s)'%str(self.x)+' = '+str(self.result))

    def create_diff_table(self):
        final_diff_table = [['x','y', '\N{white down-pointing triangle}']]
        diff_table = []
        m = self.n + 1
        
        for g in range(3,m):
            final_diff_table[0].append('\N{white down-pointing triangle}'+str(g-1))

        for i in range(0,self.n):
            diff_table_row = []
            diff_table_row.append(self.x_values[i])
            diff_table_row.append(self.y_values[i])
            while len(diff_table_row) < m:
                diff_table_row.append(0)
            diff_table.append(diff_table_row)
        
        for j in range(1,self.n):
            for k in range (2,m):
                diff_table[j][k] = round(diff_table[j][k-1] - diff_table[j-1][k-1],6)
        
        for p in range(0,self.n):
            final_diff_table_row = []
            for q in range(0,p+2):
                final_diff_table_row.append(diff_table[p][q])
            final_diff_table.append(final_diff_table_row)

        return final_diff_table

    def print_diff_table(self):
        diff_table = Table(self.diff_table)
        diff_table.title = 'Backward Difference Table'
        print(diff_table.table)

    def calculate_interpolation(self, Yn):
        h = self.x_values[1] - self.x_values[0]
        p = (self.x - self.x_values[-1]) / h
        result = Yn[1]
        m = self.n + 1
        for i in range(2,m):
            coeff = calculate_multiplication_coeff(p,i) / F(i-1)
            result = result + (coeff * Yn[i])
        return round(result,6)


if __name__ == "__main__":
    #i = Interpolation(5,1,2,2,4,3,6,4,8)
    i = Interpolation([15,20,25,30,35,40],[0.2588190,0.3420201,0.4226183,.5,0.5735764,0.6427876],43)
    # print(i.x_values)
    # print(i.y_values)

