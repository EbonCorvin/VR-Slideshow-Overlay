import requests;
import config;

# This is a free service that show the information of your ISP
# We use the lat-long provided by this service to get the weather information from open-meteo
URL_IPINFO = "https://ipinfo.io/";
# Visit https://open-meteo.com/en/docs for more the information of vailable weather data and how you get them
URL_OPEN_METEO_FORMAT = "https://api.open-meteo.com/v1/forecast?latitude=%s&longitude=%s&current=temperature_2m,relative_humidity_2m,is_day,weather_code&timezone=auto";
URL_GEOCODING = "https://geocode.maps.co/search?q=%s"
CURRENT_WEATHER_FORMAT = "Location: %s\vTemp.: %s%s\tRH: %s%%\vWeather: %s";
REFRESH_RATE = 30;
USE_FAHRENHEIT = False;

MODULE_NAME = "LocalWeather";
MODULE_DESC = "Show your city and the local weather"
CITY_NAME = "";
PLUGIN_ENABLED = False;
config.addConfig(__name__, "CITY_NAME", "Enter the city name (City, country)\nLeave it empty to auto detect the city from your IP address", "str")
config.addConfig(__name__, "USE_FAHRENHEIT", "Use fahrenheit?", "bool")
config.addConfig(__name__, "REFRESH_RATE", "Update Frequence, in minute", "num")

class LocalWeather:
    cached_message = None;
    ranCount = 0;
    latLong = None;
    cityName = None;

    def init(self):
        global URL_OPEN_METEO_FORMAT;
        if USE_FAHRENHEIT:
            URL_OPEN_METEO_FORMAT+="&temperature_unit=fahrenheit";
        self.refreshRateSecond = REFRESH_RATE * 60;
        if len(CITY_NAME) > 0:
            latLongInfo = requests.get(URL_GEOCODING % CITY_NAME);
            latLongInfo = latLongInfo.json();
            if len(latLongInfo) > 0:
                self.latLong = (latLongInfo[0]["lat"], latLongInfo[0]["lon"]);
                self.cityName = latLongInfo[0]["display_name"];
        if self.latLong is None:
            locationInfo = requests.get(URL_IPINFO);
            locationInfo = locationInfo.json();
            latLongArr = locationInfo["loc"].split(",");
            self.latLong = (latLongArr[0], latLongArr[1])
            self.cityName = locationInfo["city"];
    
    def onUpdate(self, scriptUpTime):
        if  int(scriptUpTime/self.refreshRateSecond) >= self.ranCount:
            self.fetchWeather();
            self.ranCount+=1;
        if self.cached_message is not None:
            return self.cached_message;
        
    def fetchWeather(self):
        weatherInfo = requests.get(URL_OPEN_METEO_FORMAT % self.latLong);
        self.cached_message = self.formatMessage(weatherInfo.json());

    def formatMessage(self,cached_weather):
        city = self.cityName;
        temp = cached_weather["current"]["temperature_2m"];
        tempUnit = cached_weather["current_units"]["temperature_2m"];
        rh = cached_weather["current"]["relative_humidity_2m"];
        isDay = cached_weather["current"]["is_day"];
        weatherCode = str(cached_weather["current"]["weather_code"]);
        weather = WMO_WEATHER_CODE_LUT[weatherCode]["day" if isDay==1 else "night"]["description"];
        return CURRENT_WEATHER_FORMAT % (city,temp,tempUnit,rh,weather)
            
