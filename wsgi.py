from app.app import create_app
import config

app = create_app(config)

#* Runs when the file is called.
if __name__ == "__main__":
    #* I enabled debug as it will allow for the app to be reloaded when code changes.
    app.run(debug=True)
