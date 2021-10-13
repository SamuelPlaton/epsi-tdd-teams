from django.http import HttpResponse
from .models import Generator

def index(request):
    generator = Generator('C:/Users/plato/OneDrive/Bureau/Etudes/EPSI//analyse-cdc//tdd-project/django_interface/project/models/data.csv')
    players = generator.generate_players()
    formatted_players = ["<li>{}</li>".format(player.name) for player in players]
    message = """<ul>{}</ul>""".format("\n".join(formatted_players))
    return HttpResponse(message)