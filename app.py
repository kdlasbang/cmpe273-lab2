from flask import Flask, escape, request,jsonify
import json

app = Flask(__name__)
sid=1234456
cid=1122334
DB={"students":[],
    "classes":[]}

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}! Initialize student id is 1234456'


@app.route('/students',methods=['POST'])
def create_student():
    global sid
    req=request.json
    if len(DB["students"])==0:
        DB["students"].append({"id":sid,"name":req["name"]})
        return(jsonify(id=sid,name=req["name"])),201
    else:
        sid+=1
        DB["students"].append({"id":sid,"name":req["name"]})
        return(jsonify(id=sid,name=req["name"])),201


@app.route('/students/<int:get_id>',methods=['GET'])
def get_student(get_id):
    if(len(DB["students"])==0):
        return 'Currently no student, please POST first.'
    for i in range(len(DB["students"])):
        if DB["students"][i]['id']==get_id:
            return DB["students"][i]
    return 'No your ID, sorry!'


@app.route('/classes',methods=['POST'])
def create_class():
    global cid
    req=request.json
    if len(DB["classes"])==0:
        DB["classes"].append({"id":cid,"name":req["name"],"students":[]})
        return(jsonify(id=cid,name=req["name"],students=[]))
    else:
        cid+=1
        DB["classes"].append({"id":cid,"name":req["name"],"students":[]})
        return(jsonify(id=cid,name=req["name"],students=[]))

@app.route('/classes/<int:get_id>',methods=['GET'])
def get_classes(get_id):
    if(len(DB["classes"])==0):
        return 'Currently no class, please POST first.'
    for i in range(len(DB["classes"])):
        if DB["classes"][i]['id']==get_id:
            return DB["classes"][i]
    return 'No This Class ID, sorry!'


@app.route('/classes/<int:get_id>',methods=['PATCH'])
def patch_classes(get_id):
    req=request.json
    sindex=-1
    if(len(DB["students"])==0):
        return 'No this student'
    for i in range(len(DB["students"])):
        if DB["students"][i]['id']==req["student_id"]:
            sindex=i
    if sindex==-1:
        return 'No this student'
    if(len(DB["classes"])==0):
        return 'Currently no class, please POST first.'
    for i in range(len(DB["classes"])):
        if DB["classes"][i]['id']==get_id:
            if len(DB["classes"][i]['students'])==0:
                DB["classes"][i]['students'].append(DB["students"][sindex])
                return DB["classes"][i]
            #DB["classes"][i]['students']['student'].append({DB["students"][sindex]}
            else:

                for j in range(len(DB["classes"][i]['students'])):

                    if DB["classes"][i]['students'][j]['id']==req["student_id"]:
                        return DB["classes"][i]
                DB["classes"][i]['students'].append(DB["students"][sindex])
                #dataa={"student",DB["students"][sindex]}
                #print(dataa)
                return DB["classes"][i]
    return 'No This Class'

