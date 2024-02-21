""" Извлекаем аудиодорожку из всех видео файлов.
    Видео файлы находятся в текущей папке.
    Создаём отдельную папку с готовым результатом
"""
import os, moviepy.editor                                                   # модуль для работы с видеофайлами
from pathlib import Path                                                    # модуль для работы с файлами, путь к файлу


CurrentFolder = '.'                                                         # текущая папка
TargetFolder = './mp3/'                                                     # папка назначение

if not os.path.exists(TargetFolder):                                        # создаём папку назначение, если её нет
    os.makedirs(TargetFolder)

for filename in os.listdir(CurrentFolder):
    if filename.lower().endswith(".mp4"): 
        video_file = Path(filename)                                         # присваиваем переменной путь к видеофайлу
        video = moviepy.editor.VideoFileClip(f'{video_file}')               # инициируем объект VideoFileClip, привязываем к нему видеофайл
        audio = video.audio                                                 # назначаем переменной audio метод .audio
        audio.write_audiofile(f'{TargetFolder + video_file.stem}.mp3')      # сохраняем аудиодорожку в файл, используя метод stem (путь к фалу без расширения)
        continue  




