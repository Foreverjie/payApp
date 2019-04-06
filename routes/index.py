from flask import (
    render_template,
    request,
    redirect,
    session,
    url_for,
    Blueprint,
    make_response,
)

from models.User import User
from routes import current_user
from utils.qr_utils import get_qr


main = Blueprint('index', __name__)


"""
用户在这里可以
    访问首页
    注册
    登录

用户登录后, 会写入 session, 并且定向到 /profile
"""


# @main.route("/")
# def index():
#     img_name = 'jie.png'
#     get_qr('http://www.baidu.com', img_name, 'static/origin/test.jpg')
#     img = 'static/images/' + img_name
#     return render_template('index.html', img=img)


@main.route("/")
def index():
    return render_template('login.html')


@main.route("/register")
def register():
    return render_template('register.html')


@main.route("/register/add", methods=['POST'])
def add_user():
    form = request.form
    # 用类函数来判断
    u = User.register(form)
    if u is None:
        return redirect(url_for(".register"))
    return redirect(url_for('.index'))


@main.route("/login", methods=['POST'])
def login():
    form = request.form
    print(form)
    u = User.validate_login(form)
    print(u)
    if u is None:
        return "用户不存在"
    else:
        # session 中写入 user_id
        session['user_id'] = u.id
        # 设置 cookie 有效期为 永久
        session.permanent = True
        return str(u.bank)


@main.route("/profile")
def profile():
    u = current_user()
    if u is None:
        return redirect(url_for('.index'))
    else:
        return render_template('profile.html', user=u)


# todo 返回付款码图片地址
@main.route("/payC")
def payC():
    u = current_user()
    if u is None:
        return redirect(url_for('.index'))
    else:
        img_name = u.username + '.png'
        get_qr('http://www.baidu.com', img_name, 'static/origin/test.jpg')
        img = 'static/images/' + img_name
        #     return render_template('index.html', img=img)
        return render_template('payC.html', img=img)
