def main():
    while True:
        # Ask for student's name
        name = input("\nEnter student's name (or type 'exit' to quit): ")
        if name.lower() == 'exit':
            print("Exiting calculator...")
            break

        # Ask for 3 subject marks
        try:
            mark1 = float(input("Enter marks for Subject 1: "))
            mark2 = float(input("Enter marks for Subject 2: "))
            mark3 = float(input("Enter marks for Subject 3: "))

            # Calculate the average
            average = (mark1 + mark2 + mark3) / 3

            # Determine the grade
            if average >= 75:
                grade = "A"
            elif average >= 60:
                grade = "B"
            elif average >= 40:
                grade = "C"
            else:
                grade = "Fail"

            # Display the results
            print("-" * 30)
            print(f"Name   : {name}")
            print(f"Average: {average:.1f}")
            print(f"Grade  : {grade}")
            print("-" * 30)

        except ValueError:
            print("Error: Please enter valid numeric marks.")

if __name__ == "__main__":
    main()
