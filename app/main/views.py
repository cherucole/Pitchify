from flask import render_template
from flask import render_template,request,redirect,url_for


from . import main



@main.route('/')
def index():
    '''
    my index page
    :return:
    '''
    message= "Test Dynamic message by Cherucole"
    return render_template('index.html', message=message)