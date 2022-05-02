import random

def generate_key_stream(n):
    return bytes(random.randrange(0, 256) for i in range(n))
    #return random.randint(0,9)

def xor_bytes(key_stream, message):
    length = min(len(key_stream), len(message))
    return bytes([key_stream[i]^ message[i] for i in range(length)])

message = "0 "
message = message.encode()
print("message=",message)
print("len=",len(message))
key_stream = generate_key_stream(len(message))
cipher = xor_bytes(key_stream, message)
print(key_stream)
print(cipher)
print("message:",xor_bytes(key_stream, cipher))