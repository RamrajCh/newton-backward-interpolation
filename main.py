from interpolation import Interpolation

def main():

    print ("\n----------------------Newton Backward Interpolation-------------------------\n\n")

    x_values = input('Give evenly separated x-values like 10 20 30 ...\t')
    x_values = x_values.split()

    for k in range(0, len(x_values)):
        try:
            x_values[k] = round(float(x_values[k]),8)
        except ValueError:
            print("Sorry you give string")
            main()
    
    x_values.sort()

    h = round(float(x_values[1] - x_values[0]),8)
    for i in range(1, len(x_values)-1):
        if round(x_values[i+1] - x_values[i],8) != h:
            print("Data points are not separated evenly. Please recheck and try again!!!")
            main()
    
    print("-----------------------------------------------------------------------------\n\n\n")

    y_values = []
    l = 0
    while l < len(x_values):
        try:
            y = round(float(input('Give value of y corresponding to %s\t'%x_values[l])),6)
            y_values.append(y)
            l += 1
        except ValueError:
            print("Sorry you give string")
            l = l
    
    print("-----------------------------------------------------------------------------\n\n\n")

    error = False
    while not error: 
        try:    
            x = float(input('Give Xs that you want to find: \t'))
            error = True
        except ValueError:
            print("Sorry you give string")
            error = False
        

    print("-----------------------------------------------------------------------------\n\n\n")

    i = Interpolation(x_values,y_values,x)

    print("----------------------------------End----------------------------------------\n\n\n")
    return

if __name__ == "__main__":
    main()
