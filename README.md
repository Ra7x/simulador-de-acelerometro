# Simulador de acelerometro
Programa en python que se encarga de simular los valores que genera un accelerómetro y transmitirlos a través de un broker MQTT

## Suscribirse al topic
Desde nuestra CMD o desde el servidor que empleemos como broker MQTT

`mosquitto_sub -h 192.168.0.1 -t sensores/valores`

## Publicar manualmente en el topic
Si nosotros quisiéramos publicar un mensaje en el topic con el broker de manera manual

`mosquitto_pub -h 192.168.0.1 -t sensores/valores -m 'Hola mundo :D'`
