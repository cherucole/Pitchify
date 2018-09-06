from flask import render_template

from . import main



@main.route('/')
def index():
    '''
    my index page
    :return:
    '''
    message= "Test Dynamic message by Cherucole"
    return render_template('index.html', message=message)