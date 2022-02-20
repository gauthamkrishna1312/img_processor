from email.mime import image
from PIL import Image

def imgsizing():
    
    imgname = str(input("Enter image name\n"))
    width = int(input("Enter width\n"))
    height = int(input("Enter height\n"))
    size = width,height
    
    image2 = Image.open(f'{imgname}') # Here used f string
    image2.thumbnail(size)
    image2.save(f'11{imgname}')
    
def imgformatting():
    print("Conertions on jpg,jpeg,png files only")
    imgname = str(input("Enter image with extention\n"))
    imgformat = str(input("Enter image format\n")) 
    
    
    if imgformat == 'png':
        image01 = Image.open(f'{imgname}')
        image01.save('img001.jpg')
        image01.save('img0012.jpeg')
        print("png image converted into jpeg ang jpg")
    elif imgformat == 'jpg':
        image01 = Image.open(f'{imgname}')
        image01.save('img001.png')
        image01.save('img0012.jpeg')
        print("jpg image converted into png ang jpeg")
    elif imgformat == 'jpeg':
        image01 = Image.open(f'{imgname}')
        image01.save('img001.jpg')
        image01.save('img0012.png')
        print("jpeg image converted into png ang jpg")
        
    
imgsizing()                
    #image1 = Image.open('Pic 1.jpg')
    #image1.save('Img001.jpeg')
    #image1.save('Img001.jpg')

imgformatting()