import random


def main():
    name = input("Name: ")
    description = input("Desc: ")

    with open("text.html", "w") as file:
        file.writelines(["\n<!DOCTYPE html>"
        "\n<html lang='en'>"
        "\n<head>"
        "\n<meta charset='UTF-8'>"
        "\n<title>Title</title>"
        "\n</head>"
        "\n<body>"
        "\n<center>"
        "\n<h1>"
        f"{name}"
        "\n</h1>"
        "\n<center>"
        "\n<hr>"
        f"{description}"
        "\n</body>"
        "\n</html>"])

main()
