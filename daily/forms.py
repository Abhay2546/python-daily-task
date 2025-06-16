from django import forms

class TaskForm(forms.Form):
    flagship = forms.CharField(label='Flagship Project', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    task = forms.CharField(label='Task', max_length=200, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))
    duration = forms.CharField(label='Duration', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    notes = forms.CharField(label='Notes', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))
    comment = forms.CharField(label='Comment', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))
