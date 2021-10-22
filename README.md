# way-too-basic text encryption service
a python script for very basic text encryption or decryption

the script uses basic alphabet swap encryption method relying on 8-bit binaries

# how to use
so basically u go releases and download the latest release in pyc format, then run the app to start encrypting and decrypting data!

# how to use the keys
a sample key is provided besides the readme file. download it and place the file (LEAVE THE NAME AS IT IS) in the same folder as the app itself.

the data in the key is made up of 0s and 1s, similar to binaries but encoded in UTF-8, a format that can be read by text editors.

create your own key by going to text-to-binary converter websites (I recommend [RapidTables][1]) and find the converter, enter these data SHOWN BELOW in custom order (which acts as an encryption layer as people does not know what order you went for):
![image](https://dm2302files.storage.live.com/y4mMv1xbo9oqhiPg_jMrLc4eT3EYMFOiuu0mjx4QIhSI7AxZiNOsAqN5vNMhQdoTGiqLaFf7eY40-eCKWm38ia0uK8XrF7aonFD84XiI1nlflpDET7oX47qH99vw_NMHImwxSRWv9kPnF3vQr3L0W3Tjcu_PhRL5bTINbOn3Jx3qywBPwQ73JKBQl9cNWBVpMXQ?width=766&height=900&cropmode=none)

NOTE: under option called Output Delimiter String, select "none"

after converting the data, copy the binary, open the key file (data.teskey) with notepad or other text editor and replace everything with copied data in ONE LINE
![notepad](https://dm2302files.storage.live.com/y4msCehB0g6o15wGlI7YSvGY4lwqpMgR21vXDL6Mp4CPFcmOHFle2UMI9JA3JpupvO9wOzogcYDUTYcXOCh_IMiNrfn9_qpO1tgjUXKapBS9E7pmI36sGXfV2MPyyONh6UTVnk045FsUBa0TaH2cm2k0sn92bHK8UjePXxjtx5hlo-zGSHJFVua7FHl5YFLJRdR?width=1707&height=887&cropmode=none)

viola! you got yourself an exclusive key that can be used to encrypt data that no other keys can decrypt.

you can share the key with the receipent who needs it to decrypt what you sent.

# my plan for future:
graphical user interface (quite unnecessry and will cut down compatibility on some platforms so probably not coming but yes)

[1]: https://www.rapidtables.com/convert/number/ascii-to-binary.html
