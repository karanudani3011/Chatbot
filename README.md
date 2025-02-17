# Chatbot 


Here is a README file that you can use for your GitHub repository:

---

# Face Recognition Chatbot System

A simple face recognition system integrated with an AI-powered chatbot. This system allows users to register their faces for authentication and interact with a chatbot. The chatbot is powered by the **Groq AI API**.

---

## Features

- **Face Registration**: Users can register their face using their webcam.
- **Face Verification**: Upon login, the system verifies the user's face for authentication.
- **AI-Powered Chatbot**: After successful authentication, users can interact with a chatbot powered by the Groq AI API.
- **Logout**: Users can log out and return to the login page.

---

## Requirements

- Python 3.7+
- Streamlit
- OpenCV
- Face Recognition
- Requests
- Groq API Key

---

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/your-repo-name/face-recognition-chatbot.git
cd face-recognition-chatbot
```

### 2. Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

**Note**: You can create a `requirements.txt` with the following dependencies:

```txt
streamlit
opencv-python
face-recognition
requests
streamlit-extras
```

### 3. Groq API Setup:

- Sign up at [Groq](https://groq.com) and get your **API Key**.
- Replace the `API_KEY` variable in `app.py` with your key.

---

## Usage

### 1. Start the application:

Run the following command to launch the Streamlit app:

```bash
streamlit run login.py
```

This will start the app in your browser.

### 2. Face Registration:

- Go to the **"Register Face"** button and capture your face using the webcam.
- The system will detect and save your face for future login attempts.

### 3. Login:

- After registering your face, click **"Login"**.
- The system will attempt to recognize your face. If successful, you will be redirected to the chatbot.

### 4. Chat with the AI:

- Once logged in, you can enter text in the input box and interact with the chatbot.
- The chatbot will generate responses using the Groq API.

### 5. Logout:

- Click the **"Logout"** button to log out of the system and return to the login page.

---

## Files Explanation

- **login.py**: Contains the login and face registration logic using OpenCV and face-recognition.
- **app.py**: Contains the chatbot UI and integration with the Groq AI API.
- **requirements.txt**: Contains the list of dependencies for the project.
- **known_faces/**: Directory where registered faces are saved.

---



## Troubleshooting

- **Face not detected**: Ensure that you are well-lit and the camera is clear.
- **API Error**: Double-check your API key and make sure your Groq account is active.
- **Camera not working**: Ensure your webcam is correctly connected and accessible by the system.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Thanks to [Groq AI](https://groq.com) for the API powering the chatbot.
- Thanks to [OpenCV](https://opencv.org) and [Face Recognition](https://github.com/ageitgey/face-recognition) for the face recognition functionality.

--- 


In This u can create a folder name is known_faces to store the data image of an login and registered user 

