'''
Savannah Smith
M02 Lab - Case Study: if...else and while
This Python app will accept student names and GPAs
and test if the student qualifies for either the Dean's List or the Honor Roll.
'''

def main():
    while True:
        last_name = input("Enter student's last name (or 'ZZZ' to quit): ") # Asking user for Last Name or to quit the program
        if last_name == 'ZZZ':
            print("Exiting program...")
            break
        
        first_name = input("Enter student's first name: ") # Asking user for First Name
        gpa = float(input("Enter student's GPA: ")) # Asking user for GPA 
        
        if gpa >= 3.5: # Check if GPA is a 3.5 or above (deans list)
            print(f"{first_name} {last_name} has made the Dean's List.")



if __name__ == "__main__":
    main()
