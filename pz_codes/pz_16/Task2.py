# 1. Создайте класс Іmage

# 2. У каждого экземпляра класса должно быть три собственных атрибута
# -resolution
# -title
# -extension

# 3. В классе должен быть метод resize, с помощью которого можно
# поменять разрешение изображения.

# 4*. В классе должен быть метод title, you с поковые которого можна
# имя файла записать в верхнем регистре

#5. Создайте несколько экземпляров класса Іводе и вызовите для каждого
# метод resize

class Image:
    def __init__(self, title, extension, resolution):
        self.title = title
        self.extension = extension
        self.resolution = resolution

    def resize(self, new_resolution):
        self.resolution = new_resolution

    def change_title_case(self):
        self.title = self.title.upper()


image1 = Image("image1", "jpg", "1920x1080")
image2 = Image("image2", "png", "1280x720")

image1.resize("800x600")
image2.resize("1024x768")

print("image 1:")
print("title:", image1.title)
print("extension:", image1.extension)
print("resolution:", image1.resolution)

print("\nimage 2:")
print("title:", image2.title)
print("extension:", image2.extension)
print("resolution:", image2.resolution)

image1.change_title_case()
image2.change_title_case()

print("\nimage 1 Title Uppercase:", image1.title)
print("image 2 Title Uppercase:", image2.title)

