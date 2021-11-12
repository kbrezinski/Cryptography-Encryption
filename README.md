# Cryptography-Encryption

A repository which contains all the projects for the course CNIT-141: Cryptography for Computer Networks taught by 
Sam Bowne at City College of San Francisco. Also contains completed CryptoHack challenges in the `./Cryptohack` folder.

## 1. AES
`aes.py`- basics of using AES in Python

## 2. Basics
`ceasar_cipher.py` - simple ceasar cipher implementation \
`rho.py` - rho method to find hash collisions \
`twotimepad.py` - implementation of one-time pad to for encryption \
`vigenaire_cipher.py` - simple vigenaire cipher implementation \
`xor.py` - simple xor implementation 

## 3. Math
`padding_oracle.py` - demonstrates the use of padding oracle attack against AES-CBC. Easy to forge message at the last 
block of CBC

## 4. RSA
`rsa.py` - simple RSA demonstration \
`rsa_forgery.py` - shows how to forge a RSA signature. How to create and validate the certificate. \
`rsa_keyformat.py` - shows how RSA keys are formatted in `.pem` files \
`rsa_short_key.py` - brute force RSA using a short key \
`rsa_small_calc` - RSA calculations for creation of the public and private keys

## 5. Other
`diffie_helman.py` - simple diffie-helman key exchange implementation

Includes a few scripts to simulate encryption and some cryptographic attacks. 

Examples include: padding oracle attack, two-time pad, crib drag, among others. 
 
