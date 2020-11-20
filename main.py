from interpolation import Interpolation

def main():

    print ("----------------------Newton Backward Interpolation-------------------------\n\n\n")

    x_values = input('Give x-values separated by space like 10 20 30 ...\t')
    x_values = x_values.split()

    for k in range(0, len(x_values)):
        try:
            x_values[k] = float(x_values[k])
        except ValueError:
            print("Sorry you give string")
            run()
    
    print("-----------------------------------------------------------------------------\n\n\n")

    y_values = []
    l = 0
    while l < len(x_values):
        try:
            y = float(input('Give value of y corresponding to %s\t'%x_values[l]))
            y_values.append(y)
            l += 1
        except ValueError:
            print("Sorry you give string")
            l = l
    
    print("-----------------------------------------------------------------------------\n\n\n")

    error = False
    while not error: 
        try:    
            x = float(input('Give the value of x that you want to find: \t'))
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
