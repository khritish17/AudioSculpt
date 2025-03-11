## Introduction

## Installation procedure

### Dependencies:
- `Python3`
- `OS` (Standard Python library for operating system interactions.)
- `pydub` (External library for audio manipulation. You can install it using: pip install pydub.)
- `FFMPEG` (pydub relies on either ffmpeg or libav. Ensure that one of these is installed and accessible in your system's PATH.)
## Fundamental Concepts

## Results

## Full documentation
### FILE: audio_libraries.py
Contains all the audio manipulation codes
#### Function: `convert_audio_to_wav`
This function converts audio files of various formats to WAV format using the `pydub` library.

**Purpose:**

- To provide a simple and robust way to convert audio files to the widely compatible WAV format.
- To handle both cases where the output location is specified and where it is not.
- To provide basic error handling for invalid input locations and conversion failures.

**Function Signature:**
```Python

def convert_audio_to_wav(input_location, output_location=""):
```
**Parameters:**
- `input_location` (str): The path to the input audio file. This can be an absolute or relative path.
- `output_location` (str, optional): The directory where the output WAV file should be saved. If not provided, the output file will be saved in the same directory as the input file, with the same name but a `.wav` extension.
**Return Value:**
- This function does not return any value. It prints messages to the console indicating the success or failure of the conversion.

**Functionality:**

1. **Input Validation:**
    - Checks if the `input_location` exists using `os.path.exists()`.
    - If the input location is invalid, prints an "Error: Invalid input location" message.
    - If the input location is valid, converts it to an absolute path using `os.path.abspath()`.
2. **Output Location Handling:**
    - If `output_location` is not provided (i.e., it's an empty string), the output file will be saved in the same directory as the input file. The output filename will be the same as the input filename but with a `.wav` extension.
    - If `output_location` is provided, the output file will be saved in the specified directory. The output filename will be the same as the input filename but with a `.wav` extension.
3. **Audio Conversion:**
    - Calls the nested function `convert_to_wav()` to perform the actual audio conversion using `pydub`.
    - The `convert_to_wav()` function:
        - Loads the audio file using `AudioSegment.from_file()`.
        - Exports the audio to a WAV file using `audio.export()`.
        - Includes a try-except block to catch potential errors during the conversion and print an "**Unexpected error occured during function call to 'convert_to_wav()'**" message if an error occurs.
    - Prints a "**Success: Audio converted successfully to wav format**" message upon successful conversion.
Nested Function:

```Python
def convert_to_wav(input_file_location, output_file_location):
    # ... (Implementation as described above)
```
This nested function handles the core audio conversion logic.
