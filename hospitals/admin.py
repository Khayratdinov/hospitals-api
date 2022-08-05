from django.contrib import admin
# ============================================================================ #
from leaflet.admin import LeafletGeoAdmin
# ============================================================================ #
from .models import Hospital



# =============================== HOSPITALADMIN ============================== #


class HospitalAdmin(LeafletGeoAdmin):
    list_display = ["name", "lon", "lat", "beds", "province_name", "province_code"]



# ================================= REGISTER ================================= #


admin.site.register(Hospital, HospitalAdmin)