.DS_Store# Audio Transcoder

This Python script transcodes WAV files to M4A files using FFmpeg while adding metadata from a provided CSV file. The script also allows users to choose a genre for the transcoded files and logs any missing files.

## Prerequisites

Before running the script, you need to have the following:

1. Python 3.x installed
2. FFmpeg installed and added to the PATH (https://ffmpeg.org/download.html)

## Configuration

You need to create a `config.txt` file in the same directory as the script, with the following format:

		input_directory: <path_to_input_directory>
		output_directory: <path_to_output_directory>
		metadata_file_path: <path_to_metadata_file>


Replace `<path_to_input_directory>` with the path to the folder containing your input WAV files, `<path_to_output_directory>` with the path to the folder where you want the transcoded M4A files to be saved, and `<path_to_metadata_file>` with the path to the CSV file containing the metadata.

## Metadata CSV Format

The metadata CSV file should have the following format:


Here's a README file for the GitHub repo:

vbnet
Copy code
# Audio Transcoder

This Python script transcodes WAV files to M4A files using FFmpeg while adding metadata from a provided CSV file. The script also allows users to choose a genre for the transcoded files and logs any missing files.

## Prerequisites

Before running the script, you need to have the following:

1. Python 3.x installed
2. FFmpeg installed and added to the PATH (https://ffmpeg.org/download.html)

## Configuration

You need to create a `config.txt` file in the same directory as the script, with the following format:

input_directory: <path_to_input_directory>
output_directory: <path_to_output_directory>
metadata_file_path: <path_to_metadata_file>

vbnet
Copy code

Replace `<path_to_input_directory>` with the path to the folder containing your input WAV files, `<path_to_output_directory>` with the path to the folder where you want the transcoded M4A files to be saved, and `<path_to_metadata_file>` with the path to the CSV file containing the metadata.

## Metadata CSV Format

The metadata CSV file should have the following format:

File,Song,Artist,Album,Year,Category,Start Date,End Date,Upload Date,Column J,Column K,Duration,Column M,Column N


The script expects the following columns:

- File: The name of the input WAV file without the extension (e.g., DA0000)
- Song: The song title
- Artist: The artist name
- Album: The album name
- Year: The release year

Other columns will be ignored.

## Running the Script

To run the script, open a terminal, navigate to the folder containing the script, and run:

python transcode.py


The script will prompt you to choose a genre for the transcoded files. Enter the number corresponding to your choice and press Enter. The script will then process the files and display a log of any missing files at the end.

## Output

The script will create M4A files with a bitrate of 96 kbps in the specified output directory. The file names will have the following format:

<Artist> - <Album> - <Song>.m4a

The metadata, including artist, album, title, year, and the selected genre, will be embedded in the M4A files.
