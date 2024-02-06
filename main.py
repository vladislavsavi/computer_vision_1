from src import image_processing as img_proc
import cv2

if __name__ == "__main__":
    input_image = img_proc.read_img('assets/pepe.png')

    img_proc.showByCv2(input_image)
    img_proc.showByPlt(input_image)

    channels = img_proc.splitByChannels(input_image)

    print(cv2.COLOR_BGR2HSV)

    changed_image = img_proc.conversionByColorModel(input_image, cv2.COLOR_BGR2HSV)
    img_proc.showByCv2(changed_image)

    cv2.imwrite('output_image.jpg', changed_image)
