#!/user/bin/python3
import zipfile

def extract_zip(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode())
        print(f"Password found: {password}")
    except:
        pass

def brute_force(zip_file, wordlist):
    with open(wordlist, "r") as f:
        for line in f.readlines():
            password = line.strip()
            extract_zip(zip_file, password)

def main():
    target_zip = "target.zip"
    secret_message = "secret_message.txt"
    password = "password123"

    # Create zip file with password protection
    with zipfile.ZipFile(target_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.setpassword(password.encode())
        zf.write(secret_message)

    # Brute force attack
    wordlist = "RockYou.txt"
    brute_force(zipfile.ZipFile(target_zip), wordlist)

if __name__ == "__main__":
    main()
# chatgbt.com