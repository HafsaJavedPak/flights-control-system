from django.db import models


# defining a airport
class Airport(models.Model):
    code = models.CharField( max_length=4)
    city = models.CharField(max_length=64)

    def __str__(self) -> str:
        # return super().__str__()
        return f"{self.city} ({self.code})"

# defining a flight (which has 2 airports)
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    duration = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.id} : {self.origin} to {self.destination} of {self.duration} hours"

# defining a paasenger model
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name='passengers')

    def __str__(self) -> str:
        return f"{self.first} {self.last}"