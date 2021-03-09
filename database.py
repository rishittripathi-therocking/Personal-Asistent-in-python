import pymongo
from time_module import get_date_today

def create_connection():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    return myclient

def get_questions_and_answers():
    con = create_connection()
    db = con.memory
    question = db.questions.find({})
    return question

def get_answer_from_memory(question):
    rows = get_questions_and_answers()
    answer = ""
    for questioninRow in rows:
        for key in questioninRow:
            temp_key = key.lower()
            temp_question = question.lower() 
            if temp_key == temp_question:
                answer = questioninRow[key] 
    return answer

def insert_question_and_answer(question,answer):
    myclient = create_connection()
    mydb = myclient.memory
    mycol = mydb.questions
    mydict = {question:answer}
    mycol.insert_one(mydict)

def insert_memory_of_assistent(key,value):
    myclient = create_connection()
    mydb = myclient.memory
    mycol = mydb.memoryofassistent
    mydict = {key:value}
    mycol.insert_one(mydict)

def get_name():
    con = create_connection()
    db = con.memory
    memoryofassistent = list(db.memoryofassistent.find({}))
    return [x['assistant_name'] for x in memoryofassistent if "assistant_name" in x][0]

def update_name(new_name):
    myclient = create_connection()
    mydb = myclient.memory
    mycol = mydb.memoryofassistent
    mydict = {"$set":{"assistant_name":new_name}}
    mylist = list(mycol.find({}))
    p = [x['_id'] for x in mylist if "assistant_name" in x]
    mycol.update_one({"_id": p[0]},mydict)

def insert_date(key,date):
    myclient = create_connection()
    mydb = myclient.memory
    mycol = mydb.memoryofassistent
    mydict = {key:date}
    mycol.insert_one(mydict)

def update_date(date):
    myclient = create_connection()
    mydb = myclient.memory
    mycol = mydb.memoryofassistent
    mydict = {"$set":{"date":date}}
    mylist = list(mycol.find({}))
    p = [x['_id'] for x in mylist if "date" in x]
    mycol.update_one({"_id": p[0]},mydict)

def get_date():
    con = create_connection()
    db = con.memory
    memoryofassistent = list(db.memoryofassistent.find({}))
    return [x['date'] for x in memoryofassistent if "date" in x][0]


