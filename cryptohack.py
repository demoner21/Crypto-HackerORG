flag_hex = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d" # This is the hex-encoded flag
flag_bytes = bytes.fromhex(flag_hex)
flag = flag_bytes.decode() # This will give you the decoded flag as a string
print(flag)
