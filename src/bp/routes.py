from flask import Blueprint, render_template
from src.db.methods import read_coordinates, read_single_record

show_data_bp = Blueprint('show_data_bp', __name__)

@show_data_bp.route('/snaps')
def index():
    """basic endpoint without template
    just show if there are written values"""
    return read_coordinates()

@show_data_bp.route("/snap")
def single_record():
    return read_single_record(1)

@show_data_bp.route("/snap/<p>")
def single_rec(p):
    """read single record"""
    print(p)
    return read_single_record(p)
        
@show_data_bp.route("/shot")
@show_data_bp.route("/shot/<p>")
def shot(p):
    """render shot template"""
    return render_template("snaps.html", picture_number=p)
