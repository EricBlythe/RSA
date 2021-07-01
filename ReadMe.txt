Python3 Interpreter required.
This program should be run from command line.

-k option:
make a set of RSA keys
For example, 

	python Rabin-Miller.py -k key1.txt

makes a set of keys and save them in key1.txt.
Note: python can't be left out in the command. Otherwise the index of arguments will be incorrect.


-e option:
encrypt
For example, 
	
	python Rabin-Miller.py -e key1.txt 1.txt

uses key1.txt to encrypt 1.txt. The result will be saved in 1_encrypted.txt.
Note: the third number in key1.txt is the private key. For practical use, you should delete the third number in key1.txt and then publish it and let others use it to encrypt messages and send to you.

-d option:
decrypt
For example, 
	
	python Rabin-Miller.py -d key1.txt 1_encrypted.txt

uses key1.txt to decrypt 1_encrypted.txt. The result will be saved in 1_encrypted_decrypted.txt.

