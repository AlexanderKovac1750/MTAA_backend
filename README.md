This is school project for mobile app for pub. DEVELOPMENT is halted and unlikely to restart.

The backend uses python Flask and postgres database, it is relatively easy to setup. Here are the steps:
1. Create postgres database on backend server, on port 5432 with login postgres and password 123.
2. If you wish to use other database server, change the connection parameters for psycopg2 connection at the start of python script.
3. After than pip install required modules listed below.
4. Start script and set what address will server be hosted on, this is the address that needes to be configured on client app.
5. After that you can use the app on client and interact with backend via API calls.

    This assumes connected working frontend client, more about it here
   https://github.com/AlexanderKovac1750/MTAA_frontend

For setting the IP of server and debugging purposes please use console to monitor python server.
Installation process assumes working python interpeter available to normal applications on device.

list of needed module:
  pip install psycopg2
  pip install flask flask-socketio eventlet flask-cors
  
The other import use standard libraries as far as we know.
