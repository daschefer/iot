# INTRODUCCION

# Arquitectura

![Arquitectura](diagrama.drawio.svg)

## Grafana

Imagen: Utiliza Grafana versión 9.53
Puertos:  3000 puerto pro defecto de Grafana
Volúmenes:

- `grafana.ini`: Configuración de grafana
  - Usuario y contraseña
  - Path dentro del proxy
- `datasource.json`: Configura el origen de datos de InfluxDB
- `dashboard.yaml`: Configura la carpeta `/app/dashboards` dentro del contenedor como origen de datos para los tableros
- `micasa.json`: Tablero de prueba con los datos de mqtt dentro de InfluxDb

## InfluxDb

Imagen:
Puerto: 8086  puerto por defecto de InfluxDb
Volumen: se genera un volumen persistente para los datos de InfluxDb
Variables de entorno:

- `TZ`: Timezone en formato [ver](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
- `DOCKER_INFLUXDB_INIT_MODE`: Modo de InfluxDb setup para una instalación nueva upgrade cuando se actualiza de versión
- `DOCKER_INFLUXDB_INIT_USERNAME`: Nombre de usuario administrador de InfluxDb
- `DOCKER_INFLUXDB_INIT_PASSWORD`: Contraseña del usuario administrador
- `DOCKER_INFLUXDB_INIT_ORG`: Organización por defecto
- `DOCKER_INFLUXDB_INIT_BUCKET`: bucket/ tabla creador por defecto
- `DOCKER_INFLUXDB_INIT_ADMIN_TOKEN`: Token para conectarse a la API
- `DOCKER_INFLUXDB_INIT_RETENTION`: Días de retención por defecto.

## MQTT

Imagen: Imagen estable de mosquitto 5.0

Puertos:

- 1883: puerto TCP protocolo mqtt
- 9001: http websocket

Volúmenes:

- `mosquitto.conf`: documentacion de mosquitto [ver](https://mosquitto.org/man/mosquitto-conf-5.html)

## Publisher

Contiene un script de Python que publica valores en mqtt. Esta todo harcodeado no es un buen ejemplo productivo.

## Telegraf

Volúmenes:

- `telegraf.conf`: documentación de Telegraf [ver](https://docs.influxdata.com/telegraf/v1.26/configuration/#generate-a-configuration-file)

## certgen

Imagen: Instancia de `script-runner` que ejecuta el script `certs.sh`
Volumenes:

- `certs`: mapea el volumen compartido con Nginx donde se generaran los certificados
- `certs.sh`: script almacenado en `/docker-entrypoint.d/certs.sh` que genera los certificados

## nginx

Proxy reverso
Ports:

- 80: puerto por defecto http para redirección
- 443: puerto https por defecto

Volúmenes:

- `certs`: compartido con cergen y mapeado dentro de `/etc/ssl/private/` como solo lectura
- `nginx.conf`:  COnfiguracion nginx [ver](https://www.nginx.com/resources/wiki/start/topics/examples/full/)

# Herramientas

- [MarkText](https://github.com/marktext/marktext#windows)
- [Draw.io VSCode Plug-In](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio)


