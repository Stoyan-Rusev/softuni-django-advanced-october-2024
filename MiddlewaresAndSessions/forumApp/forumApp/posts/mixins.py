from datetime import time

from django import forms
from django.http import HttpResponse
from django.utils.timezone import localtime


class DisabledFields(forms.Form):
    disabled_fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if self.disabled_fields[0] == '__all__' or field_name in self.disabled_fields:
                field.disabled = True


class RestrictedTimeMixin:
    start_time = time(9, 0)
    end_time = time(17, 0)
    message = 'Access restricted! Try again later!'

    def dispatch(self, request, *args, **kwargs):
        current_time = localtime().time()

        if not (self.start_time <= current_time <= self.end_time):
            return HttpResponse(self.message)

        return super().dispatch(request, *args, **kwargs)
