# FastAPI IoT Devices API

A REST API for managing IoT devices, built with FastAPI.

## Features
- Add new devices
- View all devices
- (Coming soon: get/update/delete by ID)

## Tech Stack
- Python 3.x
- FastAPI
- Uvicorn

## Setup & Run

1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/mahmoudali89/fastapi-iot-devices-api.git
   cd fastapi-iot-devices-api
   \`\`\`

2. Install dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. Run the server:
   \`\`\`bash
   python -m uvicorn main:app --reload
   \`\`\`

4. Open the interactive docs:
   \`\`\`
   http://127.0.0.1:8000/docs
   \`\`\`