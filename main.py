import whisper
import time
import platform
import sys

# Load Whisper model
model = whisper.load_model("tiny")

# Audio files
files = [
    "audio/clean.wav",
    "audio/noise.wav"
]

# Environment details
print("\n===== Environment Details =====")
print("OS :", platform.system(), platform.release())
print("Python :", sys.version)
print("Model :", "tiny")
print()

# Process each file
for file in files:

    print("Processing :", file)

    start = time.time()

    result = model.transcribe(file)

    end = time.time()

    output = {
        "sample": file,
        "transcript": result["text"].strip(),
        "time_sec": round(end - start, 2)
    }

    print(output)
    print()