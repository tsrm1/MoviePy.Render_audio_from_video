from moviepy.editor import *

# video = VideoFileClip("myHolidays.mp4").subclip(50,60)

# # Make the text. Many more options are available.
# txt_clip = ( TextClip("My Holidays 2013",fontsize=70,color='white')
#              .with_position('center')
#              .with_duration(10) )

# result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
# result.write_videofile("myHolidays_edited.webm",fps=25) # Many options...

media_folder = "./media/"

# Связываем переменные с видео
clip_1 = VideoFileClip(media_folder + 'chaplin.mp4')
clip_2 = VideoFileClip(media_folder + 'video_with_failing_audio.mp4')

# Склеиваем видео по очереди
final_clip = concatenate_videoclips([clip_1, clip_2])

# Снижаем громкость в видео
final_clip = final_clip.volumex(0.5)

# Сохраняем видео в файл
final_clip.write_videofile(media_folder + 'final_clip.mp4')

# Определяем продолжительность видео, сек.
print(f"Длительность видео {clip_1} = {clip_1.duration} sec.")
print(f"Длительность видео {clip_2} = {clip_2.duration} sec.")
print(f"Длительность видео {final_clip} = {final_clip.duration} sec.")

# Обрезаем видео с .. по .. сек.
final_clip = final_clip.subclip(3, 7)
print(f"Длительность видео {final_clip} = {final_clip.duration} sec.")

