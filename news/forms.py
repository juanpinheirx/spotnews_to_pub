from django import forms
from news.models import News


class CreateCategoryForm(forms.Form):
    name = forms.CharField(max_length=200, required=True)


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"
