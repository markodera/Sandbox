from flask import Flask, flash, render_template, request, url_for, redirect, session
from flask_migrate import Migrate
from flask_session import Session  
from extensions import db, bcrypt
import models

app = Flask(__name__, template_folder='templates')

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = 'QWETIVSVSIHisviwefihvsvkhsv@me24'
app.config["SESSION_TYPE"] = "filesystem"  # Configure session type

db.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app, db)
Session(app)  # Initialize Flask-Session

@app.route("/")
def index():
    return render_template('index.html')




@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first = request.form['first']
        last = request.form['last']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        try:
            if password == confirm_password:
                hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
                user = models.User(username=username, first=first, last=last, password=hashed_password)
                db.session.add(user)
                db.session.commit()
                flash("User created successfully!", "success")
                return redirect(url_for('add_task'))  # Redirect to the index page after successful signup
            else:
                flash("Passwords do not match", "error")
                return render_template('signup.html')
        except Exception as e:
            db.session.rollback()
            flash("Something went wrong", "error")
            return render_template('signup.html', error=str(e)), 500
    return render_template('signup.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if either username or password is empty
        if not username or not password:
            flash('Username or Password incorrect', 'error')
            return render_template('login.html')
        
        user = models.User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            # Set session variable upon successful login
            session['user_id'] = user.user_id
            print("Session data:", session)
            flash('Login successful!', 'success')

            return redirect(url_for('add_task'))
        else:
            flash('Invalid username or password', 'error')
            return render_template('login.html')
    return render_template('login.html')

@app.route("/task", methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        priority = request.form['priority']
        status = request.form['status']
        user_id = session.get('user_id')

        if not user_id:
            flash('User not logged in', 'error')
            return redirect(url_for('login'))

        try:
            task = models.Task(
                title=title,
                description=description,
                due_date=due_date,
                priority=priority,
                status=status,
                user_id=user_id  # Ensure user_id is assigned
            )
            db.session.add(task)
            db.session.commit()
            flash("Task added successfully!", "success")
            return redirect(url_for('view_task'))
        except Exception as e:
            db.session.rollback()
            flash("Something went wrong", "error")
            return render_template('task.html', error=str(e))
    return render_template('task.html')

@app.route("/viewtask", methods=['GET'])
def view_task():
    # Get the user's tasks from the database
    user_id = session.get('user_id')
    tasks = models.Task.query.filter_by(user_id=user_id).all()
    return render_template('viewtask.html', tasks=tasks)



if __name__ == '__main__':
    app.run(debug=True)