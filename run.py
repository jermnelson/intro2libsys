__author__ = "Jeremy Nelson"
__license__ = "MIT"

from libsys import app

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8080 # Default
    port = 8081 # Debug
    print("Before running app")
    app.run(host=host,
            port=port,
            debug=True)