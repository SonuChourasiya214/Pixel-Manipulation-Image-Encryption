# Image Encryption & Decryption using XOR
# Author: Educational Purpose

def xor_image():
    try:
        # Input image path
        path = input("Enter image path: ")

        # Input key
        key = int(input("Enter key (0-255): "))

        print("\n[+] Image Path :", path)
        print("[+] Key Used   :", key)

        # Open image in read-binary mode
        with open(path, 'rb') as file:
            image_data = file.read()

        # Convert image data to bytearray
        image_bytes = bytearray(image_data)

        # XOR operation
        for i in range(len(image_bytes)):
            image_bytes[i] = image_bytes[i] ^ key

        # Write encrypted/decrypted data back
        with open(path, 'wb') as file:
            file.write(image_bytes)

        print("\n✅ Operation completed successfully!")

    except Exception as e:
        print("\n❌ Error:", e)


if __name__ == "__main__":
    xor_image()
