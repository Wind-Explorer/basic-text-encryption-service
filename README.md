# basic text encryption service
a python script for very basic text encryption or decryption

the script uses basic alphabet swap encryption method relying on 8-bit binaries

# how to use
You will need `git` installed. Guide can be found [here][5].
Download (clone) this repository onto your device with `git clone https://github.com/Wind-Explorer/basic-text-encryption-service.git` in a terminal. Change your working directory into the downloaded repository with `dir ./basic-text-encryption-service` for Windows or `cd ./basic-text-encryption-service` for any other device and enter `python3 ./main.py` to run the script.

refer to below for system-specific terminal access instructions

# for Windows:
you do need a basic installation of python for the script to execute. I recommend [Python 3.9.7][2]. Install python by opening a command prompt from the start menu, search for "cmd", then select the "Command Prompt" app (on Windows 10 and below) or "Windows Terminal" (on Windows 11 or above). In the terminal, enter `python` or `python3` and Microsoft Store would show up, prmpting you to install Python if it is not. Afterwards, follow steps above.

# for Android:
not recommended to be used on Android because it is quite troublesome although it works, use a terminal emulator like [Termux][3] for terminal access. In the terminal, enter `apt install python3` to install Python, then follow steps above

# for iOS/iPadOS:
not recommended but similar to for Android. I recommend [LibTerm][4] for emulating terminal. Python should be pre-installed. Follow steps above.

# for Linux systems:
Open a terminal window, install Python with this [guide][6], then follow steps above.


# how to use the keys
a sample key is provided in the downloaded repository named "data.teskey". The name of this file should not be changed. Content in the key can be modified, for example replacing them with your own key.

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
[2]: https://www.python.org/downloads/release/python-397/
[3]: https://play.google.com/store/apps/details?id=com.termux
[4]: https://apps.apple.com/us/app/libterm/id1380911705
[5]: https://github.com/git-guides/install-git
[6]: https://docs.python.org/3/using/unix.html
