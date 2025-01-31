from pytubefix import YouTube
yt = YouTube(input('Cole sua url do youtube: '),
    use_oauth=True,
    allow_oauth_cache=True)
print(yt.title)
print(yt.thumbnail_url)
stream = yt.streams.get_highest_resolution()
stream.download()