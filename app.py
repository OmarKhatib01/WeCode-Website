from flask import Flask, render_template, request, redirect, url_for, session
import time
import dataset

app = Flask(__name__)
# TODO: connect your database here
db = dataset.connect("postgres://ddwbsshctrcopd:5873de1bae81aa8dd1c1680475d0f7a1674dd3ceb057f0c285c81179783333e7@ec2-174-129-224-33.compute-1.amazonaws.com:5432/d32641cd2da4vv")
app.secret_key = 'iq873g'




@app.route('/')
def home():
	return render_template ("home.html")
@app.route('/home')
def homepage():
	return render_template('home.html')


@app.route('/contact')
def con():
	return render_template ("contact.html")




# TODO: route to /list
@app.route('/list')
def listt():
	usersTable = db["users"]
	allusers = list (usersTable.all())[::-1]
	return render_template ("list.html" , allusers=allusers )
	







# TODO: route to /feed
@app.route('/feed', methods= ["GET","POST"])
def newsFeed():
	posts=db["posts"]
	allposts = list(posts.all())[::-1]
	
	if "username" in session:
		if request.method == "GET":
			return render_template("feed.html", allposts=allposts)
		else:
			form=request.form
			username = session['username']
			post=form["post"]
			time_string = time.strftime('%l:%M on %b %d, %Y')
			entry = {"username":username, "post": post, "time_string" : time_string}
			posts.insert(entry)
			allposts = list(posts.all())[::-1]
			return render_template("feed.html", allposts=allposts)
	else:
		return "You are  not logged in, please login"











# TODO: route to /register
@app.route('/register', methods=["GET", "POST"])
def regist():
	if request.method == "GET":
		return render_template ("register.html")
	else:
		form = request.form
		usersTable = db["users"]
		firstname = form["firstname"]
		lastname = form["lastname"]
		username= form["username"]
		email = form["email"]
		hometown = form["hometown"]
		personalwebsite = form["personalwebsite"]
		password = form["password"]
		entry = {"firstname":firstname , "lastname":lastname, "username":username , "email":email , "hometown":hometown , "personalwebsite":personalwebsite, "password":password}
		nameToCheck = username
		results = list(usersTable.find(username = nameToCheck))
		print len(results)
		if len(results) == 0:
			session["username"] = username
			taken = 0 
			usersTable.insert(entry)
			return redirect("/home")
			# TURN INTO LIST WHEN IT IS DONE
		else:
			taken = 1
			return render_template ("register.html", taken = taken)










@app.route('/login', methods = ["get" , "post"])
def login():
	if request.method == "GET":
		return render_template ("login.html")
	else:

		usersTable = db["users"]
		print list(usersTable.find(username="omar@1"))
		form = request.form
		username= form["username"]
		password= form["password"]
		nameToCheck = username
		results = len(list(usersTable.find(username = nameToCheck, password=password)))
		if results > 0:
			login=2
			session["username"] = username
			print('sucessful login')
			return redirect('/home')
		else:
			login=0
			return render_template("login.html" , login=login)








@app.route('/logout')
def logout():
	if 'username' in session:
	    session.pop('username', None)
	    return render_template("logout.html")



if __name__ == "__main__":
    app.run(port=3000)











