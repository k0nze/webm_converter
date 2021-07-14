# WebM Converter

inspired by [nuttylamo's](https://github.com/nuttylmao) [Batch script](https://github.com/nuttylmao/Nutty-s-WebM-Converter) for converting video files to WebM files.

## Windows
### Run
Download latest release uns zip and run the `webm_conversion.exe` inside `webm_conversion` folder.

### Bundle with PyInstaller (Windows only)
```
python3 -m pip install -r requirements.txt
python3 -m pip install pyinstaller
python3 -m PyInstaller --noconfirm webm_converter.spec
```

## Ubuntu/Linux
### Install
```
sudo apt install ffmpeg
python3 -m pip install -r requirements.txt
```

### Run
```
python3 webm_converter.py
```
