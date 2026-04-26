def main():
    cat = str(input("File name: ")).strip().casefold().replace('-', '')
    if cat.endswith('.gif'):
        print("image/gif")
    elif cat.endswith('.jpg'):
        print("image/jpeg")
    elif cat.endswith('.jpeg'):
        print("image/jpeg")
    elif cat.endswith('.png'):
        print("image/png")
    elif cat.endswith('.pdf'):
        print("application/pdf")
    elif cat.endswith('.txt'):
        print("text/plain")
    elif cat.endswith('.zip'):
        print("application/zip")
    else:
        print("application/octet-stream")






main()
