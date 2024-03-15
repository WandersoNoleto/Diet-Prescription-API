from pytube import YouTube


MEDIA_PATH = 'media_bot/youtube/media/'

class YoutubeDownloader:
    @staticmethod
    def download_video(link: str) -> str:
        try:
            yt        = YouTube(link)
            video     = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            file_path = video.download(output_path=MEDIA_PATH)
            return file_path
        except Exception as e:
            return f"An error occurred: {str(e)}"
        
    @staticmethod
    def download_audio(link: str) -> str:
        try:
            yt = YouTube(link)
            audio_stream = yt.streams.filter(only_audio=True).first()
            file_path = audio_stream.download(output_path=MEDIA_PATH)
            return file_path
        except Exception as e:
            return f"An error occurred: {str(e)}"