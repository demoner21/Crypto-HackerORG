from Crypto.Util.number import long_to_bytes

# The integer to convert back into a message
original_integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Convert the integer back into a byte string
byte_string = long_to_bytes(original_integer)

# Convert the byte string into a string of characters
original_message = byte_string.decode()

# Print the original message
print(original_message)
