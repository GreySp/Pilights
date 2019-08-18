from flask import Blueprint, render_template
from flask_login import login_required
from app.networking.forms import HunterForm

module = Blueprint('devices', __name__)

@module.route('/devices', methods=['GET', 'POST'])
def connect():
    form = HunterForm()
    return render_template('network/devices.html', form=form)