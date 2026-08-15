import pandas as pd
import numpy as np


students = pd.read_csv("students_dirty_dataset.csv")
sales = pd.read_csv("sales_dirty_dataset.csv")


print("STUDENT DATA")

print("\nFirst 5 rows:")
print(students.head())

print("\nShape:")
print(students.shape)

print("\nColumn names:")
print(students.columns)

print("\nData information:")
students.info()

print("\nStatistical summary:")
print(students.describe(include="all"))


print("\nSALES DATA")

print("\nFirst 5 rows:")
print(sales.head())

print("\nShape:")
print(sales.shape)

print("\nColumn names:")
print(sales.columns)

print("\nData information:")
sales.info()

print("\nStatistical summary:")
print(sales.describe(include="all"))


print("\nMISSING VALUES")

print("\nStudent missing values:")
print(students.isnull().sum())

print("\nStudent rows containing missing values:")
print(students[students.isnull().any(axis=1)])

print("\nSales missing values:")
print(sales.isnull().sum())

print("\nSales rows containing missing values:")
print(sales[sales.isnull().any(axis=1)])


print("\nDUPLICATE")

print("\nDuplicate Student IDs:")
print(
    students[
        students.duplicated(
            subset="StudentID",
            keep=False
        )
    ]
)

print("\nDuplicate Order IDs:")
print(
    sales[
        sales.duplicated(
            subset="OrderID",
            keep=False
        )
    ]
)


print("\nINVALID STUDENT DATA")


invalid_age = students[
    (students["Age"] < 16) |
    (students["Age"] > 100)
]

print("\nInvalid ages:")
print(invalid_age)


invalid_attendance = students[
    (students["Attendance"] < 0) |
    (students["Attendance"] > 100)
]

print("\nInvalid attendance:")
print(invalid_attendance)


invalid_hours = students[
    (students["StudyHours"] < 0) |
    (students["StudyHours"] > 24)
]

print("\nInvalid study hours:")
print(invalid_hours)


invalid_math = students[
    (students["Math"] < 0) |
    (students["Math"] > 100)
]

print("\nInvalid Math marks:")
print(invalid_math)

physics_numeric = pd.to_numeric(
    students["Physics"],
    errors="coerce"
)

print("\nPhysics after numeric conversion:")
print(physics_numeric)


invalid_programming = students[
    (students["Programming"] < 0) |
    (students["Programming"] > 100)
]

print("\nInvalid Programming marks:")
print(invalid_programming)


print("\nCATEGORICAL VALUES")

print("\nGender values:")
print(students["Gender"].unique())

print("\nDepartment values:")
print(students["Department"].unique())

print("\nMonth values:")
print(sales["Month"].unique())


print("\nCLEANING STUDENT DATA")

students_clean = students.copy()


students_clean = students_clean.drop_duplicates(
    subset="StudentID",
    keep="first"
)


students_clean["Name"] = (
    students_clean["Name"]
    .fillna("")
    .astype(str)
    .str.replace(
        r"[^A-Za-z .'-]",
        "",
        regex=True
    )
    .str.strip()
    .str.title()
)


missing_name = students_clean["Name"].eq("")

students_clean.loc[
    missing_name,
    "Name"
] = (
    "Unknown_"
    + students_clean.loc[
        missing_name,
        "StudentID"
    ].astype(str)
)


students_clean["Gender"] = (
    students_clean["Gender"]
    .astype("string")
    .str.strip()
    .str.upper()
)

gender_map = {
    "M": "M",
    "MALE": "M",
    "F": "F",
    "FEMALE": "F"
}

students_clean["Gender"] = (
    students_clean["Gender"]
    .map(gender_map)
    .fillna("Unknown")
)


students_clean["Department"] = (
    students_clean["Department"]
    .astype("string")
    .str.strip()
    .str.upper()
    .fillna("Unknown")
)

students_clean["Department"] = (
    students_clean["Department"]
    .replace("<NA>", "Unknown")
)


numeric_columns = [
    "Age",
    "StudyHours",
    "Attendance",
    "Math",
    "Physics",
    "Programming"
]

for column in numeric_columns:

    students_clean[column] = pd.to_numeric(
        students_clean[column],
        errors="coerce"
    )


valid_age = students_clean["Age"].between(
    16,
    100
)

age_median = students_clean.loc[
    valid_age,
    "Age"
].median()

students_clean.loc[
    ~valid_age |
    students_clean["Age"].isna(),
    "Age"
] = age_median

students_clean["Age"] = (
    students_clean["Age"]
    .round()
    .astype(int)
)


valid_hours = students_clean[
    "StudyHours"
].between(
    0,
    24
)

hours_median = students_clean.loc[
    valid_hours,
    "StudyHours"
].median()

students_clean.loc[
    ~valid_hours |
    students_clean["StudyHours"].isna(),
    "StudyHours"
] = hours_median


valid_attendance = students_clean[
    "Attendance"
].between(
    0,
    100
)

attendance_median = students_clean.loc[
    valid_attendance,
    "Attendance"
].median()

students_clean.loc[
    ~valid_attendance |
    students_clean["Attendance"].isna(),
    "Attendance"
] = attendance_median


subjects = [
    "Math",
    "Physics",
    "Programming"
]

for subject in subjects:

    valid_marks = students_clean[
        subject
    ].between(
        0,
        100
    )

    subject_median = students_clean.loc[
        valid_marks,
        subject
    ].median()

    students_clean.loc[
        ~valid_marks |
        students_clean[subject].isna(),
        subject
    ] = subject_median


