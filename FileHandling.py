import csv
import os
from PyQt5.QtCore import QTimer

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #CSV auto-refresh timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_from_csv)
        self.timer.start(2000)  # refresh every 2 seconds
        #path to CSV
        self.csv_path = "telemetry.csv"

    def update_from_csv(self):
        """Reads the latest telemetry row and updates the GUI."""
        if not os.path.exists(self.csv_path):
            print("CSV file not found yet.")
            return
        
        try:
            with open(self.csv_path, "r") as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                if not rows:
                    return
                latest = rows[-1]
        except Exception as e:
            print(f"Error reading CSV: {e}")
            return
        #Replace these with your actual widget names
        try:
            self.label_altitude.setText(latest.get("ALTITUDE", "N/A"))
            self.label_pressure.setText(latest.get("PRESSURE", "N/A"))
            self.label_temp.setText(latest.get("TEMP_AB", "N/A"))
            self.label_voltage.setText(latest.get("VOLTAGE", "N/A"))
            self.label_current.setText(latest.get("CURRENT", "N/A"))
            self.label_state.setText(latest.get("SOFTWARE_STATE", "N/A"))
            self.label_gnss.setText(
                f"{latest.get('GNSS_LATITUDE', 'N/A')}, {latest.get('GNSS_LONGITUDE', 'N/A')}"
            )
        except Exception as e:
            print(f"Error updating GUI: {e}")
