import subprocess

# List of required packages
packages = [
    "spotipy",
    "python-dotenv",
    "tabulate"  # Optional, only if you want to use tabulate for table formatting
]

# Install each package
for package in packages:
    subprocess.run(["pip", "install", package], stdout=subprocess.PIPE, text=True)
