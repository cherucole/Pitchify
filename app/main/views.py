from flask import render_template,request,redirect,url_for,abort
from ..models import Comment,User,Pitch,get_pitch,get_comments
from . import main
from .forms import CommentForm, PitchForm,UpdateProfile
from flask_login import login_required, current_user
from .. import db,photos

import markdown2


def save_pitch(pitch):
    Pitch.save_pitch(pitch)

@main.route('/')
def index():
    '''
    my index page
    :return:
    '''
    # message= "To view select any category"
    return render_template('index.html', )



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/category/<category>')
@login_required

def fetchcategory(category):

    '''
    View pitch page function that returns the pitch details page and its data
    '''
    category = get_pitch(category)
    # pitch = Pitch.query.get(id)
    if request.args.get("vote"):
        pitch.likes = pitch.likes + 1
        pitch.save_pitch()
    print(category)
    return render_template('pitch.html', category=category,pitch=pitch)







@main.route('/pitch/comment/new/<int:id>', methods = ['GET','POST'])
@login_required

def new_comment(id):
    form = CommentForm()
    pitch = get_pitch(id)
    # comment=get_comments(id)
    if form.validate_on_submit():
        title = form.title.data
        content=form.content.data
        comment = form.comment.data

        # Updated comment instance
        new_comment = Comment(pitch_id=pitch.id, pitch_title=title,pitch_comment=comment,pitch_content=content,user=current_user)

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
    # pitch=get_pitch(id)
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
        return redirect(url_for('.single_pitch',id = new_pitch.id ))

    # title = f'{comment.comment_content} comment'

    title = 'pitch'
    return render_template('new_pitch.html', pitch_form=form)

    # return render_template('pitch.html',title = title,pitch = pitch,comments = comments)


@main.route('/pitch/<int:id>')
def single_pitch(id):
    pitches = Pitch.query.get(id)

    # pitches=Pitch.get_pitch(pitch.id)
    # pitch=Pitch.query.get(id)
    # if pitch is None:
    #     abort(404)
    return render_template('added_pitch.html',pitch = pitches)
    # return render_template('added_pitch.html',pitch = pitch,format_pitch=format_pitch)

    # return redirect("/view/{pitch_id}".format(pitch_id=id))


@main.route("/view/<id>", methods=["GET","POST"])
def view_pitch(id):
    pitch = Pitch.query.get(id)
    if request.args.get("vote"):
       pitch.likes = pitch.likes + 1
       pitch.save_pitch()
       return redirect("/view/{pitch_id}".format(pitch_id=id))
    # return render_template("view_pitch.html",{'pitch':pitch})
    return render_template('view_pitch.html',pitch = pitch,)
