from PIL import Image, ImageTk

def image(path, dim):
    file = Image.open(path)
    
    file = file.resize(dim)
    
    file = ImageTk.PhotoImage(file)
    
    return file