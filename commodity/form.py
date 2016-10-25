__author__ = 'yem'

from django import forms

from django.utils.safestring import mark_safe

from django.contrib.admin.widgets import AdminFileWidget

from .models import Book

class AdminImageWidget(AdminFileWidget):

    def render(self, name, value, attrs=None):

        output = []

        if value and getattr(value,"url",None):
            image_url = value.url
            file_name = str(value)
            output.append(u'<a href="%s" target="_blank"><img src="%s" /> </a>' % \
                              (image_url,image_url,file_name) )
            output.append(super(AdminFileWidget,self).render(name,value,attrs))

            return mark_safe(u''.join(output))


class ThumbnailAdminForm(forms.ModelForm):

    class Meta:
        fields = '__all__'
        widgets = { 'thumbnail' : AdminImageWidget()}

        model = Book