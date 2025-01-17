from PIL import Image, ImageGrab
import requests

def create_image(url):
    r = requests.get(url)

    with open("profilepic.png", "wb") as f:
        f.write(r.content)

    background = Image.open("background.png")
    profilepic = Image.open("profilepic.png")

    background = background.resize((620, 620))
    profilepic = profilepic.resize((620, 400))

    crown = Image.open("crown.png")
    Image.Image.paste(background, profilepic, (0, 250))
    Image.Image.paste(background, crown, (0, 0))

    background.show()


def main():
    url = input("Enter URL of picture: ")
    create_image(url)


if __name__ == "__main__":
    main()