import sys
from datetime import datetime
from zoneinfo import ZoneInfo, available_timezones
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("World Time Synchronizer Pro 🌐")
window.resize(450, 200)

layout = QVBoxLayout()

title_label = QLabel("GLOBAL TIME ZONE NETWORK")
title_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
title_label.setStyleSheet("color: #2c3e50; letter-spacing: 1px;")
title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
layout.addWidget(title_label)

combo = QComboBox()
combo.setMinimumHeight(35)
combo.setFont(QFont("Arial", 10))
all_zones = sorted(list(available_timezones()))
combo.addItems(all_zones)

default_zone = "Europe/Samara"
if default_zone in all_zones:
    combo.setCurrentText(default_zone)

label = QLabel("")
label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
label.setStyleSheet("color: #27ae60; margin-top: 15px; padding: 10px; background-color: #ffffff; border-radius: 8px;")
label.setAlignment(Qt.AlignmentFlag.AlignCenter)

layout.addWidget(QLabel("<b>Select Region / City:</b>"))
layout.addWidget(combo)
layout.addWidget(label)
window.setLayout(layout)


def update_time():
    selected_zone = combo.currentText()
    try:
        now = datetime.now(ZoneInfo(selected_zone))
        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%B %d, %Y")

        label.setText(
            f"🕒 {current_time}<br>"
            f"<span style='font-size: 12px; color: #7f8c8d;'>📅 {current_date}</span>"
        )
    except Exception:
        label.setText("<span style='color: red;'>Zone Load Error</span>")


timer = QTimer()
timer.timeout.connect(update_time)
timer.start(1000)

combo.currentTextChanged.connect(update_time)
update_time()

window.show()
sys.exit(app.exec())
