from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from profiles.models import UserProfile
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Send email to store owner
            try:
                send_mail(
                    subject=f"New contact message: {contact.subject}",
                    message=(
                        f"Name: {contact.name}\n"
                        f"Email: {contact.email}\n\n"
                        f"Message:\n{contact.message}"
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_RECEIVER_EMAIL],
                    fail_silently=False,
                )
            except Exception as e:
                print("Failed to send notification email:", e)

            # Send confirmation email to user
            send_mail(
                subject="Thanks for reaching out!",
                message=(
                    f"Hi {contact.name},\n\n"
                    "Thank you for contacting us! We have received your "
                    "message and will get back to you shortly.\n\n"
                    "Your message:\n"
                    f"{contact.message}"
                ),
                from_email="The Poster Vault <sannejohansson7@gmail.com>",
                recipient_list=[contact.email],
                fail_silently=False,
            )

            messages.success(request, 
                             "Your message has been sent successfully!")
            return redirect("contact")
    else:
        if request.user.is_authenticated:
            try:
                profile = request.user.userprofile
                initial_data = {
                    "name": profile.full_name or request.user.username,
                    "email": request.user.email,
                }
            except UserProfile.DoesNotExist:
                initial_data = {
                    "name": request.user.username,
                    "email": request.user.email,
                }
            form = ContactForm(initial=initial_data)

    return render(request, "contact/contact.html", {"form": form})
