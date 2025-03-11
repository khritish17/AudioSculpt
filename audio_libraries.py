import os
from pydub import AudioSegment
def convert_audio_to_wav(input_location, output_location = ""):
    def convert_to_wav(input_file_location, output_file_location):
        try:
            audio = AudioSegment.from_file(input_file_location)
            audio.export(output_file_location, format = "wav")
        except:
            print("Unexpected error occured during function call to 'convert_to_wav()'")

    # check for valid input location
    if os.path.exists(input_location):
        input_location = os.path.abspath(input_location)
        if output_location == "":
            # if output location not provided, the output will be in the same directory as input
            base, ext = os.path.splitext(input_location)
            output_location = f"{base}.wav"
        else:
            # if output location is provided, output will be in given location
            base_with_extension = os.path.basename(input_location)
            file_name, ext = os.path.splitext(base_with_extension)
            output_location += f"/{file_name}.wav"
        
        # call to a nested function for conversion 
        convert_to_wav(input_file_location= input_location, output_file_location= output_location)
        print("Success: Audio converted successfully to wav format")
    else:
        print("Error: Invalid input location")

# # Test Case
# convert_audio_to_wav(input_location=r"D:\Codes\Projects\AudioSculpt\test.mp3")