from flask import render_template
from flask import render_template,request,redirect,url_for
from ..models import Comment,User



from . import main



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
    pitch = get_pitch(id)
    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data

        # Updated review instance
        new_comment = Comment(pitch_id=pitch.id,pitch_title=title,pitch_comment=comment)

        # save review method
        new_comment.save_comment()
        return redirect(url_for('.pitch',id = pitch.id ))

    title = f'{movie.title} comment'
    return render_template('new_comment.html',title = title, comment_form=form, pitch=pitch)