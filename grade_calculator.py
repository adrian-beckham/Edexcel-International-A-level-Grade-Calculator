subject_totals = {
    "accounting": {"total": 600, "a2": 300},
    "arabic": {"total": 200, "a2": 100},
    "biology": {"total": 600, "a2": 300},
    "business": {"total": 400, "a2": 200},
    "chemistry": {"total": 600, "a2": 300},
    "economics": {"total": 400, "a2": 200},
    "english language": {"total": 400, "a2": 200},
    "english literature": {"total": 400, "a2": 200},
    "further mathematics": {"total": 600, "a2": 300},
    "french": {"total": 400, "a2": 200},
    "geography": {"total": 400, "a2": 200},
    "greek": {"total": 200, "a2": 100},
    "german": {"total": 400, "a2": 200},
    "history": {"total": 400, "a2": 200},
    "information technology": {"total": 400, "a2": 200},
    "law": {"total": 200, "a2": 100},
    "mathematics": {"total": 600, "a2": 300},
    "physics": {"total": 600, "a2": 300}, 
    "psychology": {"total": 400, "a2": 200},
    "pure mathematics": {"total": 600, "a2": 300},
    "spanish": {"total": 400, "a2": 200}
}

grade_boundaries = [
    ("A", 0.8),
    ("B", 0.7),
    ("C", 0.6),
    ("D", 0.5),
    ("E", 0.4),
    ("F", 0.3)
]



def cal_mark(subject):
    total = subject_totals[subject]["total"]
    a2_total = subject_totals[subject]["a2"]
    try:
        obtained_totalmark = int(input("Enter your obtained total marks: "))
        obtained_a2mark = int(input("Enter your obtained a2 marks: "))
    except ValueError:
        print("Invalid input! Please enter integers only")
        return

    total_ratio = obtained_totalmark / int(total)
    a2_ratio = obtained_a2mark / int(a2_total)

    for grade, threshold in grade_boundaries:
        if total_ratio >= threshold:
            if a2_ratio >= 0.9 and grade == "A":
                print("You get the highest grade: A*!")
            else:
                print(f"Your grade is {grade}")
            break


    

def main():
    results = {}
    print("Edexcel IAL Grade Calculator")
    print("\nAvailable subjects:", ", ".join(subject_totals.keys()))
    
    while True:
        subject = input("\nEnter subject name (or enter 'done' to finish): ").lower().strip()
        if subject == "done":
            break
        if subject not in subject_totals:
            print("Invalid subject! Please enter only available subjects")
            continue
        else:
            cal_mark(subject)









main()
