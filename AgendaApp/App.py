import json

def main():

    while True:
        try:
            f = open("Meses.txt", encoding="utf8")
            linhas = f.readlines()
            for linha in linhas:
                print(linha)
            break
        except:
            print("Oops!")
if __name__ == "__main__":
    main()
