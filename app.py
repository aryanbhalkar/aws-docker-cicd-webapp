import os

from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Render the main application page."""
    return render_template(
        "index.html",
        environment=os.getenv("APP_ENV", "development"),
        version=os.getenv("APP_VERSION", "1.0.0"),
        region=os.getenv("AWS_REGION_NAME", "eu-central-1"),
    )


@app.route("/health")
def health():
    """Health endpoint used by the Application Load Balancer."""
    return jsonify(
        {
            "status": "healthy",
            "service": "aws-docker-cicd-webapp",
            "region": os.getenv("AWS_REGION_NAME", "eu-central-1"),
        }
    ), 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)