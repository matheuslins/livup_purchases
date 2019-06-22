from src import create_app


def client():
    app = create_app()
    return app.test_client()
