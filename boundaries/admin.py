from django.contrib import admin
# ============================================================================ #
from leaflet.admin import LeafletGeoAdmin
# ============================================================================ #
from .models import Boundary
# ============================================================================ #



# =============================== BOUNDARYADMIN ============================== #


class BoundaryAdmin(LeafletGeoAdmin):
    list_display = ["pk", "name", "pcode"]

    list_display_links = ["name"]


# ================================= REGISTER ================================= #


admin.site.register(Boundary, BoundaryAdmin)