from flask import Flask, render_template, Response, jsonify
<<<<<<< HEAD
import base64
import gunicorn
from camera import *
from dotenv import load_dotenv

load_dotenv()

=======
import gunicorn
from camera import *
>>>>>>> dbcd268a05f23f5b7287a735b6cde761a7ef8930

app = Flask(__name__)

headings = ("Name","Album","Artist")
df1 = music_rec()
df1 = df1.head(15)
@app.route('/')
def index():
    print(df1.to_json(orient='records'))
    return render_template('index.html', headings=headings, data=df1)

def gen(camera):
    while True:
        global df1
        frame, df1 = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/t')
def gen_table():
    return df1.to_json(orient='records')

<<<<<<< HEAD
@app.route('/capture')
def capture():
    global df1
    jpeg_bytes, df, emotion = capture_once()
    df1 = df
    b64 = base64.b64encode(jpeg_bytes).decode('utf-8')
    return jsonify({
        'image': f'data:image/jpeg;base64,{b64}',
        'data': df1.to_dict(orient='records'),
        'emotion': emotion
    })

=======
>>>>>>> dbcd268a05f23f5b7287a735b6cde761a7ef8930
if __name__ == '__main__':
    app.debug = True
    app.run()
