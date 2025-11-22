from firebase_functions import https_fn
from firebase_admin import initialize_app
from app import app

# Initialize Firebase Admin
initialize_app()

@https_fn.on_request()
def app_function(req: https_fn.Request) -> https_fn.Response:
    """
    Firebase Cloud Function entry point for the Flask app
    """
    with app.request_context(req.environ):
        return app.full_dispatch_request()
