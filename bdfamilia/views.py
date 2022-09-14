from django.shortcuts import render
from bdfamilia.models import*
from django.http import HttpResponse

# Create your views here.


def familia(request):

    familia1 = Familia(nombre = "Melina", edad = 26 , fechaNac= "1994-1-31")
    familia2 = Familia(nombre = "Nahuel", edad = 15 , fechaNac= "2007-9-12")
    familia3 = Familia(nombre = "Carlos", edad = 20 , fechaNac= "2002-3-27")
    familia1.save()
    familia2.save()
    familia3.save()

    familiares = { 

        f"Hola mi nombre es nombre es {familia1.nombre} tengo {familia1.edad} años y mi cumpleaños es el {familia1.fechaNac}     ."
        f"Hola mi nombre es nombre es {familia2.nombre}  tengo {familia2.edad} años y mi cumpleaños es el {familia2.fechaNac}       ."
        f"Hola mi nombre es nombre es {familia3.nombre} tengo {familia3.edad} años y mi cumpleaños es el {familia3.fechaNac}     ."
        
    }
    return HttpResponse(familiares )
    
    