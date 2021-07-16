# WebM Converter

inspired by [nuttylamo's](https://github.com/nuttylmao) [Batch script](https://github.com/nuttylmao/Nutty-s-WebM-Converter) for converting video files to WebM files.

## Run

Download latest release uns zip and run the `webm_converter.exe` inside `webm_converter` folder.

## Bundle with PyInstaller (Windows only)

```
python3 -m pip install -r requirements.txt
python3 -m pip install pyinstaller
python3 -m PyInstaller --noconfirm webm_converter.spec
```