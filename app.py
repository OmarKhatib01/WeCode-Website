from flask import Flask, render_template, request, redirect, url_for
import dataset

app = Flask(__name__)
# TODO: connect your database here
db = dataset.connect("postgres://ddwbsshctrcopd:5873de1bae81aa8dd1c1680475d0f7a1674dd3ceb057f0c285c81179783333e7@ec2-174-129-224-33.compute-1.amazonaws.com:5432/d32641cd2da4vv")


@app.route('/')
@app.route('/home')
def homepage():
	return render_template('home.html')

# TODO: route to /list
@app.route('/list')
def listt():
	pass
	usersTable = db["users"]
	allusers = list (usersTable.all())
	return render_template ("list.html" , allusers=allusers )
	


# TODO: route to /feed

# TODO: route to /register

# TODO: route to /error
@app.route('/error', methods=["GET", "POST"])
def error():
	# form =request.form
	# firstname=["firstname"]
	# lastname=["lastname"]
	# username=["username"]
	# email=["email"]
	# hometown=["hometown"] 
	# usersTable = db["users"]
	# entry = {"firstname":firstname , "lastname":lastname , "username":username , "email":email , "hometown":hometown}
	# usersTable.insert(entry)
	# print {{list(usersTable.all())}}
	# return render_template ("error.html" , firstname=firstname , lastname=lastname , username=username , email=email , hometown=hometown )
	
            

if __name__ == "__main__":
    app.run(port=3000)











