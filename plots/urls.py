from django.urls import path
from .views import AddPlotView, EditPlotView, DeletePlotView, ListPlotsView
 
urlpatterns = [
    path('plots/add', AddPlotView.as_view(), name='add-plot'),
    path('plots/<str:plot_id>', EditPlotView.as_view(), name='edit-plot'),
    path('plots/<str:plot_id>/delete', DeletePlotView.as_view(), name='delete-plot'),
    path('plots', ListPlotsView.as_view(), name='list-plots'),
] 