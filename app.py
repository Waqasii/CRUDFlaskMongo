from flask import Flask, render_template,request,redirect
from flask_pymongo import PyMongo

# Creating app and configuration with MongoDB
app = Flask(__name__)
mongo=PyMongo()
app.config['MONGO_URI']='mongodb+srv://user1:user1@cluster0.trxzo.mongodb.net/mydb?retryWrites=true&w=majority'
mongo.init_app(app)

'''
    DB Name: mydb
        collection For English: Eng
        collection For Italian: IT
        collection For User Login: User
    
'''



@app.route("/")
def index():
    return render_template('login.html')


@app.route("/login",methods=['GET','POST'])
def Login():
    # get all collection from User Table
    user_collection=mongo.db.User
    if(request.method=='POST'):
        # get the username and password from user
        username=request.form['username']
        password=request.form['password']
        
        # if user already exist then proceed with it to next page else save it to the database so he can login
        # in 2nd attempt (it's just ideal case of login but not secure lol)
        if(user_collection.find_one({'username':username,'password':password})):
            return render_template('layout.html')
        else:
            user_collection.insert_one({'username':username,'password':password})
            return redirect('/')



if __name__== "__main__":
    app.run(debug=True)
    app.run()