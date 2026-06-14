from flask import Blueprint, jsonify, current_app

main = Blueprint("main", __name__)


@main.route("/")
def home():
    version = current_app.config["APP_VERSION"]
    return jsonify({
        "message": f"Hello from {version}!",
        "version": version,
    })


@main.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "version": current_app.config["APP_VERSION"],
    }), 200


@main.route("/info")
def info():
    return jsonify({
        "app":     "myapp",
        "version": current_app.config["APP_VERSION"],
        "env":     "testing" if current_app.config["TESTING"] else "production",
    })
