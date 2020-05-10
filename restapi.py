import requests
import json

email="namelastname@gmail.com"
phone="969696969"

def start():
    global jdata
    r = requests.get("http://127.0.0.1:8080/api/tutorial/1.0/employees")
    if(r.ok):
        jdata= json.loads(r.content)
    else: 
        return

    createEmployee()
    return

def createEmployee():
    name=input("Insert employee's name: ")
    surname=input("Insert employee's surname: ")
    employee={
        "employeeId": len(jdata),
        "firstName": name,
        "lastName": surname,
        "email": email,
        "phone": phone
    }
    r=requests.put("http://127.0.0.1:8080/api/tutorial/1.0/employees",employee)
    print(r)
    if(r.ok):
        print("employee added")
    else:
        print("error creating employee")
    return


if __name__ == "__main__":
	start()