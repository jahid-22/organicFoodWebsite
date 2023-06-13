from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from . forms import UserLogin, MyPassChange, PassResetEmail, PassReset
from django.conf import settings
from django.conf.urls.static import static

# Path writing.
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('products/', views.Products.as_view(), name="product"),
    path('product_detail/<int:id>/', views.product_detail, name="product_detail"),
    path('feature/', views.FeatureView.as_view(), name="feature"),
    path('testimonial/', views.Testimonial.as_view(), name="testimonial"),
    path('contact/', views.Contact.as_view(), name="contact"),
    
    path('profile/', views.profile, name="profile"),
    path('address/', views.address, name="address"),
    path('add-address/', views.add_address, name="add-address"),
    
    path('add_to_cart/', views.add_to_cart, name="add_to_cart"),
    path('show_cart/', views.showcart, name="show_cart"),
    path('pluscart/', views.pluscart),
    path('minuscart/', views.minuscart),
    path('removecart/', views.removecart),
    path('checkout/', views.checkout, name="checkout"),
    path('buy-now/',views.buy_now, name="buy_now" ),
    path('paymentdone/', views.paymentdone, name="paymentdone"),
    path('order/', views.order, name="order"),

    # authentication paths

    path('registration/', views.UserRegistration.as_view(), name="register"),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='login.html',
         authentication_form=UserLogin), name="login"),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name="logout"),

    # password change form paths.

    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='password_change_form.html',
         form_class=MyPassChange, success_url='/passwordchangedone/'), name="passchange"),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(
        template_name='password_change_done.html'), name="passchangedone"),

    # password reset paths.

    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='password_reset.html',
         form_class=PassResetEmail), name="password_reset"),
    path('password_reset/done/', auth_view.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html', form_class=PassReset), name="password_reset_confirm"),
    path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'), name="password_reset_complete")


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
