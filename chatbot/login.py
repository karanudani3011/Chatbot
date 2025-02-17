import cv2
import face_recognition
import streamlit as st
import os
from streamlit_extras.switch_page_button import switch_page 

st.set_page_config(page_icon="🤖", layout="centered")

if not os.path.exists("known_faces"):
    os.makedirs("known_faces")

def register_face():
    cam = cv2.VideoCapture(0)
    st.info("📷 Capturing face... Look at the camera.")

    face_detected = False
    frame = None

    for _ in range(30):  
        ret, frame = cam.read()
        if not ret:
            st.error("❌ Failed to capture image")
            cam.release()
            return

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
        face_locations = face_recognition.face_locations(rgb_frame, model="hog")  # or "cnn"
        
        if face_locations:
            face_detected = True
            break  

    cam.release()

    if not face_detected:
        st.error("⚠️ No face detected. Please try again.")
        return

    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    if not face_encodings:
        st.error("⚠️ Face detection failed. Try again in better lighting.")
        return

    # Save the captured image
    known_face_path = os.path.join("known_faces", "known_face.jpg")
    cv2.imwrite(known_face_path, frame)
    st.success("✅ Face registered successfully!")

def capture_and_verify():
    known_face_path = os.path.join("known_faces", "known_face.jpg")
    if not os.path.exists(known_face_path):
        st.error("⚠️ No registered face found! Please register a face first.")
        return False

    known_image = face_recognition.load_image_file(known_face_path)
    known_encodings = face_recognition.face_encodings(known_image)

    if not known_encodings:
        st.error("⚠️ No face found in the known image. Please check the image.")
        return False

    known_encoding = known_encodings[0]  

    cam = cv2.VideoCapture(0)
    st.info("📷 Capturing face... Look at the camera.")

    face_matched = False

    for _ in range(30): 
        ret, frame = cam.read()
        if not ret:
            st.error("❌ Failed to capture image")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame, model="hog")  # or "cnn"
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding in face_encodings:
            match = face_recognition.compare_faces([known_encoding], face_encoding, tolerance=0.5)
            if match[0]:
                face_matched = True
                break

        if face_matched:
            break

    cam.release()

    if face_matched:
        st.success("✅ Face recognized! Redirecting to chatbot...")
        return True
    else:
        st.error("❌ Face not recognized. Access denied.")
        return False

st.title("Face Recognition System")

if st.button("Register Face"):
    register_face()

if st.button("Login"):
    if capture_and_verify():
        switch_page("app")  