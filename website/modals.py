from flask import Blueprint, render_template, request
from .models import Note
import asyncio

modals = Blueprint('modals', __name__)


@modals.route('/note_modal/<int:id>', methods=['GET', 'POST', 'PUT'])
@modals.route('/note_modal', methods=['GET', 'POST'])
def note_modal(id=None):
    if request.method == 'GET':
        note = None
        if id is not None:
            note = Note.query.get(id)  
            print("note.data " + note.data)
    return render_template('modals/note_modal.html', note=note)