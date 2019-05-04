import os
import subprocess
import pytube

# Get information from YouTube
url = input('Input URL to download: ')
yt = pytube.YouTube(url)
videos = yt.streams.all()

# Print got information
for i in range(len(videos)):
	print(i, ', ', videos[i])

# Download
key_input = int(input('Input index to download: '))
download_dir = "./"
videos[key_input].download(download_dir)

# Convert to mp3
original_fname = videos[key_input].default_filename
new_fname = input('Input file name to save: ')
subprocess.call(['./ffmpeg', '-i',
    os.path.join(download_dir, original_fname),
    os.path.join(download_dir, new_fname)])

print('Download and Convert Complete !!!')
