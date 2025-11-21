import os
from app import app

# PUBLIC_INTERFACE
def get_port() -> int:
    """
    This function determines which port the Flask app should listen on.
    It defaults to 3001 and can be overridden using the PORT environment variable.
    """
    port_str = os.environ.get("PORT", "3001")
    try:
        return int(port_str)
    except ValueError:
        # Fallback to default if invalid value is provided
        return 3001


if __name__ == "__main__":
    # Bind to all interfaces for container/demo usage.
    # Debug is enabled when REACT_APP_NODE_ENV is not 'production'
    debug = os.environ.get("REACT_APP_NODE_ENV", "").lower() != "production"
    app.run(host="0.0.0.0", port=get_port(), debug=debug, threaded=True)
