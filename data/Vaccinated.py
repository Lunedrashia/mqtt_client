#Start with day -5
import random

#Temp Mock Data
mockMean = [36.5,36.7,36.5,36.6,36.5 / #Before know ว่า เป็น covid
            36.4,37.9,38.2,38.1,37.8,37.5 /
            37.5,37.4,37.8,37.7,37.0 /
            37.5,37.6,37.6,37.5,37.2 /
            37.0,36.9,36.7,37.2,36.3]

varient = 0.3

def generateTemp(day):
    answer = mockMean[day+5] + random.randrange(-0.5, 1)*varient
    return answer

def generateO2(Temp):
    answer = 96+ random.randrange(-7,10)*varient
    return answer

