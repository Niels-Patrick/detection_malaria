from app import create_app
import webbrowser
from threading import Timer
import atexit
from app.cleanup import cleanup_upload_folder

app = create_app()

# Opening the app in a web browser
#def open_browser():
    #webbrowser.open("http://127.0.0.1:8003/")

if __name__ == "__main__":
    #Timer(1, open_browser).start()
    app.run(debug=True, host='0.0.0.0', port=8003)
    atexit.register(cleanup_upload_folder)
