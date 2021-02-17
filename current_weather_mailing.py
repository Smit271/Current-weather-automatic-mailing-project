##--> Importing Libraries
from email import message                     ##--> From Email Module importing message class
import smtplib as s                           ##--> smtplib Module as SMTP connection
from openweather_API import weather           ##--> self-Made Module for extracting weather details

def sending():                                ##--> Method to send mails to subscribed users
    ob = s.SMTP("smtp.gmail.com", 587)
    ob.starttls()
    ob.login("your-email-address@gmail.com", "password")
    subject = "Today's Weather for you sir"
    body    = "City : {}\nWeather Type : {}\nTemperature(C) : {}\nFeels Like : {}\nHumidity : {}\nWindSpeed : {} Km/h\n".format(city, weather_type, temp_c, feels_like, humidity, wind_speed)
    message = "Subject:{}\n\n{}".format(subject, body)
    listofAddress = [list of email addresses that tou want to send mail]  ##--> Subscribed User
    ob.sendmail("your-email-address@gmail.com", listofAddress, message)

    print("Successfull sent")                  ##--> Getting Acknowledge in Terminal for successful sent
    ob.quit()
city, weather_type, temp_c, feels_like, humidity, wind_speed = weather()
sending()                                      ##--> Calling method of sending mails
