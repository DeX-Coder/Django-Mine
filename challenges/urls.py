from django.urls import path
from .views import (
                    index,
                    monthly_challenge,
                    monthly_challenges_by_num
                    )

urlpatterns = [
    path("", index), # /challenges/
    path("<int:month>/", monthly_challenges_by_num),
    path("<str:month>/", monthly_challenge, name="month-challenge"),

]
