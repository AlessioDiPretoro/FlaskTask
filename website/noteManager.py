from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

noteManager = Blueprint('noteManager', __name__)

@noteManager.route('/notePage', methods=['GET', 'POST'])
@noteManager.route('/notePage/<int:id>', methods=['GET', 'POST', 'PUT'])
def notePage(id=None):
    if request.method == 'GET':
        note = None
        if id is not None:
            note = Note.query.get(id)  
            print("note.data " + note.data)
        return render_template('notePage.html', note=note, user = current_user)
    if request.method == 'POST':
        note = request.form.get('note')
        if id is None: #create new note
            if len(note) < 1:
                flash('Note is too short', category='error')
            else:
                new_note = Note(data=note, user_id=current_user.id)
                db.session.add(new_note)
                db.session.commit()
                flash('Note added')
        else: #edit this note
            if len(note) < 1:
                flash('Note is too short', category='error')
            else:
                oldNote = Note.query.get(id)
                if oldNote:
                    if oldNote.user_id == current_user.id:
                        oldNote.data = note
                        db.session.commit()
                        flash('Note Edited')
        return render_template("notes.html", user=current_user)
        