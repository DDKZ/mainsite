import autocomplete_light
from django.contrib.auth.models import User

class UserAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['^first_name','^last_name']
    model = User
autocomplete_light.register(User, UserAutocomplete)
