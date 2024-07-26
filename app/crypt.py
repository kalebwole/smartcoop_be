import base64

def encrypt_text(plain_text):
    """
    Encode the plain text using Base64 encoding.
    
    :param plain_text: The text to encode.
    :return: The encoded text as a string.
    """
    encoded_bytes = base64.b64encode(plain_text.encode('utf-8'))
    encoded_text = encoded_bytes.decode('utf-8')
    return encoded_text

def decrypt_text(encoded_text):
    """
    Decode the Base64 encoded text.
        
    :param encoded_text: The text to decode.
    :return: The decoded text as a string.
    """
    decoded_bytes = base64.b64decode(encoded_text.encode('utf-8'))
    decoded_text = decoded_bytes.decode('utf-8')
    return decoded_text