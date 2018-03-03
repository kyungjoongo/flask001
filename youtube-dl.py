import json
from flask import Flask, request, jsonify, render_template
from flask.helpers import make_response
from flask_cors import CORS
import pafy

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def home_view():
    if request.method == 'POST':
        try:
            videourl = request.form.get("videoUrl", "https://www.youtube.com/watch?v=xuAH21DkJow")
            video = pafy.new(videourl)
            streams = video.streams
            streams_info = []
            for s in streams:
                streams_info.append((s.resolution, s.extension, s.get_filesize(), s.url))

            videoInfo = {
                "title": video.title,
                "author": video.author,
                "url": "http://www.youtube.com/watch?v=" + video.videoid,
                "duration": video.duration,
                "thumbnail": video.thumb,
                "streams": streams_info
            }
            return jsonify({"sucesso": True, "video": videoInfo})
        except ValueError, e:
            return jsonify({"sucesso": False, 'error': e.message})

    else:
        return render_template("index.html")


@app.route('/ddd', methods=['GET', 'POST'])
def home_view222():
    if request.method == 'GET':
        try:

            id = request.args.get('id')
            videourl = request.form.get("videoUrl", "https://www.youtube.com/watch?v=" + id)
            video = pafy.new(videourl)
            streams = video.streams
            streams_info = []
            for s in streams:
                streams_info.append((s.resolution, s.extension, s.get_filesize(), s.url))

            videoInfo = {
                "title": video.title,
                "author": video.author,
                "url": "http://www.youtube.com/watch?v=" + video.videoid,
                "duration": video.duration,
                "thumbnail": video.thumb,
                "streams": streams_info
            }
            return jsonify({"sucesso": True, "video": videoInfo})
        except ValueError, e:
            return jsonify({"sucesso": False, 'error': e.message})

    else:
        return render_template("index.html")


@app.route('/aaa', methods=['GET', 'POST'])
def aaa():
    if request.method == 'GET':
        try:

            id = request.args.get('id')
            videourl = request.form.get("videoUrl", "https://www.youtube.com/watch?v=" + id)
            video = pafy.new(videourl)
            audioStreams = video.allstreams
            streams_info = []

            for a in audioStreams:
                print(a.bitrate, a.extension, a.get_filesize())
                streams_info.append((a.bitrate, a.extension, a.get_filesize()))

            bestaudio = video.getbestaudio()

            # print (bestaudio)
            # bestaudio.download()

            videoInfo = {
                "title": video.title,
                "author": video.author,
                "url": "http://www.youtube.com/watch?v=" + video.videoid,
                "duration": video.duration,
                "thumbnail": video.thumb,
                "streams": streams_info
            }
            return jsonify({"sucesso": True, "video": videoInfo})
        except ValueError, e:
            return jsonify({"sucesso": False, 'error': e.message})

    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run()
