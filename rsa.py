#####################################################
#   Please do not use this to secure anything!      #
#   This is just an example of manually calculating #
#   RSA in Python, for personal use such as CTFs    #
#####################################################

# run "pip install pycryptodome" if you get the error "No module namned 'Crypto'"
from Crypto.Util.number import bytes_to_long, long_to_bytes

# Refer to https://youtu.be/UjIPMJd6Xks?t=120 by Khan Academy for explanations of these values
# Although their equation for d seems to be wrong
# Values used are from Wikipedia's example of RSA: https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Example

# Values to be provided
message = b"H" # Message (in plaintext) to be encrpyted. Ensure that it is a bytestring
p = 61 # Prime 1
q = 53 # Prime 2
e = 17 # Public key e

# Larger values of p and q are required for longer messages.
# For this simple example, we can only encrypt a single character.
# You may try the following values to encrypt longer messages
# message = b"meet me at noon by the beach"
# p = 194522226411154500868209046072773892801
# q = 288543888189520095825105581859098503663
# e = 65537

print(f"Message to be encrypted: {message}")
print(f"Prime 1: {p}")
print(f"Prime 2: {q}")
print(f"Public key e: {e}")

# Step 0 (might be optional depending on the given format of the message): Convert the message to a long (64-bit signed integer)
long = bytes_to_long(message)
print(f"Message as long: {long}")

# Step 1: Calculate n
n = p*q
print(f"Public key n: {n}")

# Step 2: Calculate Φ(n) or Phi(n)
phi = (q-1)*(p-1)
print(f"Phi(n): {phi}")

# Step 3: Determine the private key d = inverse(e) mod phi
d = pow(e, -1, phi) # Private key
print(f"d: {d}")

# Step 4: Encrypt the message with the public keys e and n with message^e mod n
encrypted = pow(long, e, n)
print(f"Encrypted message: {encrypted}")

# Step 5: Decrypt the encrypted message with encrypted^d mod n
decrypted = pow(encrypted, d, n)
print(f"Decrypted message (as long): {decrypted}")

# Step 6 (only needed if step 0 was done): Convert the long back to the original message
plaintext = long_to_bytes(decrypted)
print(f"Original message: {plaintext}")