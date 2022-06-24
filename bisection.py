def n_root():
    """ this program is uses to find nth root of any number.
 For this I have used Construction of bisection method!!!!!!! """
    print(f'Wel-come\nProgram to find "n"th  root of any number "z"')
    while True:
        try:
            n = int(input("Enter value of n : "))  # nth root
            z = int(input("Enter the value of z: "))  # number for which nth root to be found
        except ValueError:
            print("Only integers are allowed.....\nEnter again.....  ")  # if number n or z entered incorrect

        else:
            y = 100   # take count for iteration for bisection method
            x_n = 0  # iterated value of result
            for x in range(0, 100):
                c = x**n-z  # finding a0, b0
                d = (x+1)**n-z
                if (c < 0 | d > 0) or (c > 0 | d < 0):  # to check the
                    a = x  # taking values for an and bn
                    b = x+1
                    while y > 0:
                        x_n = (a + b) / 2
                        f_x = x_n ** n - z
                        y = y - 1
                        if f_x < 0:
                            a = x_n
                        else:
                            b = x_n
                    else:
                        print(f'{n}th root of {z} is: {x_n}')
                    break
                if c == 0:
                    print(f'{n}th root of {z} is: {x}')
                    break
            y = input("Do you want to continue [y/n] : ")
            while y.lower() not in ('n', 'no', 'y', 'yes'):
                print("Enter correct option.......")
                y = input("you want to continue [y/n] : ")
            else:
                if y.lower() in ('n', 'no'):
                    print("Thank You !!!!")
                    break
                else:
                    continue


print(n_root.__doc__)
n_root()
