from plyer import notification
import requests

def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,
        timeout=15
    )

def getData(url):
    r=requests.get(url)
    return r.text

if __name__ == '__main__':
    notifyMe("Harry", "Lets stop the spread of this virus together")
    myHtmlData=getData("https://www.mohfw.in/")

    print(myHtmlData)
