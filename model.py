from ultralytics import YOLO

model = YOLO("bestv3.pt")
model.export(format="onnx")
