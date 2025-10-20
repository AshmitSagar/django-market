from .models import Ad
from .owner import (
    OwnerListView,
    OwnerDetailView,
    OwnerCreateView,
    OwnerUpdateView,
    OwnerDeleteView,
)


# Create your views here.
class AdListView(OwnerListView):
    model = Ad
    # By convention
    # template_name = "mkt/ad_list.html"


class AdDetailView(OwnerDetailView):
    model = Ad


class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ["title", "price", "text"]


class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ["title", "price", "text"]


class AdDeleteView(OwnerDeleteView):
    model = Ad
