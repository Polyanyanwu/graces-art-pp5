""" Context to make the list of Artist available at the menu """

from .models import Artist, ArtGenre


def artist_list(request):

    artists = Artist.objects.all().order_by('friendly_name')
    genres = ArtGenre.objects.all().order_by('friendly_name')
    context = {
        'artists': artists,
        'genres': genres,
    }
    return context
