from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired
from flask import Flask, request
from flask import render_template
app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False

class MyForm(Form):
    name = TextField('name', validators=[DataRequired()])


@app.route('/user/username')
def show_user_profile():
    # show the user profile for that user
    user = request.args.get('username')
    return 'User %s' % user

@app.route('/success', methods=('GET', 'POST'))
def success():
    return "WTF!"

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    #return render_template(r'C:\Users\ddye\Documents\PyBulls\teach-me-flask\templates\submit.html', form=form)
    #return render_template(r'C:\Users\ddye\Documents\PyBulls\teach-me-flask\templates\submit.html')
    #return render_template('submit.html')
    #return "Hello!"
    return render_template('submit.html', form=form)
    
    
app.run(port=5001, debug=True)
#app.run(port=5001)
