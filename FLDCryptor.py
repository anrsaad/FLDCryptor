#! Folder Cryptor 
# program by : Saad Anouar
# be sure to download the program from: https://github.com/anrsaad/FLDCryptor
import os
from cryptography.fernet import Fernet
from time import sleep

def intro():
    os.system("MODE CON: COLS=65 LINES=30")
    os.system("color A & cls")
    print("""

               F O L D E R   C R Y P T O R

                    _-o#&&*''''?d:>b\_
                _o/"`''  '',, dMF9MMMMMHo_
             .o&#'        `"MbHMMMMMMMMMMMHo.
           .o"" '         vodM*$&&HMMMMMMMMMM?.
          ,'     ______  $M&ood,~'`(&##MMMMMMH\\
         /    from     \ ,MMMMMMM#b?#bobMMMMHMMML
        &       here   ?MMMMMMMMMMMMMMMMM7MMM$R*Hk
       ?$.    start   :MMMMMMMMMMMMMMMMMMM/HMMM|`*L
      |          a    |MMMMMMMMMMMMMMMMMMMMbMH'   T,
      $H#:      free  `*MMMMMMMMMMMMMMMMMMMMb#}'  `?
      ]MMH#    world     ""*""\\""*#MMMMMMMMMMMMM'  -
      MMMMMb_                   |MMMMMMMMMMMP'     :
      HMMMMMMMHo                 `MMMMMMMMMT       .
      ?MMMMMMMMP                  9MMMMMMMM}       -
      -?MMMMMMM                  |MMMMMMMMM?,d-    '
       :|MMMMMM-                 `MMMMMMMT .M|.   :
        .9MMM[                    &MMMMM*' `'    .
         :9MMk                    `MMM#"        -
           &M}    Developed by:    `          .-
            `&.      [Saad Anouar]           .
              `~,   .                     ./
                  . _                  .-
                    '`--._,dd###pp=""'

""")
    sleep(3.5)

def logo():

    print("""

      ______ _      _____   _____                  _             
     |  ____| |    |  __ \ / ____|                | |            
     | |__  | |    | |  | | |     _ __ _   _ _ __ | |_ ___  _ __ 
     |  __| | |    | |  | | |    | '__| | | | '_ \| __/ _ \| '__|
     | |    | |____| |__| | |____| |  | |_| | |_) | || (_) | |   
     |_|    |______|_____/ \_____|_|   \__, | .__/ \__\___/|_|   
                                        __/ | |                  
                                       |___/|_|                 

""")

pc = os.system("hostname")

list_of_files = []

while True:
    # logo + intro
    os.system("@echo off")
    intro()
    os.system("MODE CON: COLS=75 LINES=20")
    os.system("color 3 & cls")
    logo()
    user = input("\t[enc] Encryting folder  ||  [dec] DEcrypting folder\n >> ").lower()
    def path():
        fenter = input('\nEnter your folder : >>' )
        path = fenter[1:-1]

        for root, dirs, files in os.walk(path):
            for file in files:
                list_of_files.append(os.path.join(root,file))

    if user == "enc" :
        path()
        # key
        key = Fernet.generate_key()
        print("this is your cryptage key:", key)
        with open('enckey.txt', 'wb') as filekey:
            filekey.write(key)
        with open('enckey.txt', 'rb') as filekey:
            key = filekey.read()


        for name in list_of_files:

            fernet = Fernet(key)
            with open(name, 'rb') as file:
                original = file.read()
            encrypted = fernet.encrypt(original)
            with open(name, 'wb') as enc_file:
                enc_file.write(encrypted)
            
            print(name)
            print(" ...............[File Encrypted]................")
        sleep(3)
        os.system(r"move enckey.txt %userprofile%/desktop/enckey.txt")
        os.system(r'msg * the key has bee saved to "enckey.txt" on your Desktop. (Please keep the key save)')
    elif user == "dec":
        path()
        # decrypting time

        decryptkey = input("\n\nType the key :>>  ")
        for name in list_of_files:

            fernet = Fernet(decryptkey)
            with open(name, 'rb') as enc_file:
                encrypted = enc_file.read()
            decrypted = fernet.decrypt(encrypted)
            with open(name, 'wb') as dec_file:
                dec_file.write(decrypted)
            
            print(name)
            print(" ...............[File Decrypted]................")
        sleep(3)

        os.system(r'msg * file has been Decrypting succeffuly.')
    elif user == "bey" or user == "exit":
        os.system("cls")
        break

    else:
        os.system("cls")
        print("\n\t\t      this is not a valid choice ")
        print("\n\t \tTry again. Or [bey] to exit program")
        sleep(2)