from flask_smorest import Blueprint
from flask.views import MethodView

# Health check blueprint (root prefix)
blp = Blueprint("Health Check", "health check", url_prefix="/", description="Health check route")


@blp.route("/")
class HealthCheck(MethodView):
    # PUBLIC_INTERFACE
    def get(self):
        """Return a simple health status payload."""
        return {"message": "Healthy"}
