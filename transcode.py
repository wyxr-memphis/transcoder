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

# Get the user's choice for the genre
print("Please choose a genre for this import batch:")
print("1. Rock")
print("2. Funk and Soul")
print("3. Pop")
print("4. Hip-hop")
print("5. Electronic")

choice = int(input("Enter the number corresponding to your choice: "))
genres = ["Rock", "Funk and Soul", "Pop", "Hip-hop", "Electronic"]
selected_genre = genres[choice - 1]

# Iterate through each line in the metadata file
for line in lines:
    # Split the line into parts
    parts = line.strip().split(',')

    # Check if the line has a date
    if len(parts) == 5:
        wav_file_name, artist, album, file_name, date = parts
    else:
        wav_file_name, artist, album, file_name = parts
        date = ""

    # Replace 'DA' with 'FUS' in the wav_file_name
    input_wav_file_name = wav_file_name.replace('DA', 'FUS')

    # Define input and output file paths
    input_file = os.path.join(input_directory, input_wav_file_name + '.wav')

    # Construct the output file name with artist, album, and desired output file name
    output_file_name = f"{artist} - {album} - {file_name}"
    output_file = os.path.join(output_directory, output_file_name + '.m4a')

    # Make sure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Set the title metadata to include artist, album, and song title
    title = f"{artist} - {album} - {file_name}"

    # Transcode the WAV file to AAC using FFmpeg with a reduced bitrate and add metadata
    ffmpeg_command = [
        'ffmpeg', '-i', input_file, '-vn', '-c:a', 'aac', '-b:a', '96k',
        '-metadata', f'artist={artist}', '-metadata', f'album={album}', '-metadata', f'title={title}', '-metadata', f'year={date}', '-metadata', f'genre={selected_genre}', output_file
    ]

    subprocess.run(ffmpeg_command)
