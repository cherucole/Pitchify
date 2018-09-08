from flask import render_template,request,redirect,url_for
from ..models import Comment,User,Pitch,get_pitch,get_comments
from . import main
from .forms import CommentForm, PitchForm
from flask_login import login_required

import markdown2


def save_pitch(pitch):
    Pitch.save_pitch(pitch)

@main.route('/')
def index():
    '''
    my index page
    :return:
    '''
    message= "Test Dynamic message by Cherucole"
    return render_template('index.html', message=message)






@main.route('/category/<category>')
@login_required

def fetchcategory(category):

    '''
    View pitch page function that returns the pitch details page and its data
    '''
    category = get_pitch(category)
    print(category)
    return render_template('pitch.html', category=category)







@main.route('/pitch/comment/new/<int:id>', methods = ['GET','POST'])
@login_required

def new_comment(id):
    form = CommentForm()
    pitch = get_pitch(id)
    # comment=get_comments(id)
    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data

        # Updated comment instance
        new_comment = Comment(pitch_id=pitch.id, pitch_title=title,pitch_comment=comment)

        # save comment method
        new_comment.save_comment()
        return redirect(url_for('.pitch',id = pitch.id ))

    # title = f'{comment.comment_content} comment'

    title = 'comment'
    return render_template('new_comment.html', comment_form=form, pitch=pitch,comment=comment)


@main.route('/pitch/', methods=['GET', 'POST'])
@login_required

def pitch():

    '''
    View pitch page function that returns the pitch details page and its data
    '''
    # pitch = get_pitch(id)
    form = PitchForm()
    # title = f'{pitch.title}'
    # comments = Comment.get_comments(pitch.id)
    print('working')
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        category=form.category.data

        # Updated comment instance
        new_pitch = Pitch( pitch_title=title,pitch_content=content,pitch_category=category)

        # save comment method
        new_pitch.save_pitch()
        return redirect(url_for('.pitch',id = new_pitch.id ))

    # title = f'{comment.comment_content} comment'

    title = 'pitch'
    return render_template('new_pitch.html', pitch_form=form)

    # return render_template('pitch.html',title = title,pitch = pitch,comments = comments)


# @main.route('/new_pitch/<int:id>')
# def single_pitch():
#     form = PitchForm()
#
#     pitch=Pitch.query.get(id)
#     # if pitch is None:
#     #     abort(404)
#     format_pitch = markdown2.markdown(pitch.pitch_content,extras=["code-friendly", "fenced-code-blocks"])
#     return render_template('new_pitch.html',pitch = pitch,format_pitch=format_pitch,pitch_form=form)


@main.route("/view/<id>", methods=["GET","POST"])
def view_pitch(id):
    pitch = Pitch.query.get(id)
    if request.args.get("vote"):
       pitch.likes = pitch.likes + 1
       pitch.save_pitch()
       return redirect("/view/{pitch_id}".format(pitch_id=id))
    # return render_template("view_pitch.html",{'pitch':pitch})
    return render_template('view_pitch.html',pitch = pitch,)
