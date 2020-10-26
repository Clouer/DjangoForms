from django import forms
from django.forms import widgets
from django.db.models import TextChoices

from demo.models import Book


class SearchForm(forms.Form):
    email = forms.EmailField()


class SubscribeForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()


class IceCreamForm(forms.Form):
    class Tastes(TextChoices):
        BLACKBERRY = 'черничный'
        STRAWBERRY = 'землячничный'
        LICORICE = 'лакричный'

    class Toppings(TextChoices):
        CHOCOLATE = 'Шоколадная крошка'
        CARAMEL = 'Карамель'
        PARSLEY = 'Петрушка'

    class Sizes(TextChoices):
        SMALL = 'маленнький'
        MEDIUM = 'средний'
        LARGE = 'большой'

    taste = forms.ChoiceField(choices=Tastes.choices)
    topping = forms.MultipleChoiceField(choices=Toppings.choices, widget=widgets.CheckboxSelectMultiple)
    size = forms.ChoiceField(choices=Sizes.choices, widget=widgets.RadioSelect)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['surname', 'name', 'luggage_weight', 'pass_id']
