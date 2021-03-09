from flask import render_template, Blueprint
from myapp.dashapp_nondb_2 import dash_app_2 as dash_app_2_obj



bp2 = Blueprint('dashapp_b2_name', __name__, template_folder='templates')

@bp2.route("/dash_app_2")
def dash_app2():
    return render_template('dash2.html', dash_url=dash_app_2_obj.URL_BASE,
                           min_height=dash_app_2_obj.MIN_HEIGHT)