from flask import Flask, render_template, request, redirect, url_for
import dataset

app = Flask(__name__)
# TODO: connect your database here
db = dataset.connect("postgres://ddwbsshctrcopd:5873de1bae81aa8dd1c1680475d0f7a1674dd3ceb057f0c285c81179783333e7@ec2-174-129-224-33.compute-1.amazonaws.com:5432/d32641cd2da4vv")




@app.route('/home')
def homepage():
	return render_template('home.html')

# TODO: route to /list

# TODO: route to /feed

# TODO: route to /register
@app.route('/register', methods=["GET", "POST"])
def regist():
	if request.method == "GET":
		return render_template ("register.html")
	else:
		form = request.form
		firstname = form["firstname"]
		lastname = form["lastname"]
		username= form["username"]
		email = form["email"]
		hometown = form["hometown"]
		personalwebsite = form["personalwebsite"]
		usersTable = db["users"]
		entry = {"firstname":firstname , "lastname":lastname, "username":username , "email":email , "hometown":hometown , "personalwebsite":personalwebsite}
		usersTable.insert(entry)
		return render_template("register.html", firstname = firstname, email = email, hometown = hometown, lastname = lastname, personalwebsite = personalwebsite)
		usersTable = db["users"]
		nameToCheck = "username"
		results = list(users.find(username = nameToCheck))
		print len(results)

# TODO: route to /error

if __name__ == "__main__":
    app.run(port=3000)