# https://gist.github.com/stellasphere/9490c195ed2b53c707087c8c2db4ec0c
WMO_WEATHER_CODE_LUT = {
    "0":{
        "day":{
            "description":"Sunny",
            "image":"http://openweathermap.org/img/wn/01d@2x.png"
        },
        "night":{
            "description":"Clear",
            "image":"http://openweathermap.org/img/wn/01n@2x.png"
        }
    },
    "1":{
        "day":{
            "description":"Mainly Sunny",
            "image":"http://openweathermap.org/img/wn/01d@2x.png"
        },
        "night":{
            "description":"Mainly Clear",
            "image":"http://openweathermap.org/img/wn/01n@2x.png"
        }
    },
    "2":{
        "day":{
            "description":"Partly Cloudy",
            "image":"http://openweathermap.org/img/wn/02d@2x.png"
        },
        "night":{
            "description":"Partly Cloudy",
            "image":"http://openweathermap.org/img/wn/02n@2x.png"
        }
    },
    "3":{
        "day":{
            "description":"Cloudy",
            "image":"http://openweathermap.org/img/wn/03d@2x.png"
        },
        "night":{
            "description":"Cloudy",
            "image":"http://openweathermap.org/img/wn/03n@2x.png"
        }
    },
    "45":{
        "day":{
            "description":"Foggy",
            "image":"http://openweathermap.org/img/wn/50d@2x.png"
        },
        "night":{
            "description":"Foggy",
            "image":"http://openweathermap.org/img/wn/50n@2x.png"
        }
    },
    "48":{
        "day":{
            "description":"Rime Fog",
            "image":"http://openweathermap.org/img/wn/50d@2x.png"
        },
        "night":{
            "description":"Rime Fog",
            "image":"http://openweathermap.org/img/wn/50n@2x.png"
        }
    },
    "51":{
        "day":{
            "description":"Light Drizzle",
            "image":"http://openweathermap.org/img/wn/09d@2x.png"
        },
        "night":{
            "description":"Light Drizzle",
            "image":"http://openweathermap.org/img/wn/09n@2x.png"
        }
    },
    "53":{
        "day":{
            "description":"Drizzle",
            "image":"http://openweathermap.org/img/wn/09d@2x.png"
        },
        "night":{
            "description":"Drizzle",
            "image":"http://openweathermap.org/img/wn/09n@2x.png"
        }
    },
    "55":{
        "day":{
            "description":"Heavy Drizzle",
            "image":"http://openweathermap.org/img/wn/09d@2x.png"
        },
        "night":{
            "description":"Heavy Drizzle",
            "image":"http://openweathermap.org/img/wn/09n@2x.png"
        }
    },
    "56":{
        "day":{
            "description":"Light Freezing Drizzle",
            "image":"http://openweathermap.org/img/wn/09d@2x.png"
        },
        "night":{
            "description":"Light Freezing Drizzle",
            "image":"http://openweathermap.org/img/wn/09n@2x.png"
        }
    },
    "57":{
        "day":{
            "description":"Freezing Drizzle",
            "image":"http://openweathermap.org/img/wn/09d@2x.png"
        },
        "night":{
            "description":"Freezing Drizzle",
            "image":"http://openweathermap.org/img/wn/09n@2x.png"
        }
    },
    "61":{
        "day":{
            "description":"Light Rain",
            "image":"http://openweathermap.org/img/wn/10d@2x.png"
        },
        "night":{
            "description":"Light Rain",
            "image":"http://openweathermap.org/img/wn/10n@2x.png"
        }
    },
    "63":{
        "day":{
            "description":"Rain",
            "image":"http://openweathermap.org/img/wn/10d@2x.png"
        },
        "night":{
            "description":"Rain",
            "image":"http://openweathermap.org/img/wn/10n@2x.png"
        }
    },
    "65":{
        "day":{
            "description":"Heavy Rain",
            "image":"http://openweathermap.org/img/wn/10d@2x.png"
        },
        "night":{
            "description":"Heavy Rain",
            "image":"http://openweathermap.org/img/wn/10n@2x.png"
        }
    },
    "66":{
        "day":{
            "description":"Light Freezing Rain",
            "image":"http://openweathermap.org/img/wn/10d@2x.png"
        },
        "night":{
            "description":"Light Freezing Rain",
            "image":"http://openweathermap.org/img/wn/10n@2x.png"
        }
    },
    "67":{
        "day":{
            "description":"Freezing Rain",
            "image":"http://openweathermap.org/img/wn/10d@2x.png"
        },
        "night":{
            "description":"Freezing Rain",
            "image":"http://openweathermap.org/img/wn/10n@2x.png"
        }
    },
    "71":{
        "day":{
            "description":"Light Snow",
            "image":"http://openweathermap.org/img/wn/13d@2x.png"
        },
        "night":{
            "description":"Light Snow",
            "image":"http://openweathermap.org/img/wn/13n@2x.png"
        }
    },
    "73":{
        "day":{
            "description":"Snow",
            "image":"http://openweathermap.org/img/wn/13d@2x.png"
        },
        "night":{
            "description":"Snow",
            "image":"http://openweathermap.org/img/wn/13n@2x.png"
        }
    },
    "75":{
        "day":{
            "description":"Heavy Snow",
            "image":"http://openweathermap.org/img/wn/13d@2x.png"
        },
        "night":{
            "description":"Heavy Snow",
            "image":"http://openweathermap.org/img/wn/13n@2x.png"
        }
    },
    "77":{
        "day":{
            "description":"Snow Grains",
            "image":"http://openweathermap.org/img/wn/13d@2x.png"
        },
        "night":{
            "description":"Snow Grains",
            "image":"http://openweathermap.org/img/wn/13n@2x.png"
        }
    },
    "80":{
        "day":{
            "description":"Light Showers",
            "image":"http://openweathermap.org/img/wn/09d@2x.png"
        },
        "night":{
            "description":"Light Showers",
            "image":"http://openweathermap.org/img/wn/09n@2x.png"
        }
    },
    "81":{
        "day":{
            "description":"Showers",
            "image":"http://openweathermap.org/img/wn/09d@2x.png"
        },
        "night":{
            "description":"Showers",
            "image":"http://openweathermap.org/img/wn/09n@2x.png"
        }
    },
    "82":{
        "day":{
            "description":"Heavy Showers",
            "image":"http://openweathermap.org/img/wn/09d@2x.png"
        },
        "night":{
            "description":"Heavy Showers",
            "image":"http://openweathermap.org/img/wn/09n@2x.png"
        }
    },
    "85":{
        "day":{
            "description":"Light Snow Showers",
            "image":"http://openweathermap.org/img/wn/13d@2x.png"
        },
        "night":{
            "description":"Light Snow Showers",
            "image":"http://openweathermap.org/img/wn/13n@2x.png"
        }
    },
    "86":{
        "day":{
            "description":"Snow Showers",
            "image":"http://openweathermap.org/img/wn/13d@2x.png"
        },
        "night":{
            "description":"Snow Showers",
            "image":"http://openweathermap.org/img/wn/13n@2x.png"
        }
    },
    "95":{
        "day":{
            "description":"Thunderstorm",
            "image":"http://openweathermap.org/img/wn/11d@2x.png"
        },
        "night":{
            "description":"Thunderstorm",
            "image":"http://openweathermap.org/img/wn/11n@2x.png"
        }
    },
    "96":{
        "day":{
            "description":"Light Thunderstorms With Hail",
            "image":"http://openweathermap.org/img/wn/11d@2x.png"
        },
        "night":{
            "description":"Light Thunderstorms With Hail",
            "image":"http://openweathermap.org/img/wn/11n@2x.png"
        }
    },
    "99":{
        "day":{
            "description":"Thunderstorm With Hail",
            "image":"http://openweathermap.org/img/wn/11d@2x.png"
        },
        "night":{
            "description":"Thunderstorm With Hail",
            "image":"http://openweathermap.org/img/wn/11n@2x.png"
        }
    }
}