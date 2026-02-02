def student_report(name, *marks, **info):
    total = sum(marks)
    average = total / len(marks) if marks else 0

    return {
        "name": name,
        "marks": list(marks),
        "total_marks": total,
        "average": average,
        "extra_info": info
    }


result = student_report(
    "Ayaz",
    80, 90, 75,
    city="Karachi",
    grade="A"
)

print(result)
