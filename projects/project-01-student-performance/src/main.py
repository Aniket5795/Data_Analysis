# ==========================================
# PROJECT 1: STUDENT PERFORMANCE ANALYSIS
# ==========================================

# Step 1: Import Pandas
import pandas as pd

# Step 2: Load the dataset
df = pd.read_csv("../data/students.csv")

# Step 3: Display the dataset
print("\nSTUDENT DATASET")
print(df)

# Step 4: Display basic information
print("\nDATASET INFORMATION")
print(df.info())

# Step 5: Calculate the average examination score
average_score = df["Exam_Score"].mean()

print("\nAVERAGE EXAM SCORE:")
print(round(average_score, 2))

# Step 6: Find the highest scoring student
top_student = df.loc[df["Exam_Score"].idxmax()]

print("\nTOP PERFORMING STUDENT:")
print(top_student)

# Step 7: Calculate average study hours
average_study_hours = df["Study_Hours"].mean()

print("\nAVERAGE DAILY STUDY HOURS:")
print(round(average_study_hours, 2))

# Step 8: Count students who passed
passed_students = df[df["Exam_Score"] >= 50]

print("\nNUMBER OF PASSED STUDENTS:")
print(len(passed_students))

# Step 9: Calculate pass percentage
pass_percentage = (len(passed_students) / len(df)) * 100

print("\nPASS PERCENTAGE:")
print(round(pass_percentage, 2), "%")

# Step 10: Calculate correlation
correlation = df["Study_Hours"].corr(df["Exam_Score"])

print("\nSTUDY HOURS VS EXAM SCORE CORRELATION:")
print(round(correlation, 3))

print("\nANALYSIS COMPLETED SUCCESSFULLY!")