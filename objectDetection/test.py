from inference import get_model
import supervision as sv
import cv2

# load a pre-trained yolov8n model
model = get_model(model_id="erc-cxkfa/1")

# create supervision annotators
bounding_box_annotator = sv.BoxAnnotator()
label_annotator = sv.LabelAnnotator()

# open webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise SystemExit("Could not open webcam")

try:
    while True:
        # read frame from webcam
        ok, frame = cap.read()
        if not ok:
            break

        # run inference on the frame
        results = model.infer(frame)[0]

        # load the results into the supervision Detections api
        detections = sv.Detections.from_inference(results)

        # annotate the frame with our inference results
        annotated_image = bounding_box_annotator.annotate(
            scene=frame, detections=detections)
        annotated_image = label_annotator.annotate(
            scene=annotated_image, detections=detections)

        # display the annotated frame
        cv2.imshow("Object Detection", annotated_image)
        
        # press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()