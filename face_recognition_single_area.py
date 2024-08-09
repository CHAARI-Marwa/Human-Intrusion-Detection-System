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

directory_path = r'images\post_augmentation'
images, encodages = load_images_from_folder(directory_path)
authorized_area_x_min = 0
authorized_area_x_max = 400
authorized_area_y_min = 0
authorized_area_y_max = 400
condition=False
while True:
    ret, frame = video_capture.read()
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        face_center_x = (left + right) // 2
        face_center_y = (top + bottom) // 2
        if authorized_area_x_min < face_center_x < authorized_area_x_max and \
           (authorized_area_y_min < face_center_y < authorized_area_y_max):
            area = "Authorized"
        else:
            area = "Unauthorized"
        if is_authorized(face_encoding, encodages):
            if area == "Authorized":
                condition = False
                color = (0, 255, 0)
            else:
                condition = True
                color = (0, 0, 255)
            label = f"{area}"
        else:
            condition = True
            color = (0, 0, 255)
            label = "Unauthorized"
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, label, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        if condition:
            frequency = 2000
            duration = 1000
            winsound.Beep(frequency, duration)

    cv2.rectangle(frame, (authorized_area_x_min, authorized_area_y_min), (authorized_area_x_max, authorized_area_y_max),
                  (0, 0, 0), 2)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()