def validar_email(email):
    return "@" in email and "." in email

def main():
    print(validar_email('teste@com.br'))

if __name__ == "__main__":
    main()