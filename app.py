from flask import Flask, render_template, Response
import cv2
import numpy as np
from skimage.transform import resize
import pandas as pd
from keras.models import load_model

app = Flask(__name__)


modelo = load_model('modelPrueba111-018.model')
face_clsfr = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


data = pd.read_excel('database.xlsx')


name_column = 'Name'
university_column = 'University'
major_column = 'Major'

labels_dict = {0: 'Allan', 1:'Desconocido'}
color_dict = {0: (0, 255, 0), 1: (0, 0, 0)}

def process_frame(frame):
    img = frame.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_clsfr.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face_img = gray[y:y + w, x:x + w]
        resized = resize(face_img, (150, 150, 3))

        result = modelo.predict(np.expand_dims(resized, axis=0))
        label = np.argmax(result, axis=1)[0]

        cv2.putText(img, '{}'.format(label), (x, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (86, 155, 35), 2, cv2.LINE_AA)

        if label in labels_dict:
            name = labels_dict[label]
            if name in data[name_column].values:
                student_info = data[data[name_column] == name].iloc[0]

                # Dibujar el rectángulo del estudiante
                cv2.rectangle(img, (x, y), (x + w, y + h), color_dict[label], 2)

                # Obtener información del estudiante de la base de datos
                university = student_info[university_column]
                major = student_info[major_column]

                # Mostrar información del estudiante en el cuadro
                box_x = x - 20
                box_y = y - 220
                box_width = w * 2
                box_height = 120
                cv2.rectangle(img, (box_x, box_y), (box_x + box_width, box_y + box_height), (0, 0, 0), cv2.FILLED)
                cv2.rectangle(img, (box_x, box_y), (box_x + box_width, box_y + box_height), (255, 255, 255), 2)
                cv2.putText(img, 'Estudiante:', (box_x + 5, box_y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(img, 'Nombre: {}'.format(name), (box_x + 5, box_y + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(img, 'Universidad: {}'.format(university), (box_x + 5, box_y + 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(img, 'Carrera: {}'.format(major), (box_x + 5, box_y + 80), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2, cv2.LINE_AA)
            else:
                cv2.putText(img, 'Desconocido', (x, y - 25), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 0, 255), 2, cv2.LINE_AA)
                cv2.putText(img, 'No es estudiante', (x, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2, cv2.LINE_AA)
                cv2.rectangle(img, (x, y), (x + w, y + h), color_dict[1], 2)

    ret, jpeg = cv2.imencode('.jpg', img)
    return jpeg.tobytes()

@app.route('/')
def index():
    return render_template('index.html')

def gen_frames():
    source = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    while True:
        ret, frame = source.read()
        if not ret:
            break
        frame = process_frame(frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
