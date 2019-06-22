from src import create_app
from src.settings import HOST, PORT, DEBUG


app = create_app()

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
