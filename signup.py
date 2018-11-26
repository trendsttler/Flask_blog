from flask import Flask, render_template
from forms import RegistrtionForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a8f780c237bf026a6755f5575dd1c4fc95d1847da44ad70ca4f9bdf17db5b796'

posts = [
    {
        'author': 'karan soni',
        'title': 'Blog post 1',
        'content': 'extension for Sublime Text 2 and 3! It allow you to Insert Lorem Ipsum in the editor via menu items or keyboard shortcut. Select how much text you want from the menu item in Edit Text Lorem Ipsum or on the right click menu in Lorem Ipsum . Just press the shortcut key (Alt+Shift+L) to add Lorem Ipsum text.',
        'date_posted': 'April 22, 2018' 
    },
    {
      'author': 'karan kumar soni',
      'title': 'Blog post 2',
      'content': 'extension for Sublime Text 2 and 3! It allow you to Insert Lorem Ipsum in the editor via menu items or keyboard shortcut. Select how much text you want from the menu item in Edi Text Lorem Ipsum or on the right click menu in Lorem Ipsum . Just press the shortcut key (Alt+Shift+L) to add Lorem Ipsum text.',
      'date_posted': 'April 22, 2018' 
    }
]



@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title='About') 

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title='Register', form=form) 

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title='login', form=form) 


if __name__=='__main__':
    app.run(debug=True)