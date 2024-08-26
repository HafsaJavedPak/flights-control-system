from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flight, Airport, Passenger

# index view
def index(request):
    return render(request, 'flights/index.html', {
        "flights": Flight.objects.all()
    })


# gives information about a flight and list of passengers
def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    passengers= flight.passengers.all()
    non_passengers = Passenger.objects.exclude(flights=flight).all()
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers":passengers,
        "non_passengers": non_passengers,
    })

# booking a flight
def book(request, flight_id):
    
    # for a POST r request, add a new flight
    if request.method == "POST":

        # accessing the flight
        flight = Flight.objects.get(pk=flight_id)

        # finding the passenger id if from the submitted form data
        passenger_id = int(request.POST["passenger"])

        # finding the passenger based on id
        passenger = Passenger.objects.get(pk=passenger_id)

        # adding the passenger to the flight
        passenger.flights.add(flight)

        # redirect user to flight page
        return HttpResponseRedirect(reverse("flights:flight", args=(flight_id,)))

