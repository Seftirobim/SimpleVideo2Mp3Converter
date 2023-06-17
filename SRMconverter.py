import os
#import string
from time import sleep
from rich.console import Console
from rich.markdown import Markdown
from moviepy.editor import VideoFileClip

console = Console()
title_markdown = """
# Simple Video To Mp3 Converter
"""
md = Markdown(title_markdown)

SRM_logo = """
  █████████  ███████████   ██████   ██████
 ███░░░░░███░░███░░░░░███ ░░██████ ██████ 
░███    ░░░  ░███    ░███  ░███░█████░███ 
░░█████████  ░██████████   ░███░░███ ░███ 
 ░░░░░░░░███ ░███░░░░░███  ░███ ░░░  ░███ 
 ███    ░███ ░███    ░███  ░███      ░███ 
░░█████████  █████   █████ █████     █████
 ░░░░░░░░░  ░░░░░   ░░░░░ ░░░░░     ░░░░░                                                                                            
"""

def print_title():
    console.print(SRM_logo, justify="center",style="bright_cyan")
    console.print('https://github.com/Seftirobim/SimpleVideo2Mp3Converter', justify="center", style="bold grey100")
    console.print(md)
    

#for convert all file .mp4 in folder
def convert_folder_to_mp3(input_folder,output_folder):
    with console.status("[bold] Sedang Memproses Harap Tunggu",spinner='point') as status:
        x = 1
        for filename in os.listdir(input_folder):
            if filename.endswith(('.mp4','.mkv')):
                input_file = os.path.join(input_folder, filename)
                output_file = os.path.join(output_folder,os.path.splitext(filename)[0] + '.mp3')
                convert_to_mp3(input_file, output_file)
                sleep(1)
                console.log(f"[green]Berhasil convert video[/green] {filename}")
                x += 1
        console.log(f"[bold][red]Selesai Memproses {x-1} file !")

def convert_to_mp3(input_file,output_file):
    video_clip = VideoFileClip(input_file)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_file, codec='mp3', logger=None)


#folder path
current_folder = os.getcwd()
input_folder = ''.join([current_folder,'/video'])
output_folder = ''.join([current_folder,'/converted'])

while True:
    try:
        print_title()
        prompt = input("Jalankan sekarang ? (y/N)")
    except:
        print("inputan salah")
    if prompt == 'y':
            if len(os.listdir(input_folder)) == 0:
                print("Folder masih kosong !!")
            else:
                convert_folder_to_mp3(input_folder,output_folder)
                break
    elif prompt == 'n':
        print("Terima kasih !")
        break
    else:
        print('Pilihan keliru, silahkan masukan (y/n)')
