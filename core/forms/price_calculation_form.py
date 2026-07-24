from django import forms


class PriceCalculationForm(forms.Form):
    city_from = forms.ChoiceField(label="City From:")
    city_to = forms.ChoiceField(label="City To:")

    def __init__(self, *args, **kwargs):
        service_options = kwargs.pop("dropdown_options", [])

        super().__init__(*args, **kwargs)

        if len(service_options) >= 2:
            from_city_options = [ (str(city_idx), city) for city_idx, city in enumerate(service_options[0])]
            to_city_options = [ (str(city_idx), city) for city_idx, city in enumerate(service_options[1])]
        else:
            from_city_options = []
            to_city_options = []

        self.fields["city_from"].choices = from_city_options
        self.fields["city_to"].choices = to_city_options
