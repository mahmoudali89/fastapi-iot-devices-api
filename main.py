from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Device(BaseModel):
    name: str
    device_type: str

devices = [
    {"id": 1, "name": "temperature-sensor", "device_type": "sensor"},
    {"id": 2, "name": "smart-light", "device_type": "actuator"}
]

@app.get("/devices")
def get_devices():
    return {"devices": devices}

@app.post("/devices", status_code=201)
def add_device(device: Device):
    new_id = len(devices) + 1
    new_device = {"id": new_id, "name": device.name, "device_type": device.device_type}
    devices.append(new_device)
    return {"message": "Device added", "device": new_device}