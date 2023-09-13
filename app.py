from flask import Flask, render_template, request
import pytube
from pytube import YouTube



app =  Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/submit', methods=['POST'])
def submit():
    link = request.form.get('URL')
    download(link)
    return f"sucess"

def download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
        return 0
    print("Download is completed successfully")

if __name__ == '__main__':
    app.run(debug=True)