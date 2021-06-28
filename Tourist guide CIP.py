import easyocr
from pylab import rcParams
from IPython.display import Image
from googletrans import Translator, constants
from pprint import pprint
from tkinter import Tk, Button, Label, DoubleVar, Entry
from geopy.geocoders import Nominatim
from haversine import haversine, Unit
import math

print("Enter 1 to only read text from an image.")
print("Enter 2 to translate the text from a given image to your desired language")
print("Enter 3 to convert money entered in Rs to other currencies.")
print("Enter 4 to know how far is your destination from your present location")
print("Enter 5 to exit.")
ch = int(input("Enter your choice: "))

while ch!=5 :

    #EXTRACTION OF TEXT FROM AN IMAGE
    if ch == 1:
        pprint(constants.LANGUAGES)
        rcParams['figure.figsize'] = 8, 16

        flang = input("Enter code of suspected foreign language:")

        print("Please wait....")
        reader = easyocr.Reader([flang, "en"])
        source_img = r"C:\Users\KIIT\Documents\CIP\CIP Final Project\German text1.jpg" #THE LOCATION OF THE IMAGE IS STORED HERE
        Image(source_img)
        output = reader.readtext(source_img)
        listToStr = ' '.join(map(str, output))
        string = listToStr
        text = ""

        for char in string:

            if char.isalpha() or char ==' ' :
                text += char

        print("\nThe text is:", text.strip())
        print()

    # TRANSLATION OF THE TEXT READ FROM AN IMAGE
    if ch==2:
        pprint(constants.LANGUAGES)
        rcParams['figure.figsize'] = 8, 16

        flang = input("Enter code of suspected foreign language:")

        print("Please wait....")
        reader = easyocr.Reader([flang, "en"])
        source_img = r"C:\Users\KIIT\Documents\CIP\CIP Final Project\German text1.jpg" #THE LOCATION OF THE IMAGE IS STORED HERE
        Image(source_img)
        output = reader.readtext(source_img)
        listToStr = ' '.join(map(str, output))
        string = listToStr
        only_alpha = ""
        for char in string:

            if char.isalpha() or char == ' ':
                only_alpha += char
        text = only_alpha
        print("\nThe text is:", text.strip())
        print()

        translator = Translator()
        lang = input("Enter your language code:")
        translation = translator.translate(text, dest=lang)
        print()
        print("The translated text is:")
        print(f"{translation.text}({translation.dest})")
        detection = translator.detect(text)
        print("\nOriginal language was:", constants.LANGUAGES[detection.lang])
        
    # TO CONVERT MONEY ENTERED IN INDIAN RUPEES TO 5 OTHER CURRENCIES- USD,GBP,KRW,CNY,JPY
    if ch==3:
        win = Tk()
        win.title("CURRENCY CONVERTOR")
        win.configure(background="pink")
        win.attributes("-fullscreen", False)

        def conversion():
            #THIS FUNCTION CONVERTS INDIAN RUPEES TO VARIOUS CURRENCIES
            val = float(inr_entry.get())
            dol = val * 0.0135
            usd_value.set("%.4f" % dol)
            po = val * 0.0097
            pound_value.set("%.4f" % po)
            krw = val * 15.1894
            won_value.set("%.4f" % krw)
            yuan = val * 0.087
            cny_value.set("%.4f" % yuan)
            yen = val * 1.4928
            jpy_value.set("%.4f" % yen)
    
        def reset_values():
           #THIS FUNCTION CLEARS ALL THE EXISTING VALUES SO THAT NEW VALUES CAN BE ENTERED
           inr_value.set("")
           usd_value.set("")
           pound_value.set("")
           won_value.set("")
           cny_value.set("")
           jpy_value.set("")
    
        inr_lbl = Label(win, text="RUPEES (INR)", bg="purple", fg="white", width=14)
        inr_lbl.grid(column=0,row=0,padx=60,pady=15)

        inr_value = DoubleVar()
        inr_entry = Entry(win,textvariable=inr_value,width=14)
        inr_entry.grid(column=1,row=0)
        inr_entry.delete(0,'end')

        usd_lbl = Label(win, text="US DOLLAR (USD)", bg="purple", fg="white", width=14)
        usd_lbl.grid(column=0,row=1)

        usd_value = DoubleVar()
        usd_entry = Entry(win,textvariable=usd_value,width=14)
        usd_entry.grid(column=1,row=1,pady=15, padx=60)
        usd_entry.delete(0,'end')

        pound_lbl = Label(win, text="POUND (GBP)", bg="purple", fg="white", width=14)
        pound_lbl.grid(column=0,row=2)

        pound_value = DoubleVar()
        pound_entry = Entry(win,textvariable=pound_value,width=14)
        pound_entry.grid(column=1,row=2,pady=15,padx=60)
        pound_entry.delete(0,'end')

        won_lbl = Label(win, text="WON (KRW)", bg="purple", fg="white", width=14)
        won_lbl.grid(column=0,row=3)

        won_value = DoubleVar()
        won_entry = Entry(win,textvariable=won_value,width=14)
        won_entry.grid(column=1,row=3,pady=15, padx=60)
        won_entry.delete(0,'end')

        cny_lbl = Label(win, text="YUAN (CNY)", bg="purple", fg="white", width=14)
        cny_lbl.grid(column=0,row=4)

        cny_value = DoubleVar()
        cny_entry = Entry(win,textvariable=cny_value,width=14)
        cny_entry.grid(column=1,row=4,pady=15, padx=60)
        cny_entry.delete(0,'end')

        jpy_lbl = Label(win, text="YEN (JPY)", bg="purple", fg="white", width=14)
        jpy_lbl.grid(column=0,row=5)

        jpy_value = DoubleVar()
        jpy_entry = Entry(win,textvariable=jpy_value,width=14)
        jpy_entry.grid(column=1,row=5,pady=30, padx=60)
        jpy_entry.delete(0,'end')

        #CREATES THE CONVERT BUTTON
        convert_bt = Button(win, text="Convert", bg="black", fg="white",width=14,command=conversion)
        convert_bt.grid(column=0,row=6,padx=30)

        #CREATES THE RESET BUTTON
        re_bt = Button(win, text="Reset", bg="black", fg="white", width=14, command=reset_values)
        re_bt.grid(column=1, row=6)

        win.mainloop() 

    # TO CALCULATE THE DISTANCE BETWEEN THE USER'S PRESENT LOCATION AND A PLACE OF INTEREST ENTERED BY THE USER
    if ch==4 :
        address = input("Enter your present location: ")
        geolocator = Nominatim(user_agent="Your_Name")
        location = geolocator.geocode(address)
        Latitude = location.latitude
        Longitude = location.longitude
        address2 = input("Enter your destination: ")
        location2 = geolocator.geocode(address2)
        Latitude2 = location2.latitude
        Longitude2 = location2.longitude
        user_loc = (Latitude, Longitude)
        final_loc = (Latitude2, Longitude2)
        dist = haversine(user_loc, final_loc)
        print("\nYou are",dist,"km away from your destination.")
        print()
        
    print("Enter 1 to read the text from an image")
    print("Enter 2 to translate a given text to your desired language")
    print("Enter 3 to convert money entered in Rs to other currencies.")
    print("Enter 4 to know how far is your destination from your present location")
    print("Enter 5 to exit.")
    ch = int(input("Enter your choice: "))
print("Bye ! Thank you!!!") 