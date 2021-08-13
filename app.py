from flask import Flask, render_template,request,redirect
from flask_pymongo import PyMongo

# Creating app and configuration with MongoDB
app = Flask(__name__)
mongo=PyMongo()
app.config['MONGO_URI']='mongodb+srv://user1:user1@cluster0.trxzo.mongodb.net/mydb?retryWrites=true&w=majority'
mongo.init_app(app)

'''
    DB Name: mydb
    collection1 name: Eng
    collection2 name: IT
'''


'''
class Eng(db.Model):
    _id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(200),nullable=False)
    surname=db.Column(db.String(200),nullable=False)
    cars=db.Column(db.String(500),nullable=False)
    city=db.Column(db.String(20),nullable=False)
    country=db.Column(db.String(20),nullable=False)
    
    def __repr__(self) -> str:
        return f"{self._id}  - {self.name}"
    
    
class IT(db.Model):
    _id=db.Column(db.Integer,primary_key=True)
    nome=db.Column(db.String(200),nullable=False)
    cognome=db.Column(db.String(200),nullable=False)
    strada=db.Column(db.String(500),nullable=False)
    citta=db.Column(db.String(20),nullable=False)
    pease=db.Column(db.String(20),nullable=False)
    
    def __repr__(self) -> str:
        return f"{self._id}  - {self.nomes}"
    
''' 

@app.route("/",methods=['GET','POST'])
def index():
    return render_template('login.html')



if __name__== "__main__":
    app.run(debug=True)
    app.run()