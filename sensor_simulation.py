import random
import time
import requests
import os
from datetime import datetime

# Configuration
ORION_URL = os.getenv("ORION_URL")
FLASK_ALERT_URL = os.getenv("FLASK_ALERT_URL")

TEMP_THRESHOLD_LOW = 15
TEMP_THRESHOLD_HIGH = 35
HUMIDITY_THRESHOLD_LOW = 40
HUMIDITY_THRESHOLD_HIGH = 80


def generate_temperature():
    return round(random.uniform(10, 40), 2)


def generate_humidity():
    return round(random.uniform(30, 90), 2)


def send_to_orion(temp_sensors, hum_sensors):
    payload = {"actionType": "append", "entities": []}

    for sensor in temp_sensors + hum_sensors:
        entity = {
            "id": sensor["id"],
            "type": sensor["type"],
            sensor["value_key"]: {
                "value": sensor["value"],
                "type": "Number",
                "metadata": {
                    "dateCreated": {
                        "type": "DateTime",
                        "value": datetime.utcnow().isoformat() + "Z",
                    }
                },
            },
        }
        payload["entities"].append(entity)

    try:
        response = requests.post(ORION_URL, json=payload)
        print(f"[Orion] Sent data. Status code: {response.status_code}")
    except Exception as e:
        print(f"[Orion] Error sending data: {e}")


def send_alert(sensor_id, sensor_type, value, threshold):
    alert_data = {
        "sensorId": sensor_id,
        "type": sensor_type,
        "value": value,
        "threshold": threshold,
    }
    try:
        response = requests.post(FLASK_ALERT_URL, json=alert_data)
        print(f"[Flask] Alert sent: {alert_data}. Status code: {response.status_code}")
    except Exception as e:
        print(f"[Flask] Error sending alert: {e}")


def main():
    temp_sensors = [
        {
            "id": f"TempSensor{i}",
            "type": "TemperatureSensor",
            "value_key": "temperature",
        }
        for i in range(1, 3)
    ]
    humidity_sensors = [
        {"id": f"HumiditySensor{i}", "type": "HumiditySensor", "value_key": "humidity"}
        for i in range(1, 3)
    ]

    while True:
        temp_values = [generate_temperature() for _ in temp_sensors]
        humidity_values = [generate_humidity() for _ in humidity_sensors]

        temp_entities = [
            {**sensor, "value": temp_values[i]} for i, sensor in enumerate(temp_sensors)
        ]
        humidity_entities = [
            {**sensor, "value": humidity_values[i]}
            for i, sensor in enumerate(humidity_sensors)
        ]

        send_to_orion(temp_entities, humidity_entities)

        for ent in temp_entities + humidity_entities:
            if ent["type"] == "TemperatureSensor":
                if (
                    ent["value"] < TEMP_THRESHOLD_LOW
                    or ent["value"] > TEMP_THRESHOLD_HIGH
                ):
                    send_alert(
                        ent["id"],
                        ent["type"],
                        ent["value"],
                        (
                            TEMP_THRESHOLD_HIGH
                            if ent["value"] > TEMP_THRESHOLD_HIGH
                            else TEMP_THRESHOLD_LOW
                        ),
                    )
            elif ent["type"] == "HumiditySensor":
                if (
                    ent["value"] < HUMIDITY_THRESHOLD_LOW
                    or ent["value"] > HUMIDITY_THRESHOLD_HIGH
                ):
                    send_alert(
                        ent["id"],
                        ent["type"],
                        ent["value"],
                        (
                            HUMIDITY_THRESHOLD_HIGH
                            if ent["value"] > HUMIDITY_THRESHOLD_HIGH
                            else HUMIDITY_THRESHOLD_LOW
                        ),
                    )

        time.sleep(10)


if __name__ == "__main__":
    main()
