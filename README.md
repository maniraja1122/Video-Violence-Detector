# Video-Violence-Detector
It will detect person in a video using YOLOv3 and then classify the scene as violent or non-violent based on my own trained model (Models/model_image_95) which has VGG16 and other layers. It gave accuracy of more than 95% and was trained on dataset [Violence vs. Non-Violence: 11K Images Dataset](https://www.kaggle.com/datasets/abdulmananraja/real-life-violence-situations). The dataset is also processed (Preprocessing/fileconvertor.py) by me using previous datasets and converting images to 416x416 which is the input size of YOLOv3.
I tested it on samples (Samples/) and it classified them as

| Sample           | Model Prediction         | True  |
| ----------------:|:------------------------:| -----:|
| imran.mp4        | Non-Violent              | Yes   |
| non_violence.mp4 | Non-Violent              | Yes   |
| railway.mp4      | Violent                  | Yes   |
| ufc.mp4          | Violent                  | Yes   |
| violence.mp4     | Violent                  | Yes   |
