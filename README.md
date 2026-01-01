🖼️ Pixel Manipulation for Image Encryption

This project demonstrates a simple image encryption and decryption technique using pixel manipulation (XOR operation) in Python.
It modifies the pixel values of an image using a secret key to make the image unreadable.

🔐 Using the same key, the image can be decrypted back to its original form.

✨ Features

Encrypts image using XOR pixel manipulation

Decrypts image using the same key

Supports PNG, JPG, JPEG, BMP

Beginner-friendly Python code

No external libraries required

🛠️ Technology Used

Python 3

File Handling

Bytearray & XOR Operation

📂 Project Structure
pixel-manipulation-image-encryption/
│
├── image_Encryp.py
├── test.png.jpg
└── README.md

▶️ How to Run

1️⃣ Clone the repository

git clone https://github.com/SonuChourasiya214/pixel-manipulation-image-encryption.git


2️⃣ Go to project directory

cd pixel-manipulation-image-encryption


3️⃣ Run the script

python3 image_encryp.py

🔑 How It Works

Image is read in binary format

Pixel values are converted into bytearray

XOR operation is applied using a secret key

Same process is used for encryption and decryption

🧪 Example
Enter image path: test.png.jpg
Enter key (0-255): 123


🔐 Image encrypted
Run again with same key → 🔓 Image decrypted

⚠️ Important Note

Encryption key must be between 0–255

This project is for educational purposes only

Not recommended for real-world secure encryption

📸 Sample Output

Original Image

Encrypted Image (distorted)

Decrypted Image (restored)

👨‍💻 Author

Sonu Choursiya
Cybersecurity & Ethical Hacking Enthusiast
