VERSION=0.1
FILE_NAME=webm_converter
TARGET=$(FILE_NAME)_v$(VERSION)

all: zip
	
zip: $(TARGET).zip

$(TARGET).zip: *.py images/* requirements.txt run.sh 
	python3 -m pip install -r requirements.txt
	python3 -m pip install pyinstaller
	python3 -m PyInstaller --noconfirm $(FILE_NAME).spec
	cp -r dist $(TARGET) 
	cp run.sh $(TARGET) 
	zip -r $(TARGET).zip $(TARGET) 
	rm -rf $(TARGET) 

.PHONY clean:
	-rm -rf build
	-rm -rf dist
	-rm -rf __pycache__
	-rm -rf $(TARGET) 
	-rm $(TARGET).zip
