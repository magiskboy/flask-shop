from flask import Blueprint, render_template, url_for, redirect, request
from flask_login import login_required, login_user, logout_user
from .forms import LoginForm


bp = Blueprint('admin', __name__, template_folder='templates', static_folder='static')


@bp.route('/')
@login_required
def index():
	ctx = { 'title': 'Dashboard' }
	return render_template('admin/index.html', **ctx)


@bp.route('/login')
def login():
	method = request.method
	login_form = LoginForm()

	if method == 'GET':
		ctx = { 'title': 'Login', 'login_form': login_form }
		return render_template('admin/login.html', **ctx)

	if method == 'POST':
		login_form = LoginForm()


@bp.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('admin.login'))
