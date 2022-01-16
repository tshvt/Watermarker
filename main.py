from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import os


class WatermarkMaker:
    def __init__(self):
        self.image = None

    def upload_file(self):
        try:
            f_types = [('image files', ('.png', '.jpg', '.jpeg'))]
            filename = filedialog.askopenfilename(filetypes=f_types)
            self.image = Image.open(filename)
            logo_image = Image.open("images/logo.png")
            self.image.paste(logo_image, (20, 20), logo_image)
            self.add_watermark()
        except AttributeError:
            pass

    def add_watermark(self):
        global img
        image = self.image
        if self.image.width >= 3000 or self.image.height >= 3000:
            image = self.image.resize((self.image.width // 5, self.image.height // 5))
        elif self.image.width >= 800 or self.image.height >= 800:
            image = self.image.resize((self.image.width // 3, self.image.height // 3))
        img = ImageTk.PhotoImage(image)
        title_label.destroy()
        text_1.destroy()
        text_2.destroy()
        upload_button.destroy()

        label = Label(image=img)
        label.config(pady=10, padx=10, background="#DBD1CC")
        label.grid(column=0, row=0, columnspan=2)

        another_img_button = Button(
            image=another_btn_img,
            highlightthickness=0,
            borderwidth=0,
            command=self.check_before_another
        )
        another_img_button.grid(column=0, row=1)

        save_button = Button(
            image=save_btn_img,
            highlightthickness=0,
            borderwidth=0,
            command=self.save_image
        )
        save_button.grid(column=1, row=1)

    def check_before_another(self):
        response = messagebox.askokcancel(
            title="Another Image",
            message="Are you sure? All the unsaved changes will be lost.")
        if response:
            self.upload_file()

    def save_image(self):
        root, ext = os.path.splitext(self.image.filename)
        self.image.save(root + "_marked" + ext)
        messagebox.showinfo(title="All done!", message="You watermarked image is saved.")


watermark_maker = WatermarkMaker()

# GUI
window = Tk()
window.title("Watermark Maker")
window.minsize(width=600, height=300)
window.config(padx=50, pady=50, background="#DBD1CC")

title_image = PhotoImage(file="images/title.png")
title_label = Label(image=title_image)
title_label.config(background="#DBD1CC")
title_label.grid(column=2, row=1)

text_1_image = PhotoImage(file="images/text_1.png")
text_1 = Label(image=text_1_image)
text_1.config(background="#DBD1CC")
text_1.grid(column=1, row=2)

text_2_image = PhotoImage(file="images/text_2.png")
text_2 = Label(image=text_2_image)
text_2.config(background="#DBD1CC")
text_2.grid(column=3, row=2)


# Buttons Images
upload_btn_img = PhotoImage(file="images/button_upload-image.png")
another_btn_img = PhotoImage(file="images/button_another-image.png")
save_btn_img = PhotoImage(file="images/button_save-image.png")


upload_button = Button(image=upload_btn_img,
                       highlightthickness=0,
                       borderwidth=0,
                       command=lambda: watermark_maker.upload_file())

upload_button.grid(column=2, row=3)


window.mainloop()
