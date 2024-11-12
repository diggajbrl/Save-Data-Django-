from django.shortcuts import render
from app.models import Myform  # Import your model

def app(request):
    success_message = ''  # Initialize a variable to hold the success or error message

    if request.method == 'POST':  # Check if the form has been submitted
        # Get form data
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        idemail = request.POST.get('email')

        # Check if the email already exists in the database
        if Myform.objects.filter(my_email=idemail).exists():
            success_message = 'Error: This email is already in use.'
        else:
            # Create and save a new Myform object if the email is not already in use
            try:
                apple = Myform(first_name=fname, last_name=lname, my_email=idemail)
                apple.save()
                success_message = 'Success: Thank you for submitting!'
            except Exception as e:
                success_message = f'Error: {str(e)}'  # Catch any other errors (e.g., database issues)

    # Render the template with the success or error message
    return render(request, 'index.html', {'success_message': success_message})
