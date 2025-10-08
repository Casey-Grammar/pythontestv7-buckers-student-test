
#Task 1a Echo
'''
Task 1 Echo (3marks)
Part a
When you shout across a valley you can often hear an echo back. Write a program to echo back whatever you say to it. Your program should work like this:
=========================
Shout: hello
hello hello hello
=========================  
'''
def main():
    x="Task1a"
    #===============================
    # Write your code here
    var = input('Shout: ')
    print(f'{var} {var} {var}')
    

    # End of your code here
    #===============================

if __name__ == '__main__':
    main()
