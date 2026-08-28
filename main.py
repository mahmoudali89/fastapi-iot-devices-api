from fastapi import FastAPI, HTTPException
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

@app.get("/devices/{device_id}")
def get_device(device_id: int):
    for device in devices:
        if device["id"] == device_id:
            return device
    raise HTTPException(status_code=404, detail="Device not found")

@app.put("/devices/{device_id}")
def update_device(device_id: int, updated: Device):
    for device in devices:
        if device["id"] == device_id:
            device["name"] = updated.name
            device["device_type"] = updated.device_type
            return {"message": "Device updated", "device": device}
    raise HTTPException(status_code=404, detail="Device not found")

@app.delete("/devices/{device_id}")
def delete_device(device_id: int):
    for device in devices:
        if device["id"] == device_id:
            devices.remove(device)
            return {"message": "Device deleted"}
    raise HTTPException(status_code=404, detail="Device not found")