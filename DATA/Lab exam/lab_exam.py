import numpy as np
import pandas as pd

df = pd.read_excel("Lab_Exam_1_Raw_Data.xlsx", sheet_name="Raw_Data")

print(df.head())
print("Dimensions:", df.shape)

df = df.drop_duplicates(subset="Student_ID", keep="first")

df["Name"] = df["Name"].astype(str).str.strip()
df["Department"] = df["Department"].astype(str).str.strip().str.title()

df["Assignment"] = df["Assignment"].replace("Absent", 0)

df["Quiz"] = pd.to_numeric(df["Quiz"], errors="coerce")
df["Assignment"] = pd.to_numeric(df["Assignment"], errors="coerce")
df["Attendance"] = pd.to_numeric(df["Attendance"], errors="coerce")

df.loc[~df["Quiz"].between(0, 20), "Quiz"] = np.nan

df.loc[~df["Assignment"].between(0, 20), "Assignment"] = np.nan

df.loc[~df["Attendance"].between(0, 100), "Attendance"] = np.nan

quiz_median = df["Quiz"].median()
assignment_median = df["Assignment"].median()
attendance_mean = df["Attendance"].mean()

df["Quiz"] = df["Quiz"].fillna(quiz_median)
df["Assignment"] = df["Assignment"].fillna(assignment_median)
df["Attendance"] = df["Attendance"].fillna(attendance_mean)

df["Total Score"] = np.add(df["Quiz"], df["Assignment"])

df["Percentage"] = np.round(
    (df["Total Score"] / 40) * 100,
    2
)

df["Result"] = np.where(
    (df["Percentage"] >= 50) &
    (df["Attendance"] >= 75),
    "Pass",
    "Fail"
)

df = df.sort_values(
    by="Percentage",
    ascending=False
).reset_index(drop=True)

df.to_excel(
    "Cleaned Student Data.xlsx",
    sheet_name="Cleaned Data",
    index=False
)


print("\nFile exported successfully.")

# =========================
# QUESTION 2
# =========================

student_marks = [
    {"id": "S101", "name": "Amina", "marks": [78, 84, 69]},
    {"id": "S102", "name": "Bina", "marks": [55, 61, 58]},
    {"id": "S103", "name": "Chen", "marks": [91, 88, 95]},
    {"id": "S104", "name": "Dipa", "marks": [42, 49, 46]}
]


def prepare_results(students):

    results = {}

    for student in students:

        total = 0

        for mark in student["marks"]:
            total += mark

        average = total / len(student["marks"])

        if average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"

        results[student["id"]] = {
            "name": student["name"],
            "average": round(average, 2),
            "grade": grade
        }

    return results


# Call function
results = prepare_results(student_marks)

# Print results
print("Student Results")

for student_id, data in results.items():
    print(
        f"{student_id} - {data['name']} - "
        f"Average: {data['average']:.2f} - "
        f"Grade: {data['grade']}"
    )

# Grade frequency
grade_frequency = {}

for data in results.values():

    grade = data["grade"]

    if grade in grade_frequency:
        grade_frequency[grade] += 1
    else:
        grade_frequency[grade] = 1

print("\nGrade Frequency:")
print(grade_frequency)


inventory = {
    "P101": {
        "name": "Keyboard",
        "stock": 8,
        "reorder_level": 10,
        "unit_price": 1500
    },

    "P102": {
        "name": "Mouse",
        "stock": 15,
        "reorder_level": 12,
        "unit_price": 800
    },

    "P103": {
        "name": "Headset",
        "stock": 4,
        "reorder_level": 8,
        "unit_price": 2200
    },

    "P104": {
        "name": "Webcam",
        "stock": 6,
        "reorder_level": 6,
        "unit_price": 3000
    }
}


def create_reorder_list(items):

    reorder_list = []

    for code, item in items.items():

        if item["stock"] < item["reorder_level"]:

            order_quantity = (
                2 * item["reorder_level"]
                - item["stock"]
            )

            cost = (
                order_quantity
                * item["unit_price"]
            )

            reorder_list.append({
                "code": code,
                "name": item["name"],
                "order_quantity": order_quantity,
                "cost": cost
            })

    return reorder_list


# Create reorder list
reorder_records = create_reorder_list(inventory)

# Print reorder records
print("Reorder Records:")

for record in reorder_records:
    print(
        f"Code: {record['code']}, "
        f"Name: {record['name']}, "
        f"Order Quantity: {record['order_quantity']}, "
        f"Cost: {record['cost']}"
    )

# Calculate total reorder cost
total_cost = 0

for record in reorder_records:
    total_cost += record["cost"]

print("\nTotal Reorder Cost:", total_cost)
