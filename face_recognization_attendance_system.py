import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

# Load  known faces
sarita_image = face_recognition.load_image_file("faces/sarita.jpg")
sarita_encoding = face_recognition.face_encodings(sarita_image)[0]

souvik_image = face_recognition.load_image_file("faces/souvik.jpg")
souvik_encoding = face_recognition.face_encodings(souvik_image)[0]

known_face_encodings = [sarita_encoding,souvik_encoding]
known_face_names = ["Sarita", "Souvik"]

#List of expected students
students =known_face_names.copy()

face_locations =[]
face_encodings = []

# get the current date and time
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(f"{current_date}.csv", "+w", newline="")
lnwriter = csv.writer(f)

#Video Capture Setup
while True:
    _, frame = video_capture.read()
    #Frame Preprocessing
    small_frame = cv2.resize(frame, (0,0), fx= 0.25 ,fy = 0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    #Recognition faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)

    # Face Matching and Attendance Recording
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings,face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings,face_encoding)
        best_match_index =np.argmin(face_distance)

        #Text Overlay on Frame
        if(matches[best_match_index]):
            name = known_face_names[best_match_index]

        #Add the text if a person is present
        if name in known_face_names:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCorner0fText = (10,100)
            fontScale = 1.5
            fontColor = (255, 0, 0)
            thickness = 3
            lineType = 2
            cv2.putText(frame, name + " Present ", bottomLeftCorner0fText, font,fontScale, fontColor,thickness, lineType)

            #Attendance Recording to CSV
            if name in students:
                students.remove(name)
                current_time = now.strftime("%H-%M-%S")
                lnwriter.writerow([name,current_time])

    #Displaying the Frame
    cv2.imshow("Attendance", frame)

    #Breaking the Loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

#Releasing Video Capture
video_capture.release()
cv2.destroyAllWindows()
f.close()
