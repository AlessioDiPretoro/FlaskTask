from flask import Blueprint, render_template

modals = Blueprint('modals', __name__)

@modals.route('/new_note_modal')
def new_note_modal():
    return render_template('modals/new_note_modal.html')