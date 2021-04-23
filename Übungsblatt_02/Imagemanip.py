from PIL import Image, ImageEnhance

def lightenup(picture, factor):
    im = Image.open("bilder/" + picture)
    enhancedPicture = ImageEnhance.Brightness(im)
    brightened_pic = enhancedPicture.enhance(factor)
    brightened_pic.save('test.png')
    return enhancedPicture

def binary(picture, factor):
   im = Image.open("bilder/" + picture)
   thresh = factor
   fn = lambda x : 255 if x > thresh else 0 # Wert zwischen 0-255 wählen
   binary_pic = im.convert('L').point(fn, mode ='1')
   binary_pic.save('test.png')

def sizing(picture, width, height):
     im = Image.open("bilder/" + picture)
     resized_image = im.resize((width,height)) # funktioniert noch nicht
     resized_image.save('test.png')

def ask_picture():
    input_picture = input("Welches Bild wollen sie wählen?") + ".pgm"
    return input_picture

def main():
    print("1 - Bild aufhellen/verdunkeln")
    print("2 - Binärbild erstellen")
    print("3 - Bildgröße ändern")
    print("4 - Programm beenden")
    user_choice = int(input("Was möchten Sie Tun?"))

    if user_choice == 1:
        input_picture = ask_picture()
        brightness_factor = int(input("Um welchen Faktor soll das Bild Heller/Dunkler gemacht werden?"))
        lightenup(input_picture,brightness_factor)
    elif user_choice == 2:
        input_picture = ask_picture()
        binary_factor = int(input("Welchen Faktor wollen Sie für das Binärbild?"+ "0-255"))
        binary(input_picture, binary_factor)
    elif user_choice == 3:
        input_picture = ask_picture()
        user_width = input("Welche Breite möchten sie ?")
        user_height = input("Welche Höhe möchten sie ?")
        sizing(input_picture,user_width,user_height)
    elif user_choice == 4:
        print("Programm wird beendet")
        exit()
    else:
        print("Falsche Auswahl")
        exit()

if __name__ == "__main__":
    main()
