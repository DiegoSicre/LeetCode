from base64 import encode


character : str = "b"

print(character.encode(encoding="utf-8"))


letter_in_bytes : bytes = character.encode("utf-8", "ignore")