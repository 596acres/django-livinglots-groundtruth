from django import forms
from django.utils.translation import ugettext_lazy as _


class GroundtruthRecordFormMixin(forms.ModelForm):

    def clean(self):
        cleaned_data = super(GroundtruthRecordFormMixin, self).clean()
        contact_email = cleaned_data.get('contact_email', None)
        contact_phone = cleaned_data.get('contact_phone', None)
        if not (contact_email or contact_phone):
            raise forms.ValidationError(_('Please enter an email address or '
                                          'phone number'))
        return cleaned_data
