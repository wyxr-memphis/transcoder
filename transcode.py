import os
import csv
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

# Get the user's choice for the genre
print("Please choose a genre:")
print("1. Rock")
print("2. Funk and Soul")
print("3. Pop")
print("4. Hip-hop")
print("5. Electronic")

choice = int(input("Enter the number corresponding to your choice: "))
genres = ["Rock", "Funk and Soul", "Pop", "Hip-hop", "Electronic"]
selected_genre = genres[choice - 1]

# Initialize a list to store missing files
missing_files = []

# Read metadata from the CSV file
with open(metadata_file_path, 'r') as f:
    reader = csv.reader(f)
    header = [h.strip() for h in next(reader)]
    rows = [dict(zip(header, row)) for row in reader]

# Iterate through each row in the metadata file
for row in rows:
    wav_file_name = row['File']
    artist = row['Artist'].strip()
    album = row['Album'].strip()
    file_name = row['Song'].strip()
    date = row['Year'].strip()

    # Replace 'DA' with 'SP' in the wav_file_name
    input_wav_file_name = wav_file_name.replace('DA', 'SP')

    # Define input and output file paths
    input_file = os.path.join(input_directory, input_wav_file_name + '.wav')

    if not os.path.exists(input_file):
        missing_files.append((input_wav_file_name, artist, album, file_name))
        continue

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

# Print the list of missing files at the end of the script
if missing_files:
    print("\nThese files were not found:")
    for file_info in missing_files:
        file, artist, album, title = file_info
        print(f"{file}: {artist} - {album} - {title}")
else:
    print("\nAll files were processed successfully.")
