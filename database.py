import pymongo

def create_connection():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    return myclient
    '''mydb = myclient["memory"]
    mydict = {"Tell me Time":"Get The Time"}
    mycol = mydb["questions"]
    x = mycol.insert_one(mydict)'''

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