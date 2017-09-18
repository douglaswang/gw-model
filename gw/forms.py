from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class GwModelForm(forms.Form):
    n = forms.IntegerField(
        label="Length of timeseries (n)",
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
    hini = forms.FloatField(
        label="Initial groundwater level (hini)",
        validators=[
            MinValueValidator(1)
        ]
    )
    rf = forms.FloatField(
        label="Recharge factor (recharge/rainfall)",
        validators=[
            MaxValueValidator(1),
            MinValueValidator(0)
        ]
    )
    sy = forms.FloatField(
        label="Specific yield",
        validators=[
            MaxValueValidator(1),
            MinValueValidator(0)
        ]
    )
    hmin = forms.FloatField(
        label="Groundwater level at which baseflow ceases",
        validators=[
            MinValueValidator(0)
        ]
    )
    pd = forms.FloatField(
        label="Parameter for controlling baseflow",
        validators=[
            MaxValueValidator(1),
            MinValueValidator(0)
        ]
    )
