import sys
import os
import cv2


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from VehicleDetectionTracker.VehicleDetectionTracker import VehicleDetectionTracker


video_path = "videos/t.mp4" 

if not os.path.exists(video_path):
    raise FileNotFoundError(f" Video file not found: {video_path}")

print(f" Video found: {video_path}")
vehicle_detection = VehicleDetectionTracker()
frame_counter = 0

# === Callback to show detection result ===
def result_callback(result):
    global frame_counter
    frame_counter += 1
    print(f"\n Frame #{frame_counter}")
    print("Vehicles Detected:", result["number_of_vehicles_detected"])
    for vehicle in result['detected_vehicles']:
        kph = vehicle["speed_info"].get("kph")
        if kph is not None:
            kph_str = f"{kph:.1f} kph"
        else:
            kph_str = "N/A"

        print(f"- ID: {vehicle['vehicle_id']} | Type: {vehicle['vehicle_type']} | Speed: {kph_str}")

#Run the detection 
print(" Starting detection...")
vehicle_detection.process_video(video_path, result_callback=result_callback)
print(" Finished processing video.")
