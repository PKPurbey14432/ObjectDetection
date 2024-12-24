
from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
import torch
import shutil
import os
import glob


app = FastAPI()

# Load YOLOv5 model
model = torch.hub.load("ultralytics/yolov5", "yolov5s")
os.mkdir("result")
app.mount("/result", StaticFiles(directory="result"), name="result")

@app.post("/object-detect/")
async def detect_objects(file: UploadFile = File(...)):
    try:
        os.makedirs("data", exist_ok=True)
        if os.path.exists("result"):
            shutil.rmtree("result")

        files = glob.glob("result/*")
        for f in files:
            os.remove(f)

        temp_image_path = f"data/{file.filename}"
        with open(temp_image_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        results = model(temp_image_path)

        results.save(save_dir="result")

        annotated_image_path = f"result/{file.filename}"
        saved_files = glob.glob("result/*")
        if saved_files:
            annotated_image_path = saved_files[0]

        os.remove(temp_image_path)


        detections = results.pandas().xyxy[0]
        detection_json = detections.to_dict(orient="records")

        response_data = {
            "message": "Object detection successful",
            "filename": os.path.basename(annotated_image_path),
            "annotated_image_url": f"http://localhost:8000/result/{os.path.basename(annotated_image_path)}",
            "detections": detection_json,

        }

        return JSONResponse(content=response_data, status_code=200)
    except Exception as e:
        res = {
            "message": f"error: {e}",
        }
        return JSONResponse(content=res, status_code=500)