students_clean["Average"] = (
    students_clean[
        ["Math", "Physics", "Programming"]
    ]
    .mean(axis=1)
    .round(2)
)


students_clean["Result"] = np.where(
    students_clean["Average"] >= 40,
    "Pass",
    "Fail"
)


def assign_grade(average):

    if average >= 80:
        return "A"

    elif average >= 70:
        return "B"

    elif average >= 60:
        return "C"

    elif average >= 50:
        return "D"

    else:
        return "F"


students_clean["Grade"] = (
    students_clean["Average"]
    .apply(assign_grade)
)


print("\nCLEANED STUDENT DATA")

print(students_clean)


print("\nCLEANING SALES DATA")

sales_clean = sales.copy()

sales_clean["Quantity"] = pd.to_numeric(
    sales_clean["Quantity"],
    errors="coerce"
)

sales_clean["UnitPrice"] = pd.to_numeric(
    sales_clean["UnitPrice"],
    errors="coerce"
)


print("\nDuplicate Order IDs before cleaning:")

print(
    sales_clean[
        sales_clean.duplicated(
            subset="OrderID",
            keep=False
        )
    ]
)


sales_clean = sales_clean.drop(
    sales_clean[
        (sales_clean["OrderID"] == 2013) &
        (sales_clean["Month"] == "Foo")
    ].index
)


sales_clean = sales_clean.drop_duplicates(
    subset="OrderID",
    keep="first"
)


valid_months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec"
]

sales_clean["Month"] = (
    sales_clean["Month"]
    .astype("string")
    .str.strip()
    .str.title()
)

sales_clean.loc[
    ~sales_clean["Month"].isin(valid_months),
    "Month"
] = "Unknown"


for column in ["Region", "Product"]:

    sales_clean[column] = (
        sales_clean[column]
        .astype("string")
        .str.strip()
        .str.title()
    )

    sales_clean[column] = (
        sales_clean[column]
        .replace(
            ["", "<NA>"],
            "Unknown"
        )
    )


valid_quantity = (
    sales_clean["Quantity"] > 0
)

quantity_median = sales_clean.loc[
    valid_quantity,
    "Quantity"
].median()

sales_clean.loc[
    ~valid_quantity |
    sales_clean["Quantity"].isna(),
    "Quantity"
] = quantity_median


valid_price = (
    sales_clean["UnitPrice"] > 0
)

price_median = sales_clean.loc[
    valid_price,
    "UnitPrice"
].median()

sales_clean.loc[
    ~valid_price |
    sales_clean["UnitPrice"].isna(),
    "UnitPrice"
] = price_median


sales_clean["TotalSales"] = (
    sales_clean["Quantity"] *
    sales_clean["UnitPrice"]
).round(2)


print("\nCLEANED SALES DATA")

print(sales_clean)


print("\nVALIDATION")

print("\nStudent missing values:")
print(students_clean.isnull().sum())

print("\nSales missing values:")
print(sales_clean.isnull().sum())


print("\nDuplicate Student IDs:")
print(
    students_clean[
        "StudentID"
    ].duplicated().sum()
)


print("\nDuplicate Order IDs:")
print(
    sales_clean[
        "OrderID"
    ].duplicated().sum()
)


print("\nAge values valid:")
print(
    students_clean[
        "Age"
    ].between(16, 100).all()
)


print("\nAttendance values valid:")
print(
    students_clean[
        "Attendance"
    ].between(0, 100).all()
)


print("\nMath values valid:")
print(
    students_clean[
        "Math"
    ].between(0, 100).all()
)


print("\nPhysics values valid:")
print(
    students_clean[
        "Physics"
    ].between(0, 100).all()
)


print("\nProgramming values valid:")
print(
    students_clean[
        "Programming"
    ].between(0, 100).all()
)


print("\nQuantity values valid:")
print(
    (sales_clean["Quantity"] > 0).all()
)


print("\nUnitPrice values valid:")
print(
    (sales_clean["UnitPrice"] > 0).all()
)


students_clean.to_csv(
    "students_cleaned_dataset.csv",
    index=False
)


sales_clean.to_csv(
    "sales_cleaned_dataset.csv",
    index=False
)

with pd.ExcelWriter(
    "Python_Lab_Cleaned_Datasets.xlsx",
    engine="openpyxl"
) as writer:

    students.to_excel(
        writer,
        sheet_name="Students_Raw",
        index=False
    )

    students_clean.to_excel(
        writer,
        sheet_name="Students_Clean",
        index=False
    )

    sales.to_excel(
        writer,
        sheet_name="Sales_Raw",
        index=False
    )

    sales_clean.to_excel(
        writer,
        sheet_name="Sales_Clean",
        index=False
    )


print("\nEXTRA ANALYSIS")

department_average = (
    students_clean
    .groupby("Department")["Average"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Marks by Department:")
print(department_average)



product_sales = (
    sales_clean
    .groupby("Product")["TotalSales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTotal Sales by Product:")
print(product_sales)



region_sales = (
    sales_clean
    .groupby("Region")["TotalSales"]
    .sum()
)

print("\nTotal Sales by Region:")
print(region_sales)



print("DATA CLEANING COMPLETED SUCCESSFULLY")


print("\nFiles created:")

print("students_cleaned_dataset.csv")
print("sales_cleaned_dataset.csv")
print("Python_Lab_Cleaned_Datasets.xlsx")