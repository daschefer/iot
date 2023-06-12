# INTRODUCCION

# Arquitectura
![Arquitectura](diagrama.drawio.svg)

## Grafana
Imagen: Utiliza Grafana version 9.53
Puertos:  3000 puerto pro defecto de Grafana
Volumenes:
- `grafana.ini`: COnfiguracion de grafana
  - Usuario y contraseña
  - Path dentro del proxy
- `datasource.json`: COnfigura el origen de datos de InfluxDB
- `dashboard.yaml`: Configura la carpeta `/app/dashboards` dentro del contenedor como origen de datos para los tableros
- `micasa.json`: Tablero de prueba con los datos de mqtt dentrode infludb
## influxdb
Imagen:
Puerto: 8086  puerto por defecto de influxdb
Volumen: se genera un volumen persitente para los datos de influxdb
Variables de entorno:
- `TZ`: Timezone en formato [ver](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
- `DOCKER_INFLUXDB_INIT_MODE`: Modo de influxdb setup para una instalacion nueva upgrade cuando se actualiza la version de Influx
- `DOCKER_INFLUXDB_INIT_USERNAME`: Nombre de usuario administrador de influxdb
- `DOCKER_INFLUXDB_INIT_PASSWORD`: Contraseña del usuario administrador
- `DOCKER_INFLUXDB_INIT_ORG`: Organizacion por defecto
- `DOCKER_INFLUXDB_INIT_BUCKET`: bucket/ tabla creador por defecto
- `DOCKER_INFLUXDB_INIT_ADMIN_TOKEN`: Token para conectarse a la API
- `DOCKER_INFLUXDB_INIT_RETENTION`: Dias de retencion por defecto.

## MQTT
Imagen:
Puertos:
- 1883: puerto TCP protocolo mqtt
- 9001: http websocket
Volumenes:
- `mosquitto.conf`: documentacion de mosquitto [ver](https://mosquitto.org/man/mosquitto-conf-5.html)

## Publisher
Contiene un script de python que publica valores en mqtt. Esta todo harcodeado no es un buen ejemplo productivo.

## Telegraf
Volumenes:
- `telegraf.conf`: documentacion de telegraf [ver](https://docs.influxdata.com/telegraf/v1.26/configuration/#generate-a-configuration-file)

## certgen
Imagen: Instancia de `script-runner` que ejecuta el script `certs.sh`
Volumenes:
- `certs`: mapea el volumen compartido con nginx donde se genrararn los certificados
- `certs.sh`: script almacenado en `/docker-entrypoint.d/certs.sh` que genera los certificados

## nginx
Proxy reverso
Ports:
- 80: puerto por defecto http para redireccion
- 443: puerto https por defecto
Volumenes:
- `certs`: compartido con cergen y mapeado dentro de `/etc/ssl/private/` como solo lectura
- `nginx.conf`:  COnfiguracion nginx [ver](https://www.nginx.com/resources/wiki/start/topics/examples/full/)


# Herramientas
- [MarkText](https://github.com/marktext/marktext#windows)
- [Draw.io VSCode Plug-In](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio)

# TODO
grafana
- Fijar version
- POner timezone
mqtt
- corregir puerto