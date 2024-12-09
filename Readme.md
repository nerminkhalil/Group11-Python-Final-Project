# **Group 11 Python Project**

Welcome to the **Group 11 Python Project**! This project is a Flask-based web application that analyzes and visualizes career change data. The project was developed as part of the **Introduction to Python Programming Course** in the **Data Analytics Program at St. Clair College**.

---

## **Project Description**
This web application provides users with insights into career changes based on various parameters. The platform allows:
- **Exploration of career-related data.**
- **Insights into group members and the dataset.**
- **Data table for browsing.**

---

## **Features**
1. **Home Page**: An introduction to the project and easy navigation.
2. **About Page**:
   - Information about Group 11 members.
   - Summary of the dataset, including the number of rows and columns, and detailed definitions of the variables.
3. **Data Page**:
   - Displays the dataset in a table format.


---

## **Group Members**
| Name           | Student ID |
|----------------|------------|
| Nermin Khalil  | w0896880   |
| Khiria Mohamed | w0877869   |
| Emily LeBlanc  | w0599697   |
| Sofia Alfaro   | w0872820   |
| Alaa AlHaj     | w0871728   |

---

## **Dataset**
The dataset focuses on career trends and includes variables like job satisfaction, work-life balance, and education level.

### **Dataset Summary**:
- **Rows**: *38,444*.
- **Columns**: *23*.

### **Key Variables**:
| Variable Name             | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| `Field of Study`          | Area of study pursued by the individual.                                   |
| `Current Occupation`      | The current job or role held by the individual.                            |
| `Age`                     | The individual's age.                                                     |
| `Gender`                  | The individual's gender.                                                  |
| `Years of Experience`     | Total years of work experience.                                           |
| `Education Level`         | The highest educational qualification achieved.                           |
| `Job Satisfaction`        | Level of satisfaction with the current job (1-10 scale).                  |
| `Likely to Change Occupation` | Indicates whether the individual is likely to change their job.         |

---

## **Technology Stack**
- **Programming Language**: Python
- **Framework**: Flask
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite
- **Tools**: Pandas, Gunicorn (for deployment)

---

## **Setup Instructions**
Follow these steps to run the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/nerminkhalil/Group11-Python-Project.git
   cd Group11-Python-Project
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask App**:
   ```bash
   python app.py
   ```

4. **Access the App**:
   Open a browser and go to `http://127.0.0.1:5000`.

