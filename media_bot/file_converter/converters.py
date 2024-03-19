from PIL import Image
from moviepy.editor import *
import docx2pdf

class VideoConverter:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def convert_to_mp4(self):
        video = VideoFileClip(self.file_name)
        new_name = os.path.splitext(self.file_name)[0] + ".mp4"
        video.write_videofile(new_name)
        print(f"File converted to MP4: {new_name}")

    def convert_to_mov(self):
        video = VideoFileClip(self.file_name)
        new_name = os.path.splitext(self.file_name)[0] + ".mov"
        video.write_videofile(new_name)
        print(f"File converted to MOV: {new_name}")

    def convert_to_mkv(self):
        video = VideoFileClip(self.file_name)
        new_name = os.path.splitext(self.file_name)[0] + ".mkv"
        video.write_videofile(new_name)
        print(f"File converted to MKV: {new_name}")


class ImageConverter:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def convert_to_jpg(self):
        image = Image.open(self.file_name)
        new_name = os.path.splitext(self.file_name)[0] + ".jpg"
        image.save(new_name)
        print(f"File converted to JPG: {new_name}")

    def convert_to_png(self):
        image = Image.open(self.file_name)
        new_name = os.path.splitext(self.file_name)[0] + ".png"
        image.save(new_name)
        print(f"File converted to PNG: {new_name}")

    def convert_to_gif(self):
        image = Image.open(self.file_name)
        new_name = os.path.splitext(self.file_name)[0] + ".gif"
        image.save(new_name)
        print(f"File converted to GIF: {new_name}")


class TextConverter:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def convert_to_txt(self):
        new_name = os.path.splitext(self.file_name)[0] + ".txt"
        docx2pdf.convert(self.file_name, new_name)
        print(f"File converted to PDF: {new_name}")

    def convert_to_docx(self):
        new_name = os.path.splitext(self.file_name)[0] + ".docx"
        docx2pdf.convert(self.file_name, new_name)
        print(f"File converted to DOCX: {new_name}")

    def convert_to_pdf(self):
        new_name = os.path.splitext(self.file_name)[0] + ".pdf"
        docx2pdf.convert(self.file_name, new_name)
        print(f"File converted to PDF: {new_name}")
