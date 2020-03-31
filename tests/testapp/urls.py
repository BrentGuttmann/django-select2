from django.urls import include, path
from django.views.generic import TemplateView
from django.contrib import admin

from .forms import (
    AddressChainedSelect2WidgetForm, AlbumModelSelect2WidgetForm,
    HeavySelect2MultipleWidgetForm, HeavySelect2WidgetForm,
    ModelSelect2TagWidgetForm, Select2WidgetForm
)
from .views import TemplateFormView, heavy_data_1, heavy_data_2

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name="demo-index"),
    path('admin/', admin.site.urls),

    path('select2_widget',
         TemplateFormView.as_view(form_class=Select2WidgetForm), name='select2_widget'),
    path('heavy_select2_widget',
         TemplateFormView.as_view(form_class=HeavySelect2WidgetForm), name='heavy_select2_widget'),
    path('heavy_select2_multiple_widget',
         TemplateFormView.as_view(form_class=HeavySelect2MultipleWidgetForm, success_url='/'),
         name='heavy_select2_multiple_widget'),

    path('model_select2_widget',
         TemplateFormView.as_view(form_class=AlbumModelSelect2WidgetForm),
         name='model_select2_widget'),

    path('model_select2_tag_widget',
         TemplateFormView.as_view(form_class=ModelSelect2TagWidgetForm),
         name='model_select2_tag_widget'),

    path('model_chained_select2_widget',
         TemplateFormView.as_view(form_class=AddressChainedSelect2WidgetForm),
         name='model_chained_select2_widget'),

    path('heavy_data_1', heavy_data_1, name='heavy_data_1'),
    path('heavy_data_2', heavy_data_2, name='heavy_data_2'),

    path('select2/', include('django_select2.urls')),
]
