from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017")
db = client["employee_db"]
collection = db["employees"]

@app.route("/employees", methods=["GET"])
def get_employees():
    employees = list(collection.find({}, {"_id": 0}))
    return jsonify(employees)

@app.route("/employees", methods=["POST"])
def add_employee():
    employee = request.get_json()
    collection.insert_one(employee)
    return jsonify({"message": "Employee added successfully"})

@app.route("/employees/<employee_id>", methods=["PUT"])
def update_employee(employee_id):
    new_employee_data = request.get_json()
    collection.update_one({"employee_id": employee_id}, {"$set": new_employee_data})
    return jsonify({"message": "Employee updated successfully"})

@app.route("/employees/<employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    collection.delete_one({"employee_id": employee_id})
    return jsonify({"message": "Employee deleted successfully"})

if __name__ == "__main__":
    app.run()
