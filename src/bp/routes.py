"""Define routes as Blueprint to be imported in app.py"""
from flask import Blueprint, render_template
from src.db.methods import read_coordinates, read_single_record, find_latest_record
from src.common.funcs import get_uri, get_websocket_uri

show_data_bp = Blueprint('show_data_bp', __name__)

@show_data_bp.route("/")
def index():
    """Render the client connected to websocket
    showing the mousemove coordinates."""
    ip, port = get_websocket_uri()
    return render_template("index.html", websocket_uri="{0}:{1}".format(ip, port))

@show_data_bp.route('/snaps')
def all_snaps():
    """basic endpoint without template
    just show if there are written values"""
    return read_coordinates()

@show_data_bp.route("/snap")
def single_record():
    """raw view of a single record"""
    latest = find_latest_record()
    print(latest)
    return read_single_record(latest-2)

@show_data_bp.route("/snap/<p>")
def single_rec(p):
    """read single record"""
    print(p)
    return read_single_record(p)
        
@show_data_bp.route("/shot")
def shot0():
    """render shot 0 template"""
    return render_template("snaps.html", picture_number=0, uri = get_uri())
@show_data_bp.route("/shot/<p>")
def shot(p):
    """render shot template"""
    return render_template("snaps.html", picture_number=p, uri = get_uri())
