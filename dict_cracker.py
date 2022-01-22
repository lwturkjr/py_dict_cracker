# After working on Free Code Camp sha-1 password cracker challenge, I threw this together.
import hashlib

print("Valid hash types are: md5, sha1, sha256, sha512, sha3_256, sha3_512, blake2s, blake2b \n")
dict_file = input("Dictionary File: ")
hash_to_crack = input("Hash to crack: ").lower()
hash_type = input("Type of Hash: ").lower()
#salt_file = input("Salt File: ") # If you have a list of known salts, you can uncomment this

dict_file = open(dict_file, "r", encoding='latin-1') # rockyou.txt is encoded with latin-1, also works with top10k, you might need to change encoding for other dictionary files.
dict_file_lines = dict_file.readlines()

#salt_file = open(salt_file, "r")
#salt_lines = salt_file.readlines()

# There has to be a more elgant way to do this?
if hash_type == "md5":
    for i in range(0,len(dict_file_lines)):
        #for x in range(0,len(salt_lines)):
        hash_chk = hashlib.md5(dict_file_lines[i].replace("\n","").encode()).hexdigest()
        # salted = salt_lines[x].replace("\n","")+dict_file_lines[i].replace("\n","") # prepended
        # salted = dict_file_lines[i].replace("\n","")+salt_lines[x].replace("\n","") # appended
        # salted = salt_lines[x].replace("\n","")+dict_lines[i].replace("\n","")+salt_lines[x].replace("\n","") # both
        # salted_hash = hashlib.md5(salted.encode()).hexdigest()

        if hash_to_crack == hash_chk: # If you want to add the salted stuff, change hash_chk to salted_hash.
            print("Password found: ", dict_file_lines[i].replace("\n",""))
            exit()
    else:
        print("Password not Found")

elif hash_type == "sha1":
    for i in range(0,len(dict_file_lines)):
        hash_chk = hashlib.sha1(dict_file_lines[i].replace("\n","").encode()).hexdigest()

        if hash_to_crack == hash_chk:
            print("Password found: ", dict_file_lines[i].replace("\n",""))
            exit()
    else:
        print("Password not Found")

elif hash_type == "sha256":
    for i in range(0,len(dict_file_lines)):
        hash_chk = hashlib.sha256(dict_file_lines[i].replace("\n","").encode()).hexdigest()

        if hash_to_crack == hash_chk:
            print("Password found: ", dict_file_lines[i].replace("\n",""))
            exit()
    else:
        print("Password not Found")

elif hash_type == "sha512":
    for i in range(0,len(dict_file_lines)):
        hash_chk = hashlib.sha512(dict_file_lines[i].replace("\n","").encode()).hexdigest()

        if hash_to_crack == hash_chk:
            print("Password found: ", dict_file_lines[i].replace("\n",""))
            exit()
    else:
        print("Password not Found")

elif hash_type == "sha3_256":
    for i in range(0,len(dict_file_lines)):
        hash_chk = hashlib.sha3_256(dict_file_lines[i].replace("\n","").encode()).hexdigest()

        if hash_to_crack == hash_chk:
            print("Password found: ", dict_file_lines[i].replace("\n",""))
            exit()
    else:
        print("Password not Found")

elif hash_type == "sha3_512":
    for i in range(0,len(dict_file_lines)):
        hash_chk = hashlib.sha3_512(dict_file_lines[i].replace("\n","").encode()).hexdigest()

        if hash_to_crack == hash_chk:
            print("Password found: ", dict_file_lines[i].replace("\n",""))
            exit()
    else:
        print("Password not Found")

elif hash_type == "blake2s":
    for i in range(0,len(dict_file_lines)):
        hash_chk = hashlib.blake2s(dict_file_lines[i].replace("\n","").encode()).hexdigest()

        if hash_to_crack == hash_chk:
            print("Password found: ", dict_file_lines[i].replace("\n",""))
            exit()
    else:
        print("Password not Found")
elif hash_type == "blake2b":
    for i in range(0,len(dict_file_lines)):
        hash_chk = hashlib.blake2b(dict_file_lines[i].replace("\n","").encode()).hexdigest()

        if hash_to_crack == hash_chk:
            print("Password found: ", dict_file_lines[i].replace("\n",""))
            exit()
    else:
        print("Password not Found")
else:
    print("Input Valid hash type.")
