from input_module import take_input
from process import processes
from output_module import output
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["memory"]
print(myclient.list_database_names())

while True:
    i = take_input()
    o = processes(i)
    output(o)

