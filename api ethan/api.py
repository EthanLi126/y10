import requests
import urllib
from urllib.request import urlopen

# test for internet connection
def is_internet():
        try:
            urlopen('https://www.google.com', timeout=1)
            return True
        except urllib.error.URLError as Error:
                    return False
                
# if internet is connected
if is_internet():
        
    def writeHTML(state,date,temp,mintemp,maxtemp,windspeed,humidity):
            myfile = open("Weather.html","w")
            myfile.write("<head>")
            myfile.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\">")
            myfile.write("</head>")
            myfile.write("<body>")
            myfile.write("<div class=\"pagecontainer\">")
            myfile.write(state)
            myfile.write(date)
            myfile.write("</div>")
            myfile.write("</body>")
            myfile.close()

    def main():
            # use API to get place info
            response = requests.get("https://www.metaweather.com/api/location/4118/")

            # if API call is correct
            if (response.status_code == 200):
                            wjson = response.json()
                            state = (wjson["consolidated_weather"][0]['weather_state_name'])
                            date = (wjson["consolidated_weather"][0]['applicable_date'])
                            temp = (wjson["consolidated_weather"][0]['the_temp'])
                            mintemp = (wjson["consolidated_weather"][0]['min_temp'])
                            maxtemp = (wjson["consolidated_weather"][0]['max_temp'])
                            windspeed = (wjson["consolidated_weather"][0]['wind_speed'])
                            humidity = (wjson["consolidated_weather"][0]['humidity'])
                            writeHTML(state,date,temp,mintemp,maxtemp,windspeed,humidity) 

                            
                            
                            print(state, temp, mintemp, maxtemp, windspeed, humidity)
                            
                            print("HTML file has been written. Please proceed")
    
                            
                                  
            else:
                    state = "An Error has occured"
                    writeHTML(state)
                    print("An error has occured")

    main()


else:
    print("Internet disconnected. Please connect to the internet before running the program")
    

