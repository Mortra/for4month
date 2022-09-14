from django import forms
from . import models,parser
from .models import Anime


class ParserForm(forms.Form):
    MEDIA_CHOICE = (
        ("Anime", "Anime"),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICE)

    class Meta:
        fields = [
            'media_type'
        ]

    def parser_data(self):
        if self.data['media_type'] == 'Anime':
            animes_parser = parser.parser_ing()
            for data in animes_parser:
                models.Anime.objects.create(**data)


class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ['link', 'title', 'year', 'city', 'ganre']
