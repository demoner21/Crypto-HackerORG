import base64
hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
bytes_data = bytes.fromhex(hex_string)
base64_data = base64.b64encode(bytes_data)
print(base64_data)
