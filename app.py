import streamlit as st
import pandas as pd

st.title("🎓 Student Record Management System")

# Initialize student records
if "students" not in st.session_state:
    st.session_state.students = []

# Menu
menu = st.sidebar.selectbox(
    "Select Operation",
    ["Add Student", "View Students", "Update Student", "Delete Student"]
)

# CREATE
if menu == "Add Student":
    st.header("Add Student")

    roll = st.number_input("Roll Number", min_value=1, step=1)
    name = st.text_input("Student Name")
    age = st.number_input("Age", min_value=1, max_value=100)
    course = st.text_input("Course")

    if st.button("Add Student"):
        if not name.strip() or not course.strip():
            st.warning("Please fill all fields.")

        elif any(s["Roll"] == roll for s in st.session_state.students):
            st.warning("Roll number already exists!")

        else:
            student = {
                "Roll": roll,
                "Name": name,
                "Age": age,
                "Course": course
            }

            st.session_state.students.append(student)
            st.success("Student Added Successfully!")

# READ
elif menu == "View Students":
    st.header("Student Records")

    if st.session_state.students:
        df = pd.DataFrame(st.session_state.students)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No student records found.")

# UPDATE
elif menu == "Update Student":
    st.header("Update Student")

    if st.session_state.students:
        rolls = [s["Roll"] for s in st.session_state.students]
        roll = st.selectbox("Select Roll Number", rolls)

        student = next(
            s for s in st.session_state.students if s["Roll"] == roll
        )

        name = st.text_input("New Name", student["Name"])
        age = st.number_input(
            "New Age", min_value=1, max_value=100, value=student["Age"]
        )
        course = st.text_input("New Course", student["Course"])

        if st.button("Update Student"):
            if not name.strip() or not course.strip():
                st.warning("Please fill all fields.")
            else:
                student["Name"] = name
                student["Age"] = age
                student["Course"] = course

                st.success("Student Updated Successfully!")
    else:
        st.info("No students available to update.")

# DELETE
elif menu == "Delete Student":
    st.header("Delete Student")

    if st.session_state.students:
        rolls = [s["Roll"] for s in st.session_state.students]
        roll = st.selectbox("Select Roll Number", rolls)

        if st.button("Delete Student"):
            st.session_state.students = [
                s for s in st.session_state.students
                if s["Roll"] != roll
            ]

            st.success("Student Deleted Successfully!")
    else:
        st.info("No students available to delete.")