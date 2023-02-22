from pytube import YouTube
from pytube.exceptions import RegexMatchError

url = input("Ссылка: ")
try:
    yt = YouTube(url)
except RegexMatchError:
    raise ValueError("Неверная ссылка!")

print(yt.title)
print(yt.author)
print("Скачиваем файл")

type = input('1 - mp4, 2 - mp3: ')
if type == "1":
    try:
        yt.streams.filter(progressive=True, file_extension = 'mp4').order_by('resolution').desc().first().download('Video', f'{yt.title}.mp4')
    except OSError:
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download('Video', f'{yt.video_id}.mp4')
    print("Загрузка завершена")
elif type == "2":
    yt.streams.filter(only_audio=True).first().download('audio', f'{yt.title}.mp3')
    print('mp3 файл скачан')
