import os
import subprocess

# Define input and output directories
input_directory = '/Users/robbygrant/scripts/transcoder/files'
output_directory = '/Users/robbygrant/scripts/transcoder/mp3s'

# Read metadata from the text file
with open('metadata.txt', 'r') as f:
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
    output_file = os.path.join(output_directory, output_file_name)

    # Make sure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Set the title metadata to just the song name with the wav file name (FUS prefix)
    title = os.path.splitext(file_name)[0]

    # Transcode the WAV file to MP3 using FFmpeg and add metadata
    ffmpeg_command = [
        'ffmpeg', '-i', input_file, '-vn', '-ar', '44100', '-ac', '2', '-b:a', '192k',
        '-metadata', f'artist={artist}', '-metadata', f'album={album}', '-metadata', f'title={title}', '-metadata', f'Year={year}', output_file
    ]

    subprocess.run(ffmpeg_command)
