from ImageProcessor import ImageProcessor

imp = ImageProcessor()
arr = imp.load("../42AI.png")
print(arr)
# print(type(arr))
imp.display(arr)
