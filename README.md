# Audio Transcription Script Using Whisper
This script allows you to transcribe audio files using OpenAI's Whisper API. It makes use of the 1Password CLI to retrieve the OpenAI API key.

## Prerequisites
1Password CLI: You must have the [1Password CLI](https://developer.1password.com/docs/cli/get-started/) installed and set up on your machine.

Python 3.x: Ensure you have Python 3 installed. You can check using python --version.

## Dependencies
This script requires the following Python libraries:

`dotenv`: For loading environment variables.

`openai`: For interacting with the OpenAI API.

`pydub`: For converting audio files to mp3 format.

You can install these dependencies using pip:

```
pip install python-dotenv openai pydub
```

## Usage
Ensure that an environment variable is set to the 1Password secret reference of your OpenAI API key.


```
export OPENAI_API_KEY="op://vault/item/field"
```

To transcribe an audio file, use the following command:

```
op run -- python3 transcribe.py <file_name>
```

Replace <file_name> with the path to your audio file.

**Note**: The script can process audio files of various formats, but will convert them to mp3 before transcribing.

## Configuration
Ensure you have the OpenAI API key stored securely in 1Password and that the environment variable "OPENAI_API_KEY" is set with the correct secret reference.
