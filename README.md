## pyinstaller
```bash
python -O -m PyInstaller --windowed --onefile .\main.py
```

## yolo
### install
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
git clone https://github.com/ultralytics/ultralytics.git
cd ultralytics
git checkout v8.3.27
cd ..
pip install ./ultralytics
```
### Train
```bash
yolo.exe train imgsz=896 batch=2 epochs=5 data='N:\\programming\\plasma\\yolo_training_gray\\dataset.yaml' model='yolo11s.pt' amp=False
```
