import requests    #allows you to send HTTP requests 
from datetime import datetime
 
city=input("\nENTER THE NAME OF CITY: ") 

#API RELATED 
apikey="9009da12d9d675cff47747fd60b73697"
api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+apikey
apireq=requests.get(api)  # GET is request to the specified url
api_data=apireq.json()  # json (JavaScript object notation) store the data of existing url

#MAIN
if api_data["cod"] == '404':  
     print("\nINVALID CITY :(\n")
else:
    temp=int(((api_data['main']['temp'])))
    description=api_data['weather'][0]['description']
    hmdt=api_data['main']['humidity']
    wind_speed=api_data['wind']['speed']
    date_time=datetime.now().strftime("%d %b %Y | %I:%M %p")


    print("\n----------------------------------------------------------------")
    print("   WEATHER INFORMATION FOR - "+city.upper()+" ||",date_time)
    print("----------------------------------------------------------------\n")
    print("        TEMPERATURE         : ",temp-273,"°C")
    print("        DESCRIPTION         : ",description)
    print("        HUMIDITY            : ",hmdt,"%")
    print("        WIND SPEED          : ",wind_speed,"KM/H\n")

