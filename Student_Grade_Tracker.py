#Calculates the average of a list of grades
def calculate_average(grades):
   avg = sum(grades)/len(grades)
   average = round(avg, 2)
   return average
#Determines grade based on average

def calculate_grade(average):
   if average >= 90:
      return 'A'
   elif average>=80:
      return 'B'
   elif average >=70:
      return 'C'
   elif average >= 60:
      return 'D'
   else :
      return 'F'
   
# Lists to store subject names and corresponding grades
subjects = []
grades = []


# Continuously prompt the user for subject names and grades until 'exit' is entered
while True:
   subject = (input("Enter your subject (for exit type 'exit'):"))
   if subject == 'exit':
      break
   while True:
        try:
            grade = float(input(f"Enter marks of {subject} (0-100):"))
            if 0 <= grade <= 100:
                break
            else:
                print("Invalid grade. Please enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")
   subjects.append(subject)
   grades.append(grade)

# Calculate the average grade
Average = calculate_average(grades)
# Determine the letter grade based on the average grade
grade = calculate_grade(Average)
# Print the calculated average grade and letter grade
print(f"Your Grade is {grade} and GPI is {Average}")

# Save data to a text file
file_name = "grades.txt"
with open(file_name, "a") as file:  # Open file in append mode so previous data will not overwrite
    for i in range(len(subjects)):
        file.write(f"{subjects[i]}: {grades[i]}\n")  # Write subject and grade to file