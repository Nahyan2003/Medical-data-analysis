# 🏥 Medical Data History -- SQL Project

## 📌 Project Overview

This project is a comprehensive SQL-based database analysis system built
using a Medical Data History dataset. It demonstrates fundamental and
advanced SQL concepts by executing 34 structured queries on a relational
healthcare database.

The project integrates: - MySQL (Remote Database - Read Only) - Python -
Pandas - VS Code Jupyter Notebook

------------------------------------------------------------------------

## 🎯 Project Objectives

-   Execute 34 structured SQL queries
-   Practice real-world database querying
-   Apply SQL fundamentals and advanced concepts
-   Integrate MySQL with Python
-   Perform healthcare data analysis

------------------------------------------------------------------------

## 🗂 Database Information

Database Name: project_medical_data_history\
Domain: Healthcare / Hospital Records

### 📊 Tables Used

### 1️⃣ Patients

-   patient_id (Primary Key)
-   first_name
-   last_name
-   birth_date
-   gender
-   height
-   weight
-   allergies
-   city
-   province_id (Foreign Key)

### 2️⃣ Admissions

-   admission_id (Primary Key)
-   patient_id (Foreign Key)
-   admission_date
-   discharge_date
-   diagnosis
-   attending_doctor_id (Foreign Key)

### 3️⃣ Doctors

-   doctor_id (Primary Key)
-   first_name
-   last_name
-   specialty

### 4️⃣ Province_Names

-   province_id (Primary Key)
-   province_name

------------------------------------------------------------------------

## 🔗 Entity Relationships

-   One Patient → Many Admissions (1:N)
-   One Doctor → Many Admissions (1:N)
-   One Province → Many Patients (1:N)

------------------------------------------------------------------------

## 🛠 Technologies Used

-   Python 3.x
-   MySQL Server
-   mysql-connector-python
-   Pandas
-   VS Code
-   Jupyter Notebook

------------------------------------------------------------------------

## 💻 SQL Concepts Applied

### 🔹 Basic Queries

-   SELECT
-   WHERE
-   ORDER BY
-   DISTINCT
-   LIMIT

### 🔹 Filtering & Conditions

-   AND / OR
-   BETWEEN
-   LIKE
-   IN
-   IS NULL

### 🔹 Aggregations

-   COUNT()
-   SUM()
-   AVG()
-   MAX()
-   MIN()
-   GROUP BY
-   HAVING

### 🔹 Advanced Queries

-   INNER JOIN
-   Subqueries
-   CASE Statements
-   Date Functions
-   String Functions

------------------------------------------------------------------------

## 📈 Sample Query Categories

1.  Patient demographic filtering
2.  Admission statistics
3.  Province-wise aggregation
4.  Allergy trend analysis
5.  Doctor-patient relationship queries
6.  BMI-based obesity detection
7.  Multiple admission analysis
8.  Join-based diagnosis filtering

------------------------------------------------------------------------

## 🧮 BMI Calculation Logic

BMI Formula:

BMI = weight (kg) / (height (m))²

SQL Logic Used:

CASE\
WHEN weight / POWER(height/100, 2) \>= 30 THEN 1\
ELSE 0\
END AS isObese

------------------------------------------------------------------------

## ⚠ Challenges Faced

-   Read-only database (UPDATE permission denied)
-   MySQL connection timeouts
-   Schema mismatch errors
-   Handling NULL values properly

------------------------------------------------------------------------

## ✅ Solutions Implemented

-   Used IFNULL() instead of UPDATE
-   Reconnected database session when expired
-   Used CASE instead of modifying database
-   Verified schema using DESCRIBE command

------------------------------------------------------------------------

## 📊 Key Insights Derived

-   Gender distribution patterns
-   Most common allergies
-   City-wise patient concentration
-   Patients with multiple admissions
-   Province-wise height averages
-   Doctor specialization distribution

------------------------------------------------------------------------

## 🚀 Learning Outcomes

-   Strong understanding of SQL fundamentals
-   Hands-on experience with relational databases
-   Practical exposure to JOIN operations
-   Integration of SQL with Python workflow
-   Improved analytical thinking
-   Database debugging skills

------------------------------------------------------------------------

## 🔮 Future Improvements

-   Add data visualization dashboard
-   Convert project into web application
-   Add authentication & CRUD operations
-   Implement performance optimization
-   Integrate with AI analytics

------------------------------------------------------------------------

## 📌 Conclusion

This project successfully demonstrates real-world database querying
using SQL and Python. It strengthens core database skills required for
Data Analytics, AI Engineering, and Backend Development.

------------------------------------------------------------------------

## 👨‍💻 Author

Medical SQL Project\
Student Database Analysis Project
