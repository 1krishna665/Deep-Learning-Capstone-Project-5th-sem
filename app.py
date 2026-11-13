"""
Smart Campus Scene Recognition - Backend Service
Serves the web frontend and runs PyTorch MobileNetV3-Large inference.
"""

import io
import os
import torch
import torchvision.transforms as transforms
from torchvision.models import mobilenet_v3_large, MobileNet_V3_Large_Weights
import torch.nn as nn
from PIL import Image
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder=".")
CORS(app)

# Target Classes identical to the capstone dataset
CLASS_NAMES = [
    "Classroom",
    "Common_Canteen",
    "Corridor",
    "Laboratory",
    "Library",
    "Office"
]

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Model Preprocessing (standard ImageNet 224x224 transforms used in notebook)
inference_transforms = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

def load_campus_model():
    """Initializes MobileNetV3-Large with 6 classes and loads weights if present."""
    model = mobilenet_v3_large(weights=None)
    in_features = model.classifier[3].in_features
    model.classifier[3] = nn.Linear(in_features, len(CLASS_NAMES))

    # Look for model weights saved from Colab / local training
    weights_paths = ["best_model.pth", "model.pth", "campus_mobilenet_v3.pth"]
    loaded = False
    for p in weights_paths:
        if os.path.exists(p):
            try:
                state = torch.load(p, map_location=DEVICE)
                model.load_state_dict(state)
                print(f"[INFO] Loaded trained weights from: {p}")
                loaded = True
                break
            except Exception as e:
                print(f"[WARN] Error loading {p}: {e}")

    if not loaded:
        print("[INFO] No custom .pth found. Initializing feature extractor backbone with pretrained weights.")
        base = mobilenet_v3_large(weights=MobileNet_V3_Large_Weights.DEFAULT)
        # copy convolutional features
        model.features.load_state_dict(base.features.state_dict())

    model.to(DEVICE)
    model.eval()
    return model

model = load_campus_model()

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(".", path)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "online",
        "device": str(DEVICE),
        "classes": CLASS_NAMES
    })

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    try:
        image_bytes = file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        tensor = inference_transforms(image).unsqueeze(0).to(DEVICE)

        with torch.no_grad():
            outputs = model(tensor)
            probs = torch.softmax(outputs, dim=1)[0].cpu().numpy()

        class_probs = [
            {"class": CLASS_NAMES[i], "probability": float(probs[i])}
            for i in range(len(CLASS_NAMES))
        ]
        class_probs.sort(key=lambda x: x["probability"], reverse=True)

        top_pred = class_probs[0]

        return jsonify({
            "predicted_class": top_pred["class"],
            "confidence": top_pred["probability"],
            "top_3": class_probs[:3],
            "probabilities": class_probs
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"\n=======================================================")
    print(f"Smart Campus Scene Recognition Web Server Running!")
    print(f"Open in browser: http://127.0.0.1:{port}")
    print(f"=======================================================\n")
    app.run(host="127.0.0.1", port=port, debug=False)

