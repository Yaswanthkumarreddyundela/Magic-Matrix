#function to create a magic square of odd order.
def odd_mat(n):
    """This function only returns a magic square of odd order,
    even number inputs will result in showing error."""
    #creating an empty matrix of order n with all values zero so that they can be filled later.
    magicSquare = [[0 for x in range(n)]
                   for y in range(n)]
    # initialize position of 1
    i = n // 2
    j = n - 1
    # Fill the magic square
    num = 1
    while num <= (n * n):
        if i == -1 and j == n:
            j = n - 2
            i = 0
        else:

            if j == n:
                j = 0

            if i < 0:
                i = n - 1

        if magicSquare[int(i)][int(j)]:
            j = j - 2
            i = i + 1
            continue
        else:
            magicSquare[int(i)][int(j)] = num
            num = num + 1

        j = j + 1
        i = i - 1
    return magicSquare

#function to create magic square of doubly even order.
def doubly_square(n):
    """This function only returns magic square for doubly even numbers (i.e., 4*n)
    other inputs will result in showing error or return a matrix which is not a magic square."""
    # creating an empty matrix of order n with all values zero so that they can be filled later.
    mat=[[0 for i in range(n)] for j in range(n)]
    count=0
    for i in range(0,n):
        for j in range(0,n):
            count+=1
            mat[i][j]=count
    #filling up the top left part of the matrix.
    def top_left(n):
        for i in range(0,n//4):
            for j in range(0,n//4):
                mat[i][j]=(n*n+1)-mat[i][j]

    # filling up the top right part of the matrix.
    def top_right(n):
        for i in range(0,n//4):
            for j in range(3*(n//4),n):
                mat[i][j]= (n*n+1)-mat[i][j]

    # filling up the bottom left part of the matrix.
    def bottom_left(n):
        for i in range((3*n//4),n):
            for j in range(0,n//4):
                mat[i][j]=(n*n+1)-mat[i][j]

    # filling up the bottom right part of the matrix.
    def bottom_right(n):
        for i in range((3*n//4),n):
            for j in range((3*(n//4)),n):
                mat[i][j]=(n*n+1)-mat[i][j]

    # filling up the centre part of the matrix.
    def centre(n):
        for i in range(n//4,3*(n//4)):
            for j in range(n//4,3*(n//4)):
                mat[i][j]=(n*n+1)-mat[i][j]
    top_left(n)
    top_right(n)
    bottom_left(n)
    bottom_right(n)
    centre(n)
    return mat

#function to calculate the sum of elements of each row column and diagonals of a magic square.
def matsum(n):
    """This function returns the sum of elements of each row column and diagonals of a magic square."""
    return (f"Sum of each row, column or diagonal is = {n*(n*n+1)//2} \n")

#Here the program is being executed.
if __name__=="__main__":
    char = "Welcome to the world of magic squares!!!"
    print(char.center(85, "*"))
    a = input("\nPress 'y' to continue or 'n' to exit: ")
    while a == "y":
        n = input("Enter order of matrix:- ")
        if n.isdigit():
            n=int(n)
        else:
            print("Enter a valid input!!!")
            n=int(input("Enter order of matrix:- "))
        if n % 2 != 0 and 2 < n < 100:
            print(matsum(n))
            for i in range(n):
                for j in range(n):
                    print("|" + (str(odd_mat(n)[i][j])).ljust(len(str(max(max(odd_mat(n)))))) + "|", end=" ")
                print()
            print(f"Congratulations! here is your magic square of order {n}")
        elif n / 4 == n // 4 and 2 < n < 100:
            print(matsum(n))
            for i in range(n):
                for j in range(n):
                    print("|" + (str(doubly_square(n)[i][j])).ljust(len(str(max(max(doubly_square(n)))))) + "|",
                          end=" ")
                print()
            print(f"\nCongratulations! here is your magic square of order {n}")
        elif n == (n // 4) * 4 + 2 and 2 < n < 100:
            print("Please enter a number which is not singly even i.e., not equal to (n*4)+2.")
        else:
            print("Please enter a valid order between 3 to 99")

        a = input("\nPress 'y' to continue or 'n' to exit: ")
        if a == "n":
            char2 = "Thank you for interacting with us !!!"
            print(char2.center(85, "*"))