import lib.GoogleWeather as GoogleWeather
import os
import time


class WeatherReport():

    def __init__(self):
        print("Weather report started")
        self.cnt_failed = 0


    def get_weather(self, name="", location="Desselbrunn"):
        try:
            weather = GoogleWeather.GoogleWeather(location)
            actual_weather = weather.get_actual_weather()
            weather = GoogleWeather.GoogleWeather(location)
            weather_prediction = weather.get_weather_prediction()
        except Exception as e:
            print("get_weather failed - retrying - ErrorMessage: ", e)
            print("cnt fails ", self.cnt_failed)
            self.cnt_failed = self.cnt_failed + 1
            if self.cnt_failed > 10:
                cwd = os.getcwd()
                f = open(cwd + "/resources/weather/reboot_flag.txt", "w")
                f.write("True")
                f.close()
                os.system("sudo reboot now")
                time.sleep(10)
            os.system("sudo pkill chromium")
            f = open("/resources/weather/weather.log", "a")
            f.write(str(time.strftime("%d.%m.%Y")) + ", " + str(time.strftime("%H:%M:%S")) + ", " + "get_weather failed - retrying - ErrorMessage: " + str(e) + "\n")
            f.close()
            time.sleep(5)
            self.get_weather()        

        loc = actual_weather["location"]
        day_time = actual_weather["day_time"]
        weather = actual_weather["weather"]
        temp = actual_weather["temp"]
        rain = actual_weather["rain"]
        hm = actual_weather["humidity"]
        ws = actual_weather["wind_strength"]
        wi = actual_weather["weather_icon"]
        src = weather_prediction["source"]

        if name == "":
            text = "Servus, \ndein Wetterbot meldet sich mit dem derzeitigen Wetter in "\
                +loc+". Es ist "+day_time+", derzeit haben wir folgendes Wetter: "\
                +weather+". Die Außentemperatur beträgt "+temp+", die Luftfeuchtigkeit beträgt "\
                +hm+" und die Regenwahrscheinlichkeit beträgt "+rain+". Es weht ein Wind mit "+ws+"."+wi\
                +"Und hier noch das Wetter für die kommenden Tage:\n"+src+"Dein Wetterbot wünscht dir noch einen schönen Tag."
        else:
            text = "Servus " + name + ", \ndein Wetterbot meldet sich, wie angefragt, mit dem derzeitigen Wetter in "\
                +loc+". Es ist "+day_time+", derzeit haben wir folgendes Wetter: "\
                +weather+". Die Außentemperatur beträgt "+temp+", die Luftfeuchtigkeit beträgt "\
                +hm+" und die Regenwahrscheinlichkeit beträgt "+rain+". Es weht ein Wind mit "+ws+"."+wi\
                +"\nDein Wetterbot wünscht dir noch einen schönen Tag."
        cwd = os.getcwd()
        f = open(cwd + "/resources/weather/weather_report.txt", "w+")
        f.write(text)
        f.close()

        print("Weather report DONE")
        return text
        

    def get_weather_prediction(self, name=""):
        try:
            weather = GoogleWeather.Weather("Desselbrunn")
            weather_prediction = weather.get_weather_prediction()
        except Exception as e:
            print("get_weather_prediction failed - retrying - ErrorMessage: ", e)
            self.cnt_failed = self.cnt_failed + 1
            if self.cnt_failed > 10:
                cwd = os.getcwd()
                f = open(cwd + "/resources/weather/reboot_flag.txt", "w")
                f.write("True")
                f.close()
            #-->os.system("sudo reboot now")
                time.sleep(10)
        #-->os.system("sudo pkill chromium")
            cwd = os.getcwd()
            f = open("/resources/weather/weather.log", "a")
            f.write(str(time.strftime("%d.%m.%Y")) + ", " + str(time.strftime("%H:%M:%S")) + ", " + "get_weather_prediction failed - retrying - ErrorMessage: " + str(e) + "\n")
            f.close()
            time.sleep(5)
            self.get_weather_prediction()        

        loc = weather_prediction["location"]
        day_time = weather_prediction["day_time"]
        weather = weather_prediction["weather"]
        temp = weather_prediction["temp"]
        rain = weather_prediction["rain"]
        hm = weather_prediction["humidity"]
        ws = weather_prediction["wind_strength"]
        wi = weather_prediction["weather_icon"]
        src = weather_prediction["source"]

        if name == "":
            text = "Servus, \ndein Wetterbot meldet sich mit dem derzeitigen Wetter in "\
                +loc+". Es ist "+day_time+", derzeit haben wir folgendes Wetter: "\
                +weather+". Die Außentemperatur beträgt "+temp+", die Luftfeuchtigkeit beträgt "\
                +hm+" und die Regenwahrscheinlichkeit beträgt "+rain+". Es weht ein Wind mit "+ws+". "+wi\
                +"\nDein Wetterbot wünscht dir noch einen schönen Tag."
        else:
            text = "Servus " + name + ", \ndein Wetterbot meldet sich, wie angefragt, mit dem derzeitigen Wetter in "\
                +loc+". Es ist "+day_time+", derzeit haben wir folgendes Wetter: "\
                +weather+". Die Außentemperatur beträgt "+temp+", die Luftfeuchtigkeit beträgt "\
                +hm+" und die Regenwahrscheinlichkeit beträgt "+rain+". Es weht ein Wind mit "+ws+". "+wi+\
                +"\nDein Wetterbot wünscht dir noch einen schönen Tag."

        cwd = os.getcwd()
        f = open(cwd + "/resources/weather/weather_report.txt", "w+")
        f.write(text)
        f.close()

        print("Weather report DONE")
        return text



if __name__ == "__main__":
    a = WeatherReport()
    a.get_weather()
