from flask import Blueprint, render_template, request,flash, jsonify


from flask_login import login_required, current_user


from .models import Note
from . import db

import json

#define this file is a blueprint which have bunch of route (urls)

views = Blueprint('views', __name__)

@views.route('/', methods = ['GET','POST'])
@login_required
#when were this route is called the below functions is called
def home():
    print("home retrival")
    if request.method == 'POST':
        print('request type is post')
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data = note, user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('note added',category='success')



    return render_template("home.html",user = current_user)

@views.route('/delete-note', methods = ['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({}) #empty response
