from django import forms

CATEGORY_CHOICES = [
    ('', 'Category'),  # Non-selectable heading
    ('elementary', 'Elementary'),
    ('senior', 'Senior'),
    ('junior', 'Junior'),
    ('lightweight', 'Lightweight'),
    ('lfr', 'LFR (Modular)'),
]

class JoinForm(forms.Form):
    full_name = forms.CharField(
        max_length=100,
        label="Full Name",
        error_messages={'required': ''}  # Set empty string for required error message
    )
    age = forms.IntegerField(
        label="Age",
        error_messages={'required': ''}
    )
    city = forms.CharField(
        max_length=100,
        label="City",
        error_messages={'required': ''}
    )
    school_name = forms.CharField(
        max_length=100,
        label="School Name",
        error_messages={'required': ''}
    )
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        label="Category",
        error_messages={'required': ''}
    )
