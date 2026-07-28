from fastapi import FastAPI,Body

app = FastAPI()

students = [
    {"name":"srihari","course":"DS","studentid":1},
    {"name":"srinu","course":"DA","studentid":2},
    {"name":"rajesh","course":"DS","studentid":3},
    {"name":"Srikanth","course":"DA","studentid":4}]

#GET
@app.get('/')
def home_page():
    return {
        "message":"welcome to fastapi"
        }
#GET
@app.get('/get_all_students') # get all students is done
def view_all_students():
    return {"Operation":"GET",
            "result":students}

# http://127.0.0.1:8000/get_all_students
# http://127.0.0.1:8000/get_single_student_by_id/3

#GET
@app.get('/get_single_student_by_id/{student_id}') # path paramer
def single_student(student_id:int):
    for i in students:
        if i['studentid'] == student_id:
            return {
                "Request":"GET",
                    "result":i
                    }
    return {"message":"student id you are looking for is not available in the students list"}

#POST
@app.post('/add_student')
def add_single_student(addnewstudent=Body()):
    students.append(addnewstudent)
    return {"operation":"POST","students details":students}

#PUT
@app.put('/update_student_Details_by_id/{studentid}')
def single_student(name:str,course:str,student_id:int):
    dict_ = {"name":name,"course":course,"studentid":student_id}
    for i in students:
        if i['studentid'] == student_id:
            P = i.update(dict_)
            return {
                "Request":"PUT",
                    "Previous detail":i
                    }
    return {"message":"student id you are looking for is not available in the students list"}

#DELETE
@app.delete('/delete_student_Details_by_id/{studentid}')
def single_student(student_id:int):
    for i in range(len(students)):
        if students[i]['studentid'] == student_id:
            d = students.pop(i)
            return {
                "Request":"DELETE",
                    "deleted detail":d
                    }
    return {"message":"student id you are looking for is not available in the students list"}
