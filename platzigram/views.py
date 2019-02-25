#utilities
from datetime import datetime

from django.http import HttpResponse

from django.http import JsonResponse

from django.core import serializers

# Hello World
def hello_world(request):
  now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
  return HttpResponse('Hi , server time is {now}'.format(now=str(now)))


#Responds in json argument numbers sent in the url example: mysite/?numbers=201
def hi(request):
  # Hi
  # print(request)
  
  #DEBUGGER
  # import pdb; pdb.set_trace() #debugger
  # c + enter en consola para cerrarlo 

  values = request.GET['numbers']

  values = values.split(',')
  #Map with lambda
  # values = list(map(lambda x: int(x), values))
  
  #map with function
  values = list(map(toInt, values))
  
  values.sort()

  # creating dictionary from the array
  values = {values[i]: values[i] for i in range(0, len(values), 1)}

  # import pdb; pdb.set_trace() #debugger
  
  # import pdb; pdb.set_trace() #debugger

  return JsonResponse(values,safe=True)

def toInt(x):
  return int(x)


def say_age(request , name , age):
  #retuns name and age 
  message = "Hello I am {name} my age is {age}"

  # return JsonResponse(data, safe=True)
  return HttpResponse(message.format(name = name,age = age))

  
