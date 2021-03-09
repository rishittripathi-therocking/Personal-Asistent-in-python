import pymongo

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
    return memoryofassistent[0]['assistant_name']

def update_name(new_name):
    myclient = create_connection()
    mydb = myclient.memory
    mycol = mydb.memoryofassistent
    mydict = {"$set":{"assistant_name":new_name}}
    mycol.update_one({"_id":list(mycol.find({}))[0]["_id"]},mydict)

