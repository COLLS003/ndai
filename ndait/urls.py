from rest_framework_nested import routers
from . import views
# urlpatterns = router.urls


router = routers.DefaultRouter()
router.register('Passenger', views.PassengerViewSet)
router.register('voyague', views.VoyagueViewSet)
router.register('owners', views.OwnerViewSet)
router.register('driver', views.DriverViewSet)
router.register('vehicle', views.VehicleViewSet)
router.register('payment', views.PaymentViewSet)
router.register('paymentStatus', views.PaymentStatusViewSet)
router.register('bookings', views.BookingsViewSet)



urlpatterns = router.urls