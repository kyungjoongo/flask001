import json
from flask import Flask, request, jsonify, render_template
from flask.helpers import make_response

import pafy


id = 'Sv6dMFF_yts'
video = pafy.new("https://www.youtube.com/watch?v=" + id)
audioStreams = video.audiostreams
streams_info = []

for a in audioStreams:
    print(a.bitrate, a.extension, a.get_filesize())

audioStreams[3].download()

