# file which holds context processors for contact form.

from .forms import ContactForm

def contact(request):
    contact_form = {}
    contact_form['form'] = ContactForm()
    return contact_form
