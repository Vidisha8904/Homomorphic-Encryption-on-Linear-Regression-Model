# Homomorphic-Encryption-on-Linear-Regression-Model
Homomorphic Encryption on a Machine Learning Model using Partially Homomorphic Encryption(Pailler Cryptosystem) on a dummy dataset


This project demonstrates how machine learning inference can be performed on encrypted data using Paillier Partially Homomorphic Encryption.

A simple client–server setup is used where:

The client encrypts sensitive input data

The server performs computation directly on ciphertext

The client decrypts the final result

At no point does the server see the original data.


What This Project Does

Uses Paillier encryption to protect sensitive inputs

Runs a linear regression model on encrypted data

Returns an encrypted prediction

Only the client can decrypt the result using the private key

This project focuses on privacy-preserving machine learning, not model accuracy.


Tech Stack

Python

phe (Python Paillier library)

Linear Regression (pre-trained coefficients)

JSON for client–server data exchange

Project Structure
├── client.py        # Key generation, encryption, decryption
├── server.py        # Encrypted computation (linear regression)
├── linmodel.py      # Stores trained model coefficients
├── data.json        # Encrypted input data (client → server)
├── answer.json      # Encrypted prediction (server → client)
├── README.md


How It Works (High Level)

Client generates Paillier public & private keys

Client encrypts input features using the public key

Encrypted data is sent to the server

Server performs linear regression using homomorphic operations

Server returns encrypted prediction

Client decrypts the final result


Supported Operations

Paillier encryption supports:

Homomorphic addition

Homomorphic scalar multiplication

This makes it suitable for linear models, such as linear regression.



Use Case

The example use case predicts a mental health relapse risk score from encrypted mental health indicators, showing how sensitive data can be processed without being exposed.


Disclaimer
The dataset used is synthetic and does not contain real patient data.
