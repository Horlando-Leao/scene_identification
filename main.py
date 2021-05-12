from classImage.ImagesDetector import ImagesDetector
from classImage.CleaningImages import CleaningImages

if __name__ == '__main__':

    novoDetec = ImagesDetector([1,0,1,1,1,0,1,1,0])
    print(novoDetec.image)
    print(novoDetec)

    clearImag = CleaningImages.get_type_clear_one()
    print(clearImag)

