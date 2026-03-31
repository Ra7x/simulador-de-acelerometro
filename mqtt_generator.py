import json, os, random, time
import paho.mqtt.client as mqtt
import dotenv as load_dotenv

load_dotenv.load_dotenv()
BROKER_IP = os.getenv("BROKER_IP")
BROKER_PORT = int(os.getenv("BROKER_PORT"))
TOPIC = os.getenv("TOPIC")

# Crear cliente MQTT usando WebSockets
client = mqtt.Client(transport="websockets")

def generar_datos():
    """Genera un diccionario con valores aleatorios."""
    return {
        "data1": round(random.uniform(-180, 180), 2), #Rotación en el eje X
        "data2": round(random.uniform(-180, 180), 2), #Rotación en el eje Y
        "data3": round(random.uniform(0, 9.8), 2) #Aceleración gravitatoria
    }

def main():
    # Conexión al broker
    client.connect(BROKER_IP, BROKER_PORT, 60)
    client.loop_start()

    try:
        while True:
            datos = generar_datos()
            json_datos = json.dumps(datos)

            # Publicar en MQTT
            client.publish(TOPIC, json_datos)
            print("Enviado:", json_datos)

            time.sleep(1)  # enviar cada segundo
    except KeyboardInterrupt:
        print("Finalizando...")
    finally:
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()
