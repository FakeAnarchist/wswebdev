import requests
import json

email="namelastname@gmail.com"
phone="969696969"

def start():
    global jdata
    while True:
        r = requests.get("http://127.0.0.1:8080/api/tutorial/1.0/employees")
        if(r.ok):
            jdata= json.loads(r.content)
        else: 
            print("unable to get data")
            return

        action=input("select your action: ")
        if(action == "add"):
            createEmployee()
        elif (action == "exit"):
            return
        elif(action == "delete"):
            deleteEmployee()
        elif(action == "status"):
            statusEmployee()
        elif(action == "list"):
            employeeList()
        

def createEmployee():
    name=input("Insert employee's name: ")
    surname=input("Insert employee's surname: ")
    id=input("Insert employee's id: ")
    employee={
        "employeeId": id,
        "firstName": name,
        "lastName": surname,
        "email": email,
        "phone": phone
    }
    r=requests.post("http://127.0.0.1:8080/api/tutorial/1.0/employees",json=employee)
    if(r.ok):
        print("employee added")
    else:
        print("error creating employee")

def deleteEmployee():
    id= input("what is the id of the employee ")
    bang="http://127.0.0.1:8080/api/tutorial/1.0/employees/"+str(id)
    r=requests.delete(bang)
    if(r.ok):
        print("employee deleted")
    else:
        print("error deleting employee")
    return

def statusEmployee():
    id= input("what is the id of the employee ")
    bang="http://127.0.0.1:8080/api/tutorial/1.0/employees/"+str(id)
    r=requests.get(bang)
    if(r.ok):
        print(json.loads(r.content))
    else:
        print("error viewing employee")
    return

def employeeList():
    r=requests.get("http://127.0.0.1:8080/api/tutorial/1.0/employees")
    if(r.ok):
        print(json.loads(r.content))
    else:
        print("error viewing employee")
    return

if __name__ == "__main__":
	start()