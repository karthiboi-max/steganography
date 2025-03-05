import cv2
import os
import string

def show_progress_bar(step, total_steps, bar_length=50):
    progress = step / total_steps
    arrow = '-' * int(progress * bar_length - 1) + '>'
    spaces = ' ' * (bar_length - len(arrow))
    print(f'Progress: [{arrow}{spaces}] {int(progress*100)}%', end='\r')

def encrypt_image(img_path, msg, password):
    img = cv2.imread(img_path)
    rows, cols, _ = img.shape

    if len(msg) > rows * cols:
        print("Message is too long to be encoded in the image!")
        return

    d = {chr(i): i for i in range(256)}
    n, m, z = 0, 0, 0

    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = (n + 1) % rows
        m = (m + (n == 0)) % cols
        z = (z + 1) % 3
        show_progress_bar(i + 1, len(msg))

    cv2.imwrite("Encryptedmsg.png", img)
    print("\nEncryption complete. Image saved as 'Encryptedmsg.png'.")
    os.system("Lambo.png")

def decrypt_image(img_path, msg_length, password):
    img = cv2.imread(img_path)
    rows, cols, _ = img.shape
    message = ""

    n, m, z = 0, 0, 0
    c = {i: chr(i) for i in range(256)}

    for i in range(msg_length):
        message += c[img[n, m, z]]
        n = (n + 1) % rows
        m = (m + (n == 0)) % cols
        z = (z + 1) % 3
        show_progress_bar(i + 1, msg_length)

    print("\nDecryption complete. Message: ", message)

def main():
    choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? ")
    img_path = "np.png"
    password = input("Enter password: ")

    if choice.lower() == 'e':
        msg = input("Enter secret message: ")
        encrypt_image(img_path, msg, password)
    elif choice.lower() == 'd':
        msg_length = int(input("Enter length of secret message: "))
        entered_password = input("Enter passcode for Decryption: ")
        if password == entered_password:
            decrypt_image(img_path, msg_length, password)
        else:
            print("Not a valid key!")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
