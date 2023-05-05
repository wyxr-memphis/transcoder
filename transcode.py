import os
import subprocess

# Read paths from config.txt
with open('config.txt', 'r') as f:
    config_lines = f.readlines()

config = {}
for line in config_lines:
    if ':' not in line:
        continue

    key, value = line.strip().split(':')
    config[key] = value

input_directory = config['input_directory']
output_directory = config['output_directory']
metadata_file_path = config['metadata_file_path']

# Read metadata from the text file
with open(metadata_file_path, 'r') as f:
    lines = f.readlines()

# Iterate through each line in the metadata file
for line in lines:
    # Split the line into parts
    parts = line.strip().split(',')

    # Check if the line has a year
    if len(parts) == 5:
        wav_file_name, artist, album, file_name, year = parts
    else:
        wav_file_name, artist, album, file_name = parts
        year = ""

    # Replace 'DA' with 'FUS' in the wav_file_name
    input_wav_file_name = wav_file_name.replace('DA', 'FUS')

    # Define input and output file paths
    input_file = os.path.join(input_directory, input_wav_file_name + '.wav')
    
    # Construct the output file name with artist, album, and desired output file name
    output_file_name = f"{artist} - {album} - {file_name}"
    output_file = os.path.join(output_directory, output_file_name + '.aac')

    # Make sure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Set the title metadata to just the song name with the wav file name (FUS prefix)
    title = os.path.splitext(file_name)[0]

    # Transcode the WAV file to AAC using FFmpeg with a reduced bitrate and add metadata
    ffmpeg_command = [
        'ffmpeg', '-i', input_file, '-vn', '-ar', '44100', '-ac', '2', '-c:a', 'aac', '-b:a', '96k',
        '-metadata', f'artist={artist}', '-metadata', f'album={album}', '-metadata', f'title={title}', '-metadata', f'year={year}', output_file
    ]

    subprocess.run(ffmpeg_command)
