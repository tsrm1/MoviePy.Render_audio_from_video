from moviepy.editor import *
import os

media_folder = "./media"

# Создаём список файлов в каталоге 
files = os.listdir(media_folder)
print(f'files= {files}')

# отфильтровываем картинки и создаём список картинок
images = list(filter(lambda x: x.endswith('.jpg'), files))
print(f'images={images}')

# создаём видео из картнок и объединяем их в список
clips = [ImageClip(media_folder + '/' + m).set_duration(3) for m in images]

# # Связываем переменные с картинками/фото, устанавливаем длительность, сек.
# clip_1 = ImageClip(media_folder + '128432_or.jpg').set_duration(5)
# clip_2 = ImageClip(media_folder + 'Beautiful-Flowers-Closeup.jpg').set_duration(5)
# # clip_3 = ImageClip(media_folder + 'colorful-flowers.avif').set_duration(5)
# clip_4 = ImageClip(media_folder + 'cvety1.jpg').set_duration(5)

# # Склеиваем видео по очереди
# final_clip = concatenate_videoclips([clip_1, clip_2, clip_4], method='compose')
final_clip = concatenate_videoclips(clips, method='compose')


# Сохраняем видео в файл
final_clip.write_videofile(media_folder + '/' + 'slide_show.mp4', fps=25)

