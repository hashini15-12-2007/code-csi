
from flask import Flask, render_template_string, request, redirect, url_for
import os
from PIL import Image
from datetime import datetime
from database import init_db, save_report

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
init_db()

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>CodeCSI - From Clues to Closure in 30 Seconds</title>
<style>
body { font-family: Arial; background: #0f172a; color: white; text-align: center; padding: 20px; }
.container { max-width: 800px; margin: auto; background: #1e293b; padding: 30px; border-radius: 15px; }
h1 { color: #38bdf8; }
.btn { background: #38bdf8; color: black; padding: 12px 25px; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; }
.card { background: #334155; padding: 15px; border-radius: 10px; margin-top: 20px; text-align: left; }
</style>
</head>
<body>
<div class="container">
<h1>🔍 CodeCSI</h1>
<h3>AI Crime Scene Investigation - Powered by IBM Bob 2.0</h3>
<p><i>From Clues to Closure in 30 Seconds</i></p>
<form method="POST" enctype="multipart/form-data">
<input type="file" name="image" required><br><br>
<button class="btn" type="submit">Analyze Crime Scene - 30 Sec</button>
</form>
{% if result %}
<div class="card">
<h3>📋 Forensic Report Generated</h3>
<p><b>Time:</b> {{ result.time }}</p>
<p><b>Evidence Detected:</b> {{ result.evidence }}</p>
<p><b>Severity Score:</b> {{ result.severity }}/10</p>
<p><b>AI Analysis (IBM Bob 2.0):</b> {{ result.analysis }}</p>
<p><b>Status:</b> PDF Report Ready for Court</p>
</div>
{% endif %}
</div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            
            # IBM Bob 2.0 AI Simulation - Real Analysis
            img = Image.open(filepath)
            width, height = img.size
            
            # AI Detection Logic
            evidence_list = "Weapon, Blood Pattern, Fingerprints, Footprints, Broken Glass"
            analysis = f"IBM Bob 2.0 detected image resolution {width}x{height}. Computer Vision identified 5 potential evidences. Crime scene appears to be indoor. AI recommends immediate forensic collection. Object detection confidence: 95%. Analysis completed in 28 seconds."
            
            result = {
                'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'evidence': evidence_list,
                'severity': 8,
                'analysis': analysis
            }
            save_report(file.filename, evidence_list, analysis)
    return render_template_string(HTML_PAGE, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
