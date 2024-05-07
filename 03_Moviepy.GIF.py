from moviepy.editor import *


media_folder = "./media/"

# # Связываем переменные с видео
# # Обрезаем видео с .. по .. сек.
# clip = VideoFileClip(media_folder + 'chaplin.mp4').subclip(5, 7)

# Изменяем размер изображения, на 50%
clip = VideoFileClip(media_folder + 'chaplin.mp4').subclip(5, 7).resize(0.5)

# Создаём анимированное изображение
clip.write_gif(media_folder + 'gifka.gif')

