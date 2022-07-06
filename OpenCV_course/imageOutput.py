import numpy as np
import cv2

image = cv2.imread("Image/lunar.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Moon", image)
cv2.waitKey()
cv2.destroyAllWindows()

print(image.shape)
h, w , c = image.shape
print("heihgt", h, "width", w, "channel", c)