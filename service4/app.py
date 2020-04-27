# imports app object from ./application/__init__.py
from application import app

# if the file is being run directly, and not imported, then start the application.
if __name__ == '__main__':
 app.run(debug=True, port=5003, host='0.0.0.0')
