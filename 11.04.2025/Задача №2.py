radius, side = map(float, input().split())

circumference = 2 * 3.14159 * radius

circle_area = 3.14159 * radius ** 2

square_area = side ** 2

percentage = (circle_area / square_area) * 100

print(f"Длина окружности равно {circumference:.2f}.\nПлощадь круга составляет {percentage:.2f} % от площади квадрата.")