from flask import render_template,request,redirect,url_for,abort
from ..models import Comment,User,Pitch
# We may also use the import * command to import all objects from a specific module e.g from ..models import *
# ,get_pitch,get_comments
from . import main
from .forms import CommentForm, PitchForm,UpdateProfile
from flask_login import login_required, current_user
from .. import db,photos
import markdown2


def save_pitch(pitch):
    Pitch.save_pitch(pitch)

@main.route('/')
def index():
    pitches = Pitch.query.order_by(Pitch.posted.desc()).all()
    '''
    my index page
    :return:
    '''
    return render_template('index.html', pitches=pitches )

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
    category = Pitch.get_pitch(category)
    if request.args.get("vote"):
        pitch.likes = pitch.likes + 1
        pitch.save_pitch()
    print(category)
    return render_template('pitch.html', category=category,pitch=pitch)

@main.route('/comments/<id>')
@login_required
def comment(id):
    comments =Comment.get_comments(id)
    print(comment)
    title = 'comments'
    return render_template('comments.html',comments = comments,title = title)

@main.route('/comment/<int:pitches_id>', methods = ['GET', 'POST'])
@login_required
def new_comment(pitches_id):
    pitches = Pitch.query.filter_by(id = pitches_id).first()
    form = CommentForm()

    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comment(comment_content=comment,user_id=current_user.id, pitches_id=pitches_id)

        new_comment.save_comment()

        return redirect(url_for('main.index'))
    title='New Pitch'
    return render_template('new_comment.html',title=title,comment_form = form,pitches_id=pitches_id)

@main.route('/pitch/', methods=['GET', 'POST'])
@login_required
def pitch():
    form = PitchForm()
    print('working')
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        category=form.category.data

        # Updated comment instance
        new_pitch = Pitch( pitch_title=title,pitch_content=content,pitch_category=category,user_id=current_user.id)

        # save comment method
        new_pitch.save_pitch()
        return redirect(url_for('.single_pitch',id = new_pitch.id ))

    title = 'pitch'
    return render_template('new_pitch.html', pitch_form=form)



@main.route('/pitch/<int:pitch_id>',methods=["GET","POST"])
def single_pitch(pitch_id):
    pitches = Pitch.query.filter_by(id=pitch_id).one()

    comments=Comment.get_comments(pitch_id)


    form =CommentForm()
    if form.validate_on_submit():
        comment=form.comment.data


        new_comment = Comment(comment_content=comment,user_id=current_user.id, pitch_id=pitch_id)

        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('main.pitch_comments', pitch_id=pitches.id))


        # new_comment.save_comment()

        # return redirect(url_for('.view_pitch', id=pitches.id, comments=comments))

    return render_template('added_pitch.html',pitch = pitches,form=form, comments=comments)


@main.route('/pitch_comments/<int:pitch_id>' ,methods=['GET', 'POST'])
def pitch_comments(pitch_id):

    pitch = Pitch.query.filter_by(id=pitch_id).one()
    # comments=Comment.get_comments(pitch_id)
    comments=Comment.query.all()


    return render_template('pitch_comments.html', pitch=pitch, comments=comments, pitch_id=pitch.id)



@main.route("/view/<id>", methods=["GET","POST"])
def view_pitch(id):
    pitch = Pitch.query.get(id)
    if request.args.get("vote"):
       pitch.likes = pitch.likes + 1
       pitch.save_pitch()
       return redirect("/view/{pitch_id}".format(pitch_id=id))
    return render_template('view_pitch.html',pitch = pitch, comment=comment)



