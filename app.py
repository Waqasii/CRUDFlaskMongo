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


@app.route("/english",methods=['GET','POST'])
def English():
    # get the data from Eng table
    eng_collection=mongo.db.Eng
    totalEng=eng_collection.find()
    if(request.method=='POST'):
        name=request.form['name']
        surname=request.form['surname']
        if(eng_collection.find_one({'name':name,'surname':surname})):
            print('User Found')
            car_length=len(eng_collection.find_one({'name':name,'surname':surname})['cars'])
            car_brand=request.form['car_brand']
            car_model=request.form['car_model']
            car={'id':car_length+1,'brand':car_brand,'model':car_model}
            eng_collection.update({'name':name,'surname':surname}, {'$push': {'cars': car}})
            
        else:
            print('New User')
            car_brand=request.form['car_brand']
            car_model=request.form['car_model']
            cars=[{'id':1,'brand':car_brand,'model':car_model}]
            city=request.form['city']
            country=request.form['country']
            eng_collection.insert_one({'name':name,'surname':surname,'cars':cars,'city':city,'country':country})
        totalEng=eng_collection.find()
        return render_template('english.html',totalEng=totalEng)
    else:
        print(type(totalEng))
        return render_template('english.html',totalEng=totalEng)



@app.route("/italian",methods=['GET','POST'])
def Italian():
    return render_template('italian.html')
    

if __name__== "__main__":
    app.run(debug=True)
    app.run()