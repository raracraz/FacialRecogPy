import PySimpleGUI as sg
import cv2 

layout = [
    [sg.Image(key = '-IMAGE-')],
    [sg.Text('People in picture: 0', key = '-TEXT-', expand_x = True, justification = 'center')],
]

window = sg.Window('Face Detector', layout)

# get video
video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSE:
        break

window.close()
