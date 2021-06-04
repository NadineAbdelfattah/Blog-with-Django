from django import forms
from .models import Post, Category

# choices = [('coding', 'coding'), ('sports', 'sports'), ('entertainment', 'entertainment'), ]
choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body')
        widgets = {
            'title': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the post title'}),
            'title_tag': forms.TimeInput(
                attrs={'class': 'form-control', 'placeholder': 'Please enter the post tag title'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter the post body'}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')
        widgets = {
            'title': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the post title'}),
            'title_tag': forms.TimeInput(
                attrs={'class': 'form-control', 'placeholder': 'Please enter the post tag title'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter the post body'}),

        }
