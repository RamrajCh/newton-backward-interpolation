from math import factorial as F
import terminaltables

def calculate_multiplication_coeff(p,n):
    # Coeff for nth term is (p(p+1)(p+2)....(p+n-1)) / n! 

    temp = p
    for i in range(1,n-1):
        temp = temp * (p+i)
    return temp / F(n-1)

class Interpolation:
    def __init__(self, x_values:list, y_values:list, x:float):
        # Initialize data values
        self.x = float(x)
        self.x_values = x_values
        self.y_values = y_values
        
        # Call function to create and print backward difference table
        self.n = len(self.x_values)
        self.diff_table = self.create_diff_table()
        self.print_diff_table()

        # Function call to calculate and print. Pass row Yn in the function
        self.calculate_interpolation(self.diff_table[-1])


    def create_diff_table(self):
        #No. of columns in diff table
        m = self.n + 1

        #Initialize diff table with first row
        final_diff_table = [['x','y', '\N{white down-pointing triangle}']]
        
        for g in range(3,m):
            final_diff_table[0].append('\N{white down-pointing triangle}'+str(g-1))

        #Initialize a empty temporary diff table
        temp_diff_table = []

        # Append x and y values in temporary difference table
        for i in range(0,self.n):
            diff_table_row = []
            diff_table_row.append(self.x_values[i])
            diff_table_row.append(self.y_values[i])
            while len(diff_table_row) < m:
                diff_table_row.append(0)
            temp_diff_table.append(diff_table_row)
        
        #Append differences in temporary difference table
        for j in range(1,self.n):
            for k in range (2,m):
                temp_diff_table[j][k] = round(temp_diff_table[j][k-1] - temp_diff_table[j-1][k-1],6)

        # Remove unwanted datas from temporary diff table and append all rows to final diff table
        for p in range(0,self.n):
            final_diff_table_row = []
            for q in range(0,p+2):
                final_diff_table_row.append(temp_diff_table[p][q])
            final_diff_table.append(final_diff_table_row)

        return final_diff_table


    def print_diff_table(self):
        # Print diff table by calling SingleTable function of terminaltables module
        diff_table = terminaltables.SingleTable(self.diff_table)
        diff_table.title = 'Backward Difference Table'
        print(diff_table.table)


    def calculate_interpolation(self, Yn):
        #sample Yn = [x_n, y_n, nabla(y_n), nabla2(y_n), nabla3(y_n), ...]

        # Find difference in x_values i.e h and calculate p
        h = self.x_values[1] - self.x_values[0]
        p = (self.x - self.x_values[-1]) / h

        #Initialize result with y_n as in sample
        result = Yn[1]
        
        # For every data in Yn after y_n i.e. after index 2, 
        # find multiplication coeff (done by calling function calculate_multiplication_coeff(p, index)), 
        # multiply it with correspomding data and add to result  
        m = len(Yn)
        for i in range(2,m):
            coeff = calculate_multiplication_coeff(p,i)
            result = result + (coeff * Yn[i])
        
        # Round obtained result to six decimal places and print result
        result = round(result,6)
        print('Y(%s)'%str(self.x)+' = '+str(result))


if __name__ == "__main__":
    #i = Interpolation(5,1,2,2,4,3,6,4,8)
    i = Interpolation([15,20,25,30,35,40],[0.2588190,0.3420201,0.4226183,.5,0.5735764,0.6427876],43)
    # print(i.x_values)
    # print(i.y_values)

