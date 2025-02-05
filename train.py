from ultralytics import YOLO

if __name__ == '__train__':
    model = YOLO("yolov8n.yaml")
    results = model.train(data="config.yaml", epochs=1, workers=0, device='cpu')
