from django.urls import path, include

from .views import *


urlpatterns = [
    # Authorization
    path('sign-in/', SignInView.as_view(), name='sign_in'),
    path('token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),
    path('sign-out/', SignOutView.as_view(), name='sign_out'),
    path('sign-up/', SignUpView.as_view(), name='sign_up'),

    # Users
    path('users/', include([
        # path(''),
        # path('<uuid:pk>/'),
        path('current/', CurrentUserView.as_view(), name='current_user'),

    ]))

]
