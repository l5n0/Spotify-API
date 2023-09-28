import subprocess

packages = [
    "spotipy",
    "python-dotenv",
    "tabulate"  
]
for package in packages:
    subprocess.run(["pip", "install", package], stdout=subprocess.PIPE, text=True)
