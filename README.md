# ObjectDetection

Setup the Application to the Machine.

1. clone the repository:
    cmd: git clone https://github.com/PKPurbey14432/ObjectDetection.git

2. goto the repository
    cmd : cd ObjectDetection

3. run the command and make sure the docker installed in your system
    cmd: docker compose up --build

4. open the link to see the swagger documentation on the browser
    link : http://localhost:8000/docs/

5. select the image to the form and wait for the response for some time

6. response will be in below format
    {
        "message": "Object detection successful",
        "filename": "Screenshot from 2024-12-21 14-53-36.jpg",
        "annotated_image_url": "http://localhost:8000/result/Screenshot from 2024-12-21 14-53-36.jpg",
        "detections": [
            {
            "xmin": 112.78993225097656,
            "ymin": 41.267967224121094,
            "xmax": 269.72467041015625,
            "ymax": 229.17672729492188,
            "confidence": 0.915153980255127,
            "class": 5,
            "name": "bus"
            },
        ]
    }

7. you can use the link of annotated_image_url on the browser to view the annoated image as well.

