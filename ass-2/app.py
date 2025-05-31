from flask import Flask,request,render_template
from dotenv import load_dotenv
import os,pymongo
import pymongo.mongo_client

load_dotenv()
MONGO_URI=os.getenv('MONGO_URI')
client= pymongo.MongoClient(MONGO_URI)
db= client.data
collection=db['assignment2']

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
    form_data=dict(request.form)
    collection.insert_one(form_data)
    return 'success'

if __name__=='__main__':
    app.run(debug=True)
    