from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

user = Blueprint('user', __name__)

@user.route('/user', methods=['GET'])
def home():
    return render_template("user.html", user=current_user)