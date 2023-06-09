from rest_framework import serializers
import six
from rest_framework.fields import ChoiceField


class ChoiceDisplayField(ChoiceField):
    def __init__(self, *args, **kwargs):
        super(ChoiceDisplayField, self).__init__(*args, **kwargs)
        self.choice_strings_to_display = {
            six.text_type(key): value for key, value in self.choices.items()
        }

    def to_representation(self, value):
        if value in ('', None):
            return value
        return {
            'value': self.choice_strings_to_values.get(six.text_type(value),
                                                       value),
            'label': self.choice_strings_to_display.get(six.text_type(value),
                                                        value),
        }


class DefaultModelSerializer(serializers.ModelSerializer):
    serializer_choice_field = ChoiceDisplayField
