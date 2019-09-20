import requests
import urllib
from urllib.request import urlopen

# test for internet connection
def is_internet():
        try:
            urlopen('https://www.google.com', timeout=3)
            return True
        except urllib.error.URLError as Error:
                    return False
                
# if internet is connected
if is_internet():
        
    def writeHTML(state,img,date,temp,mintemp,maxtemp,windspeed):
            myfile = open("Weather.html","w")
            myfile.write("<head>\n")
            myfile.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\">\n")
            myfile.write("</head>\n")
            myfile.write("<body>\n")
            myfile.write("<div class=\"pagecontainer\">\n")
            myfile.write("  <div class=\"header\">\n")
            myfile.write("      <h1>Toronto Weather</h1>\n")
            myfile.write("  </div>\n")
            myfile.write("  <div class = \"weather\">\n")
            myfile.write("      <h5>")
            myfile.write(date)
            myfile.write("</h5>\n")
            myfile.write("      <img src=\"")
            myfile.write(img)
            myfile.write("\" style=\"width:10%\">\n")
            myfile.write("      <h4>")
            myfile.write(state)
            myfile.write("</h4>\n")
            myfile.write("      <h2>")
            myfile.write(str(temp))
            myfile.write("°C</h2>\n")
            myfile.write("  </div>\n")
            myfile.write("  <div class = \"weather2\">\n")
            myfile.write("      <h4>")
            myfile.write("Low of: ")
            myfile.write(str(mintemp))
            myfile.write("°C</h4>\n")
            myfile.write("      <h4>")
            myfile.write("High of: ")
            myfile.write(str(maxtemp))
            myfile.write("°C</h4>\n")
            myfile.write("      <h4>")
            myfile.write("Windspeed: ")
            myfile.write(str(windspeed))
            myfile.write(" mph</h4>\n")
            myfile.write("  </div>\n")
            myfile.write("</div>\n")
            myfile.write("</body>\n")
            myfile.close()

    def main():
            # use API to get place info
            response = requests.get("https://www.metaweather.com/api/location/4118/")

            # if API call is correct
            if (response.status_code == 200):
                            wjson = response.json()
                            state = (wjson["consolidated_weather"][0]['weather_state_name'])
                            abbr = (wjson["consolidated_weather"][0]['weather_state_abbr'])
                            date = (wjson["consolidated_weather"][0]['applicable_date'])
                            temp = (wjson["consolidated_weather"][0]['the_temp'])
                            mintemp = (wjson["consolidated_weather"][0]['min_temp'])
                            maxtemp = (wjson["consolidated_weather"][0]['max_temp'])
                            windspeedi = (wjson["consolidated_weather"][0]['wind_speed'])

                            windspeed = round(windspeedi)

                            if(abbr == "lc"):
                                img="images/lc.svg"
                            elif(abbr == "c"):
                                img="images/c.svg"
                            elif(abbr == "h"):
                                img="images/h.svg"
                            elif(abbr == "hc"):
                                img="images/hc.svg"
                            elif(abbr == "hr"):
                                img="images/hr.svg"
                            elif(abbr == "lr"):
                                img="images/lr.svg"
                            elif(abbr == "s"):
                                img="images/s.svg"
                            elif(abbr == "sl"):
                                img="images/sl.svg"
                            elif(abbr == "sn"):
                                img="images/sn.svg"
                            elif(abbr == "t"):
                                img="images/t.svg"

                    
                                
                                    
                            writeHTML(state,img,date,temp,mintemp,maxtemp,windspeed) 
                            #print(state, temp, mintemp, maxtemp, windspeed,)
                            print("HTML file has been written. Please proceed")
    
                            
                                  
            else:
                    state = "An Error has occured"
                    writeHTML(state)
                    print("An error has occured")

    main()


else:
    print("Internet disconnected. Please connect to the internet before running the program.")
    

