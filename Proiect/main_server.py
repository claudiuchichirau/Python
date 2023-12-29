from server.server import app

if __name__ == '__main__':
    """
    This condition checks if this script is the main module being run.
    If it is, it starts the Flask application with debugging enabled.
    """

    app.run(debug=True)
