


from .models import Horoscope, Compatibility
from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Horoscope
from .utils import parse_xml_file
from .forms import UploadXMLForm  # We'll create this form in the next step


class HoroscopeAdmin(admin.ModelAdmin):
    change_list_template = "admin/horoscope_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('import-xml/', self.admin_site.admin_view(self.import_xml_view), name='import-xml'),
        ]
        return custom_urls + urls

    def import_xml_view(self, request):
        if request.method == "POST":
            form = UploadXMLForm(request.POST, request.FILES)
            if form.is_valid():
                uploaded_file = request.FILES['xml_file']
                if uploaded_file.name.endswith('.xml'):
                    try:
                        horoscope_data = parse_xml_file(uploaded_file)
                        for data in horoscope_data:
                            Horoscope.objects.update_or_create(
                                sign=data['sign'],
                                defaults={
                                    'description': data['description'],
                                    'start_date': data['start_date'],
                                    'end_date': data['end_date'],
                                    'element': data['element'],
                                    'color': data['color'],
                                    'positive_traits': data['positive_traits'],
                                    'negative_traits': data['negative_traits'],
                                }
                            )
                        self.message_user(request, "Horoscope data imported successfully.")
                        return redirect("..")
                    except ValueError as e:
                        self.message_user(request, f"Error in XML file: {e}")
                else:
                    self.message_user(request, "Please upload a valid XML file.")
        else:
            form = UploadXMLForm()

        context = self.admin_site.each_context(request)
        context['form'] = form
        return render(request, "admin/import_xml.html", context)

    import_xml_view.short_description = "Import from XML"


admin.site.register(Horoscope, HoroscopeAdmin)

admin.site.register(Compatibility)
