from django.contrib.auth import update_session_auth_hash
from django.shortcuts import redirect,render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm


@login_required(login_url='login')
def changePassword (request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            currentUser = form.save()
            update_session_auth_hash(request, currentUser)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
    else:
        form = PasswordChangeForm(data=request.POST, user=request.user)
       
    return render (request, 'auth/changePassword.html', {'form':form})