# CryptoVault
Cryptovault is a versatile encryption tool offering command-line efficiency, intuitive graphical controls, and remote accessibility via a web interface. Securely encrypt and decrypt folders with ease, whether you prefer direct commands, a user-friendly interface, or remote management capabilities.

## Installation

Clone the project

```bash
   git clone https://github.com/AnanthaBayary/CryptoVault.git
```

Go to the project directory

```bash
   cd CryptoVault
```
## Usage
#### Key Generation : ####

To Generate a key:
```bash
   python key.py
```
***

#### CLI : ####

To use the CLI.py file:
```bash
   python CLI.py <action> <folder_path> <key>
```
Encryption of folder:

```bash
   python CLI.py encrypt "C:\Users\Username\Documents\my_folder" bou9PrL52qwKxUfXKiS8wD6CVx65zzcTqIYZorKtRhU=
```
Decryption of folder:

```bash
   python CLI.py decrypt "C:\Users\Username\Documents\my_folder" bou9PrL52qwKxUfXKiS8wD6CVx65zzcTqIYZorKtRhU=
```
***
#### GUI : ####

To use the GUI.py file:
```bash
   python GUI.py
```
***

#### WEB : ####

Go to the Web directory:

```bash
  cd Web
```
Run the flask server :

```bash
  python app.py
```

#### Open browser : ####

Type the local address:

```bash
  http://127.0.0.1:5000
```
***

## License

[MIT](https://choosealicense.com/licenses/mit/)
***

## Disclaimer

This tool is for educational purposes only. Use responsibly and ensure compliance with applicable laws and regulations.
