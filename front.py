import requests
import streamlit as st

API_URL = "http://localhost:5000"

def get_employees():
    response = requests.get(f"{API_URL}/employees")
    if response.status_code == 200:
        employees = response.json()
        return employees
    else:
        st.error("Error retrieving employees")

def add_employee(employee):
    response = requests.post(f"{API_URL}/employees", json=employee)
    if response.status_code == 200:
        st.success("Employee added successfully")
    else:
        st.error("Error adding employee")

def update_employee(employee_id, new_employee_data):
    response = requests.put(f"{API_URL}/employees/{employee_id}", json=new_employee_data)
    if response.status_code == 200:
        st.success("Employee updated successfully")
    else:
        st.error("Error updating employee")

def delete_employee(employee_id):
    response = requests.delete(f"{API_URL}/employees/{employee_id}")
    if response.status_code == 200:
        st.success("Employee deleted successfully")
    else:
        st.error("Error deleting employee")

def main():
    st.title("Employee Management System")
    menu = ["View Employees", "Add Employee", "Update Employee", "Delete Employee"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "View Employees":
        employees = get_employees()
        if employees:
            st.table(employees)

    elif choice == "Add Employee":
        st.subheader("Add Employee")
        employee_id = st.text_input("Employee ID")
        name = st.text_input("Name")
        position = st.text_input("Position")
        salary = st.number_input("Salary", step=1000)
        if st.button("Add"):
            employee = {
                "employee_id": employee_id,
                "name": name,
                "position": position,
                "salary": salary
            }
            add_employee(employee)

    elif choice == "Update Employee":
        st.subheader("Update Employee")
        employee_id = st.text_input("Employee ID")
        new_name = st.text_input("New Name")
        new_position = st.text_input("New Position")
        new_salary = st.number_input("New Salary", step=1000)
        if st.button("Update"):
            new_employee_data = {
                "name": new_name,
                "position": new_position,
                "salary": new_salary
            }
            update_employee(employee_id, new_employee_data)

    elif choice == "Delete Employee":
        st.subheader("Delete Employee")
        employee_id = st.text_input("Employee ID")
        if st.button("Delete"):
            delete_employee(employee_id)

if __name__ == "__main__":
    main()
