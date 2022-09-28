from django import forms

class ToDoListForm(forms.Form):
    title = forms.CharField(label="Title", max_length=50)
    description = forms.CharField(label ="Deskripsi", max_length=250)