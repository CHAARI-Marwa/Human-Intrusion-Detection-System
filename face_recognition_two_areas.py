import cv2
import face_recognition
import os
import winsound
import tkinter as tk

def load_images_from_folder(folder):
    images = []
    encodings = []
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        if os.path.isfile(path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image = face_recognition.load_image_file(path)
            face_encodings = face_recognition.face_encodings(image)
            if len(face_encodings) > 0:
                encoding = face_encodings[0]
                images.append(image)
                encodings.append(encoding)
    return images, encodings
def is_authorized(face_encoding, known_encodings):
    matches = face_recognition.compare_faces(known_encodings, face_encoding)
    return any(matches)

video_capture = cv2.VideoCapture(0)

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, screen_width)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, screen_height)

video_capture.set(cv2.CAP_PROP_FPS, 30)

directory_path_area1 = r'images\post_augmentation\area1'
images, encodages = load_images_from_folder(directory_path_area1)
authorized_area1_x_min = 0
authorized_area1_x_max = 300
authorized_area1_y_min = 0
authorized_area1_y_max = 500

directory_path_area2 = r'images\post_augmentation\area2'
images1, encodages1 = load_images_from_folder(directory_path_area2)
authorized_area2_x_min = 450
authorized_area2_x_max = 650
authorized_area2_y_min = 200
authorized_area2_y_max = 600

def draw_rectangle(frame, face_location, color, thickness):
    top, right, bottom, left = face_location
    if is_authorized(face_encoding , encodages):
        color = (0, 255, 0)
    else:
        color = (0, 0, 255)
    cv2.rectangle(frame, (left, top), (right, bottom), color, thickness)

while True:
    ret, frame = video_capture.read()
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    aut1 = False
    aut2 = False
    for (top, right, bottom, left), face_encoding  in zip(face_locations, face_encodings):
        condition1 = False
        area1 = "Unauthorized"
        face_center_x = (left + right) // 2
        face_center_y = (top + bottom) // 2

        if (authorized_area1_x_min < face_center_x < authorized_area1_x_max and
                authorized_area1_y_min < face_center_y < authorized_area1_y_max):
            area1 = "Authorized"

        if is_authorized(face_encoding , encodages):
            if area1 == "Authorized":
                condition1 = False
                color1 = (0, 255, 0)
                aut1=True
            else:
                condition1 = True
                color1 = (0, 0, 255)
            etiquette = f"{area1}"
        else:
            condition1 = True
            color1 = (0, 0, 255)
            etiquette = "Unauthorized"

        '''if not aut2:
            cv2.rectangle(frame, (gauche, haut), (droite, bas), color, 2)
            cv2.putText(frame, etiquette, (gauche, haut - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)'''

        condition2 = False
        area2 = "Unauthorized"

        if (authorized_area2_x_min < face_center_x < authorized_area2_x_max and
                authorized_area2_y_min < face_center_y < authorized_area2_y_max):
            area2 = "Authorized"

        if is_authorized(face_encoding , encodages1):
            if area2 == "Authorized":
                condition2 = False
                color2 = (0, 255, 0)
                aut2 = True
            else:
                condition2 = True
                color2 = (0, 0, 255)
            etiquette1 = f"{area2}"
        else:
            condition2 = True
            color2 = (0, 0, 255)
            etiquette1 = "Unauthorized"
        if not aut1:
            cv2.rectangle(frame, (left, top), (right, bottom), color2, 2)
            cv2.putText(frame, etiquette1, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color2, 2)
        if not aut2:
            cv2.rectangle(frame, (left, top), (right, bottom), color1, 2)
            cv2.putText(frame, etiquette, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color1, 2)
        if aut1 and aut2:
            cv2.rectangle(frame, (left, top), (right, bottom), color2, 2)
            cv2.putText(frame, etiquette1, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color2, 2)

        if (condition2 and condition1) :
            frequency = 2000
            duration = 1000
            winsound.Beep(frequency, duration)

    cv2.rectangle(frame, (authorized_area1_x_min, authorized_area1_y_min),
                  (authorized_area1_x_max, authorized_area1_y_max), (0, 0, 0), 2)

    cv2.rectangle(frame, (authorized_area2_x_min, authorized_area2_y_min),
                  (authorized_area2_x_max, authorized_area2_y_max), (0, 70, 70), 2)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()