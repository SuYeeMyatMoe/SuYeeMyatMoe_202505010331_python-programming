choice = "y" 

# Main loop to allow multiple students' marks to be entered
while choice.lower() == "y": 

    # Prompt the user to enter marks for three quizzes and convert to float
    quiz_1 = float(input("Enter Quiz 1 mark: ")) 
    quiz_2 = float(input("Enter Quiz 2 mark: "))
    quiz_3 = float(input("Enter Quiz 3 mark: "))

    # Calculate the average by summing the quizzes and dividing by 3
    average = (quiz_1 + quiz_2 + quiz_3) / 3 
    print(f"The average mark is: {average:.2f}")

    # Determine pass or fail status based on a passing grade of 50
    if average >= 50: 
        print("Result: Pass")
    else: 
        print("Result: Fail")

    # Ask the user if they want to run the program again for another student
    choice = input("Continue? Select Y/N: ") 

print("Program Ended")