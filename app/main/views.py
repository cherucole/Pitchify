from flask import render_template,request,redirect,url_for
from ..models import Comment,User
from . import main
from .forms import CommentForm



@main.route('/')
def index():
    '''
    my index page
    :return:
    '''
    message= "Test Dynamic message by Cherucole"
    return render_template('index.html', message=message)

@main.route('/pitch/comment/new/<int:id>', methods = ['GET','POST'])
def new_comment(id):
    form = CommentForm()
    # pitch = get_pitch(id)
    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data

        # Updated comment instance
        new_comment = Comment(pitch_id=pitch.id,pitch_title=title,pitch_comment=comment)

        # save comment method
        new_comment.save_comment()
        return redirect(url_for('.pitch',id = pitch.id ))

    # title = f'{comment.comment_content} comment'
    return render_template('new_comment.html', comment_form=form, pitch=pitch)


@main.route('/pitch/<int:id>')
def pitch(id):

    '''
    View pitch page function that returns the pitch details page and its data
    '''
    pitch = get_pitch(id)
    title = f'{pitch.title}'
    comments = Comment.get_comments(pitch.id)

    return render_template('pitch.html',title = title,pitch = pitch,comments = comments)