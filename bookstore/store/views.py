from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UploadedFile

# Define your security code
SECURITY_CODE = 'MUGANZA123'  # Replace with your desired code

def home(request):
    return render(request, 'store/home.html')

def self(request):
    files = UploadedFile.objects.filter(category='self')
    return render(request, 'store/self.html', {'files': files})

def financial(request):
    files = UploadedFile.objects.filter(category='financial')
    return render(request, 'store/financial.html', {'files': files})

def skills(request):
    files = UploadedFile.objects.filter(category='skills')
    return render(request, 'store/skills.html', {'files': files})

def skill(request):
    files = UploadedFile.objects.filter(category='skill')
    return render(request, 'store/skill.html', {'files': files})

def guide(request):
    files = UploadedFile.objects.filter(category='guide')
    return render(request, 'store/guide.html', {'files': files})

def tutorial(request):
    files = UploadedFile.objects.filter(category='tutorial')
    return render(request, 'store/tutorial.html', {'files': files})

def upload(request):
    # Clear session on every page load to force security code re-entry on refresh
    request.session.pop('authenticated', None)  # Remove the session authentication
    
    # Check if the security code has been entered correctly
    if request.method == "POST":
        if request.POST.get("security_check"):  # If the security form is submitted
            entered_code = request.POST.get("security_code")

            if entered_code == SECURITY_CODE:
                # Store in session that the user is authenticated for this request
                request.session['authenticated'] = True
            else:
                return HttpResponse("Invalid security code. Please try again.")

        elif request.POST.get('delete') == 'delete':  # Handle file/link deletion
            # Check if the user has been authenticated
            if not request.session.get('authenticated', False):
                return HttpResponse("Unauthorized. You must enter the security code first.")

            category = request.POST.get('delete_category')
            file_name = request.POST.get('file_name')

            # Try to find the file/link with the provided name and category
            try:
                # Check for a file with the provided name in the specified category
                file_to_delete = UploadedFile.objects.get(file__icontains=file_name, category=category)  # For file
                file_to_delete.delete()  # Delete the file from the database
                return HttpResponse(f"File '{file_name}' from category '{category}' has been deleted.")
            except UploadedFile.DoesNotExist:
                try:
                    # Check for a link with the provided title in the specified category
                    link_to_delete = UploadedFile.objects.get(url__icontains=file_name, category=category)  # For link
                    link_to_delete.delete()  # Delete the link from the database
                    return HttpResponse(f"Link '{file_name}' from category '{category}' has been deleted.")
                except UploadedFile.DoesNotExist:
                    return HttpResponse(f"File or Link '{file_name}' not found in category '{category}'.")

        else:  # Handle file or link upload
            # Check if the user has been authenticated
            if not request.session.get('authenticated', False):
                return HttpResponse("Unauthorized. You must enter the security code first.")

            category = request.POST.get('category')  # Get the selected category
            file = request.FILES.get('file')  # Get the uploaded file (optional)
            url = request.POST.get('url')  # Get the submitted URL (optional)
            description = request.POST.get('description')  # Get the file description

            # Save the uploaded file or link to the database
            new_file = UploadedFile.objects.create(
                category=category,
                file=file if file else None,  # Save the file if provided
                url=url if url else None,  # Save the link if provided
                description=description
            )
            new_file.save()

            # Redirect to the appropriate category page
            return redirect(category)

    return render(request, 'store/upload.html')
