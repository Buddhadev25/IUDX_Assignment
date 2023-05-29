### Building Url Dynamically 
####Variable Rules And URL Building

from flask import Flask,redirect,url_for,render_template
import requests
import mysql.connector
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('Weather.html')

@app.route('/weather/<float:lat>/<float:lon>',methods=['GET'])
def weather(lat,lon):
    api_key = "API_KEY"
    OWM_API_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather?"
    weather_params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        }
    response = requests.get(OWM_API_ENDPOINT, params=weather_params)
    weather_data=response.json()
    weather=weather_data["weather"][0]["description"]
    Location=weather_data["name"]
    store(weather,Location)
    return Location+" weather is: "+weather

def store(weather,Location):
    conn = mysql.connector.connect(user='web',password='web@123',database='webapi')
    cursor = conn.cursor()
    w=weather
    l=Location
    print(w+l)
    sql = """INSERT INTO weather(Location, Weather) VALUES (%s, %s)"""
    val=(w,l)
    try:
        # Executing the SQL command
        cursor.execute(sql,val)

        # Commit your changes in the database
        conn.commit()

    except:
        # Rolling back in case of error
        conn.rollback()

        # Closing the connection
        conn.close()
    return "Successfully saved!"

if __name__=='__main__':
    app.run(debug=True)
