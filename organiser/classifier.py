from pathlib import  Path

def classifier(path:Path , config):
    file_extension= path.suffix.lower()

    for category, data in config["categories"].items():
        extensions = data["extension"]
        if file_extension in extensions:
            return category
    return "others"




