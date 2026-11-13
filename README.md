# Smart Campus Scene Recognition - Web Application & Frontend

Modern web frontend and PyTorch inference backend for the **Smart Campus Scene Recognition** capstone project (MobileNetV3-Large).

---

## 🚀 Quick Start Options

### Option 1: Instant Client-Side Demo (No Python Required)
1. Double-click or open `index.html` directly in Google Chrome, Microsoft Edge, or any modern web browser.
2. Drag and drop any campus photo or click one of the preset buttons (`Classroom`, `Library`, `Laboratory`, `Common_Canteen`, `Corridor`, `Office`) to test the interface immediately!

---

### Option 2: Full PyTorch Backend Inference
1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **(Optional) Add your trained weights:**
   If you exported your weights (`best_model.pth`) from the Google Colab notebook, place `best_model.pth` in this folder. If not present, the app initializes the MobileNetV3 feature extractor automatically.

3. **Start the web server:**
   ```bash
   python app.py
   ```

4. **Open in your browser:**
   ```
   http://127.0.0.1:5000
   ```

---

## 🎯 Target Campus Categories
- **Classroom**: Lecture halls, student seating, podiums, whiteboards.
- **Common_Canteen**: Campus cafeterias, dining tables, food courts.
- **Corridor**: Hallways, walkways, passages.
- **Laboratory**: Research equipment, computers, experiment benches.
- **Library**: Bookstacks, reading cubicles, study halls.
- **Office**: Faculty cabins, administration offices, consultation desks.

---

## 📁 File Structure
- `index.html`: Responsive UI dashboard with drag-and-drop file upload, preview, and results display.
- `style.css`: Clean, dark glassmorphism styling and responsive layout.
- `app.js`: Interactive frontend logic, probability visualizations, and API communication.
- `app.py`: Flask application with `/predict` endpoint executing MobileNetV3-Large PyTorch inference.
- `requirements.txt`: Python package requirements.

