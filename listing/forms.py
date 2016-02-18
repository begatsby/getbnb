from django import forms

from .models import Property


class PropertyAdminForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Property
        fields = ['owner', 'name', 'description', 'property_type', 'room_type',
            'accomodation_count', 'bedroom_count', 'bed_count',
            'bathroom_count']
