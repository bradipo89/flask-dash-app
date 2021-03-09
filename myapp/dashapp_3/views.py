from flask import render_template, Blueprint
from myapp.dashapp_3 import dash_app_3 as dash_app_3_obj



bp3 = Blueprint('dashapp_b3_name', __name__, template_folder='templates')

@bp3.route("/dash_app_3")
def dash_app3():
    return render_template('dash3.html', dash_url=dash_app_3_obj.URL_BASE)