from storage import load_students, save_students

students = load_students()

students = {}

while True:

    print("\n====== STUDENT DATABASE SYSTEM ======")
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Exit")

    choice = input("\nEnter your choice: ").strip()

    if not choice.isdigit():
        print("Please enter a valid number.")
        continue

    choice = int(choice)

    # ================= ADD STUDENT =================
    if choice == 1:

        student_id = input("Enter student ID: ").strip()

        if not student_id.isdigit():
            print("Student ID must be a number.")
            continue

        student_id = int(student_id)

        if student_id in students:
            print("Student ID already exists!")
            continue

        name = input("Enter student name: ").strip()

        if not name.replace(" ", "").isalpha():
            print("Name must contain only letters.")
            continue

        marks = input("Enter student marks: ").strip()

        if not marks.isdigit():
            print("Marks must be a number.")
            continue

        marks = int(marks)

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            continue

        students[student_id] = {
            "name": name,
            "marks": marks
        }

        save_students(students)

        print("Student added successfully!")

    # ================= VIEW STUDENTS =================
    elif choice == 2:

        if not students:
            print("No students found.")
        else:
            print("\nStudents:\n")

            for i, (sid, data) in enumerate(students.items(), start=1):
                print(f"{i}. ID: {sid} | Name: {data['name']} | Marks: {data['marks']}")

            print(f"\nTotal students: {len(students)}")

    # ================= SEARCH STUDENT =================
    elif choice == 3:

        sid = input("Enter student ID to search: ").strip()

        if not sid.isdigit():
            print("Invalid ID.")
            continue

        sid = int(sid)

        if sid in students:
            student = students[sid]
            print(f"\nID: {sid} | Name: {student['name']} | Marks: {student['marks']}")
        else:
            print("Student not found.")

    # ================= UPDATE STUDENT =================
    elif choice == 4:

        sid = input("Enter student ID to update: ").strip()

        if not sid.isdigit():
            print("Invalid ID.")
            continue

        sid = int(sid)

        if sid not in students:
            print("Student not found.")
            continue

        new_name = input("Enter new name: ").strip()

        if not new_name.replace(" ", "").isalpha():
            print("Name must contain only letters.")
            continue

        new_marks = input("Enter new marks: ").strip()

        if not new_marks.isdigit():
            print("Marks must be a number.")
            continue

        new_marks = int(new_marks)

        if new_marks < 0 or new_marks > 100:
            print("Marks must be between 0 and 100.")
            continue

        students[sid]["name"] = new_name
        students[sid]["marks"] = new_marks

        save_students(students)

        print("Student updated successfully!")

    # ================= DELETE STUDENT =================
    elif choice == 5:

        sid = input("Enter student ID to delete: ").strip()

        if not sid.isdigit():
            print("Invalid ID.")
            continue

        sid = int(sid)

        if sid in students:
            del students[sid]
            
            save_students(students)

            print("Student deleted successfully!")
        else:
            print("Student not found.")

    # ================= EXIT =================
    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please select between 1 and 6.")