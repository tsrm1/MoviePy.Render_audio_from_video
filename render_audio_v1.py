""" Извлекаем аудиодорожку из видео файла.
    Название видеофайла и аудиофайла прописываем вручную.
"""
import moviepy.editor                               # модуль для работы с видеофайлами

video = moviepy.editor.VideoFileClip('video-1.mp4') # название видеофайла
audio = video.audio                                 # назначаем переменной audio метод .audio
audio.write_audiofile('my_audio.mp3')               # сохраняем аудиодорожку в файл

