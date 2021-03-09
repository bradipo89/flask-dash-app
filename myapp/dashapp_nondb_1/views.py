from flask import render_template, Blueprint
from myapp.dashapp_nondb_1 import dash_app_1 as dash_app_1_obj



bp1 = Blueprint('dashapp_b1_name', __name__, template_folder='templates')

@bp1.route("/dash_app_1")
def dash_app1():
    return render_template('dash1.html', dash_url=dash_app_1_obj.URL_BASE,
                           min_height=dash_app_1_obj.MIN_HEIGHT)