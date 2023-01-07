from django.urls import path
from .views import (
                    monthly_challenge,
                    monthly_challenges_by_num
                    )

urlpatterns = [
    # path("", home),
    # path("january/", january),
    # path("february/", february),
    # path("march/", march),
    # path("april/", april),
    path("<int:month>/", monthly_challenges_by_num),
    path("<str:month>/", monthly_challenge, name="month-challenge")
]
