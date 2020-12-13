from PIL import Image
from tkinter import Tk, PhotoImage, Canvas, NW



def algoritm (txtname, imagename, mode, size = (960,540)):
    size = size[::-1] if format == 1 else size
    img = Image.new("RGB", size, "white")
    f = open(txtname, "r")
    data = f.read().split("\n")
    for i in range(len(data)-1):
        data[i] = data[i].split(" ")
        if mode == 1:
            img.putpixel((int(data[i][0]), int(data[i][1])), (0, 0, 0))
        else:
            img.putpixel((int(data[i][1]), 540 - int(data[i][0]) if format == 3 else int(data[i][0])), (0, 0, 0))
    img.save(f"{imagename}.png")
    return size


def main():
    txtname = input("Enter dataset name (DS7.txt):\n")
    imagename = input("Enter name of the new image:\n")
    mode = (int(input("1. Direct dataset visualisation \n"
                      "2. Dataset_visualisation visualisation with changed coordinates\n"
                      "3. Dataset_visualisation visualisation with changed coordinates and normal visualisation\n"
                      "\nEnter 1, 2 or 3\n")))
    while mode not in (1, 2, 3):
        mode = (int(input("1. Direct dataset visualisation \n"
                          "2. Dataset_visualisation visualisation with changed coordinates\n"
                          "3. Dataset_visualisation visualisation with changed coordinates and normal visualisation\n"
                          "\nEnter 1, 2 or 3\n")))
    size = algoritm(txtname, imagename, mode)
    windowMain = Tk()
    windowMain.geometry(f'{size[0]}x{size[1]}+50+50')
    ph_im = PhotoImage(file=f'{imagename}.png')
    canv = Canvas(windowMain, width=size[0], height=size[1])
    canv.create_image(1, 1, anchor=NW, image=ph_im)
    canv.place(x=10, y=10)
    windowMain.mainloop()
    restart = input("Do you want to continue? (y/n)\n")
    if restart == "y":
        main()


if __name__ == '__main__':
    main()


