""" Context to make the list of Artist available at the menu """

from .models import Artist


def artist_list(request):

    artists = Artist.objects.all().order_by('friendly_name')

    context = {
        'artists': artists,
    }
    return context
