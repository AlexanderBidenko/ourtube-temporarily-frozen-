from pytube import YouTube


video_url = 'https://www.youtube.com/watch?v=G0aekmshR4A'


def download(video_url):
    yt_obj = YouTube(video_url)
    filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
    video_title = yt_obj.title
    # download the highest quality video
    filters.get_highest_resolution().download()
    print(video_title)
    print('Video Downloaded Successfully')
    return video_title


yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
print(yt.captions)
