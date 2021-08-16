from website import create_app

app = create_app()

#only works when run directly but not called
if __name__ == '__main__':
    app.run(debug = True)