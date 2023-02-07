import pgpy

PGP_MESSAGE = """"""

PGP_KEY = """"""

message = pgpy.PGPMessage.from_blob(PGP_MESSAGE)

# load the private key from file
private_key, _ = pgpy.PGPKey.from_blob(PGP_KEY)

# decrypt the message using the private key
decrypted_message = private_key.decrypt(message)

if __name__ == "__main__":
    print("Decrypted message: ", decrypted_message.message)
