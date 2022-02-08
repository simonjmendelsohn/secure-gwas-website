import datetime
import functools
import json
import secrets
import string

import flask
import pyrebase
from firebase_admin import auth as firebase_auth
from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from google.auth import jwt
from google.auth.transport import requests
from google.oauth2 import id_token

from src.utils.google_cloud.google_cloud_iam import GoogleCloudIAM

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.before_app_request
def load_logged_in_user():
    try:
        session_cookie = flask.request.cookies.get("session")
        user_dict = firebase_auth.verify_session_cookie(
            session_cookie, check_revoked=True
        )
        g.user = {"id": user_dict["email"]}
    except Exception as e:
        if "session cookie provided: None" not in str(e):
            print(f'Error logging in user: "{e}"')
        g.user = None


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view


@bp.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        password_check = request.form["password_check"]

        if password_check != password:
            flash("Passwords do not match. Please double-check and try again.")
        else:
            try:
                firebase_auth.create_user(email=email, password=password)
                gcloudIAM = GoogleCloudIAM()
                gcloudIAM.give_cloud_build_view_permissions(email)

                return update_session_cookie_and_return_to_index(email, password)
            except Exception as e:
                if ("EMAIL_EXISTS") in str(e):
                    flash(
                        "This email is already registered.  Please either Log In or use a different email."
                    )
                else:
                    print(f'Error creating user: "{e}"')
                    flash("Error creating user.")
    return render_template("auth/register.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        try:
            return update_session_cookie_and_return_to_index(email, password)
        except Exception as e:
            if ("INVALID_PASSWORD") in str(e):
                flash("Invalid password. Please try again.")
            elif ("USER_NOT_FOUND") in str(e):
                flash("No user found with that email. Please try again.")
            else:
                print(f'Error logging-in user: "{e}"')
                flash("Error logging in. Please try again.")

    return render_template("auth/login.html")


@bp.route("/callback", methods=("POST",))
def callback():
    try:
        id_token.verify_oauth2_token(
            request.form["credential"],
            requests.Request(),
            "419003787216-rcif34r976a9qm3818qgeqed7c582od6.apps.googleusercontent.com",
        )
    except Exception as e:
        print(f'Error with jwt token validation: "{e}"')
        flash("Invalid Google account.")
        return redirect(url_for("gwas.index"))

    token = jwt.decode(request.form["credential"], verify=False)
    rand_str = "".join(secrets.choice(string.ascii_lowercase) for _ in range(16))

    try:
        firebase_auth.get_user_by_email(token["email"])
        firebase_auth.update_user(
            uid=token["email"], email=token["email"], password=rand_str
        )
    except firebase_auth.UserNotFoundError:
        firebase_auth.create_user(
            uid=token["email"], email=token["email"], password=rand_str
        )
        gcloudIAM = GoogleCloudIAM()
        gcloudIAM.give_cloud_build_view_permissions(token["email"])

    return update_session_cookie_and_return_to_index(token["email"], rand_str)


@bp.route("/logout")
def logout():
    response = redirect(url_for("auth.login"))
    response.set_cookie("session", expires=0)
    return response


def update_session_cookie_and_return_to_index(email, password):
    pb = pyrebase.initialize_app(json.load(open("fbconfig.json")))

    expires_in = datetime.timedelta(days=1)

    user = pb.auth().sign_in_with_email_and_password(email, password)
    session_cookie = firebase_auth.create_session_cookie(
        user["idToken"], expires_in=expires_in
    )
    response = redirect(url_for("gwas.index"))
    response.set_cookie(
        "session",
        session_cookie,
        expires=datetime.datetime.now() + expires_in,
        httponly=True,
        secure=True,
    )

    return response
