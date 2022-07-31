from src import init_app

# https://towardsdatascience.com/how-to-insert-dummy-data-into-databases-using-flask-sqlalchemy-9c59efab4527

app = init_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0')