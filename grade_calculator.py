# Student Grade Calculator
# Week 2 Project
# Name: Tushti Sharma

def calculate_grade(average):
    if average >= 90:
        return "A", "Excellent!"
    elif average >= 80:
        return "B", "Very Good!"
    elif average >= 70:
        return "C", "Good!"
    elif average >= 60:
        return "D", "Needs Improvement!"
    else:
        return "F", "Failed!"


def get_valid_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter marks for {subject}: "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100")

        except ValueError:
            print("Please enter a valid number")


def main():
    print("=" * 40)
    print("STUDENT GRADE CALCULATOR")
    print("=" * 40)

    num_students = int(input("Enter number of students: "))

    student_names = []
    student_results = []

    for i in range(num_students):
        print(f"\n=== STUDENT {i + 1} ===")

        name = input("Enter student name: ")

        math = get_valid_marks("Math")
        science = get_valid_marks("Science")
        english = get_valid_marks("English")

        average = (math + science + english) / 3

        grade, comment = calculate_grade(average)

        student_names.append(name)

        student_results.append({
            "average": average,
            "grade": grade,
            "comment": comment
        })

    print("\n" + "=" * 40)
    print("RESULTS SUMMARY")
    print("=" * 40)

    print("Name\t\tAverage\tGrade\tComment")

    for i in range(len(student_names)):
        print(
            f"{student_names[i]}\t\t"
            f"{student_results[i]['average']:.1f}\t"
            f"{student_results[i]['grade']}\t"
            f"{student_results[i]['comment']}"
        )

    if num_students > 0:
        averages = [result["average"] for result in student_results]

        class_avg = sum(averages) / len(averages)
        max_avg = max(averages)
        min_avg = min(averages)

        max_index = averages.index(max_avg)
        min_index = averages.index(min_avg)

        print("\n" + "=" * 40)
        print("CLASS STATISTICS")
        print("=" * 40)

        print(f"Total Students: {num_students}")
        print(f"Class Average: {class_avg:.1f}")
        print(f"Highest Average: {max_avg:.1f} ({student_names[max_index]})")
        print(f"Lowest Average: {min_avg:.1f} ({student_names[min_index]})")

    print("\n" + "=" * 40)
    print("Thank you for using the Grade Calculator!")
    print("=" * 40)


if __name__ == "__main__":
    main()