'''
Savannah Smith
M02 Lab - Case Study: if...else and while
This Python app will accept student names and GPAs
and test if the student qualifies for either the Dean's List or the Honor Roll.
'''

def main():
    while True:
        last_name = input("Enter student's last name (or 'ZZZ' to quit): ")
        if last_name == 'ZZZ':
            print("Exiting program...")
            break
        
        first_name = input("Enter student's first name: ")
        gpa = float(input("Enter student's GPA: "))
        
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} does not qualify for any honors.")
        print()  # Just for spacing


if __name__ == "__main__":
    main()
