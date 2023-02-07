import base64
import cv2


# Encrypt the PGP key
def encrypt(key):
    return base64.b64encode(key).decode()


# Decrypt the PGP key
def decrypt(key):
    return str(base64.b64decode(key))


# Hide the encrypted key in the image
def hide_key_in_image(encrypted_data, img):
    # Convert the encrypted key to binary
    binary_data = format(int.from_bytes(encrypted_data.encode(), 'big'), 'b')

    # Modify the least significant bit of each channel (R, G, B)
    # to hide the binary key
    for i in range(0, len(img), 4):
        img[i] = (img[i] & ~1) | int(binary_data[i % len(binary_data)])
        img[i + 1] = (img[i + 1] & ~1) | int(binary_data[(i + 1) % len(binary_data)])
        img[i + 2] = (img[i + 2] & ~1) | int(binary_data[(i + 2) % len(binary_data)])

    return img


image = cv2.imread("img_nature.jpg")

# Example usage
pgp_key = b""
with open("./0x1959B529-sec.asc", "rb") as f:
    pgp_key = bytes(f.read())
encrypted_key = encrypt(pgp_key)

# Assume that the image data is stored in a list 'image'
hidden_image = hide_key_in_image(encrypted_key, image)
# Récupérez les données de l'image
data = image.reshape(-1, 3)

# Récupérez la clé binaire dissimulée dans l'image
binary_key = ""
print(len(data))
for pixel in data:
    binary_key += str(pixel[0] & 1) + str(pixel[1] & 1) + str(pixel[2] & 1)

# Convertir la clé binaire en chiffrée
encrypted_key = binary_key

# Déchiffrez la clé PGP
pgp_key = decrypt(encrypted_key)

pgp_key = bytes.fromhex(pgp_key).decode('utf-8')

# Affichez la clé déchiffrée
print("Clé PGP déchiffrée:", pgp_key)
