#!/usr/bin/python3
"""List Challenge"""

def main():
    #Part 1
    wordbank= ["indentation", "spaces"]
    
    #Part 2
    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "Louis", "Mabel", "Paul", "Zach"]
    
    #Part 3
    wordbank.append(4)
    
    #Part 4
    inNum = int(input("Enter a number between 0 and 17: "))

    #Part 5
    student_name = tlgstudents[inNum]

    #Part 6
    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")

if __name__ == "__main__":
    main()
