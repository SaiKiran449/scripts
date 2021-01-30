from paho.mqtt import client as mqtt_client


# MQTT connection details
broker = 'eu1.cloud.thethings.industries'
port = 1883
topic = "#"
client_id = "test-client"    ##The client id with which it connects to the MQTT Broker. It could be any unique value.
username = "application@tenant"
password = "......................................."

# LoRa Cloud geo location connection details
geo_location_request_url = "https://gls.loracloud.com/api/v3/solve/singleframe"
ocp_apim_subscription_key = "..............."

# Extract the gateway data and the frame data required to send the request to Geo Location API
def extract_gateway_and_frame_data(gateway_details:list):
    gateway_data = []
    frame_data = []
    for gateway in gateway_details:
        current_gateway_data = {"gatewayId":gateway["gateway_ids"]["eui"],"latitude":gateway["location"]["latitude"],
                                "longitude":gateway["location"]["longitude"],"altitude":gateway["location"]["altitude"]}
        current_frame_data = [gateway["gateway_ids"]["eui"],None,gateway["timestamp"],gateway["rssi"],gateway["snr"]]
        gateway_data.append(current_gateway_data)
        frame_data.append(current_frame_data)
    return gateway_data,frame_data

# prepare the request data required to send the request to Geo Location API
def get_request_data(gateway_details:list):

    gateway_data,frame_data = extract_gateway_and_frame_data(gateway_details=gateway_details)
    request_data = {
        "gateways":gateway_data,
        "frame":frame_data
    }
    return request_data

# Make an API call to the LoRa cloud Geo location Single Frame API
def send_data_to_geolocation_api(request_data:dict):
    import requests
    import json
    from requests.structures import CaseInsensitiveDict

    url = geo_location_request_url
    headers = CaseInsensitiveDict()
    headers["Ocp-Apim-Subscription-Key"] = ocp_apim_subscription_key
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "application/json"

    data = json.dumps(request_data)

    resp = requests.post(url, headers=headers, data=data)

    response_code = resp.status_code
    response_content = json.loads(resp.content)
    return response_code,response_content

# This method is used to connect to the MQTT broker
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username=username,password=password)
    client.on_connect = on_connect
    client.connect(host=broker, port=port)
    return client

# This method is used to subscribe to the topics and make a request to Geo Location API if the MQTT topic is uplink topic
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        import json
        # Filters out the MQTT uplink topics of the devices of an application
        is_uplink_topic_message = msg.topic[-2:] == "up"

        if is_uplink_topic_message:
            uplink_message = json.loads(msg.payload.decode())
            device_id = uplink_message["end_device_ids"]["device_id"]
            gateway_details = uplink_message["uplink_message"]["rx_metadata"]
            request_data = get_request_data(gateway_details=gateway_details)
            print("Request data to LoRa Cloud Geo Location for device-id {} is :\n".format(device_id),request_data)
            response_code, response_content = send_data_to_geolocation_api(request_data=request_data)
            print("Response from LoRa Cloud Geo Location for device-id {} is :\n".format(device_id),response_code,response_content)

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
