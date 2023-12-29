from django import forms

from main.models import Student, Subject


class StyleFormMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class StudentForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'
        fields = ('firstname', 'lastname', 'avatar', 'email',)
        # exclude = ('is_active',)

    def clean_email(self):
        cleaned_data = self.cleaned_data['email']
        if 'test.test' not in cleaned_data:
            raise forms.ValidationError('not valid email. should contain test.test')
        return cleaned_data


class SubjectForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

