from django.shortcuts import redirect
from forms import ContactForm
from contact import handle_form


class ContactFormMiddleware(object):
    def process_request(self, request):
        if request.POST and 'contact_form' in request.POST:
            modal_form = True if 'modal_form' in request.POST else False
            form, success = handle_form('Contact Form', request, ContactForm)
            if success:
                return redirect('/thank-you/')
        else:
            form, modal_form = ContactForm(), False
        request.contact_form = form
        request.is_modal_form = modal_form