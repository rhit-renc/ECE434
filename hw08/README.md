# HW08
## MAX31820 Temperature Sensors and Logging in Sheets
To read the temperature sensors, connect the sensors to P9_14. If necessary, refer to hw07/README.md.

The hw08 directory contains the following files

credentials.json: the OAuth client secret. Used to authenticate to the authorization server and obtain an API token.

logger.py: The script that logs the sensor data to Sheets

token.json: The API token. Used to provide the API server with information and authentication.

To run the script:
1. Ensure the proper Google Python libraries are installed.
2. Execute hw08/logger.py
3. The Sheets document the script logs to can be found at https://docs.google.com/spreadsheets/d/1GSA4805MK-H0aieQ1GmOMr9Q62gqeACgWguzbKkXi1Q/edit?usp=sharing
4. To stop logging, kill the running script by pressing Ctrl + C from the terminal

Note: The script takes a while until it starts logging, so be patient.
