from .models import Subscription
from .forms import UserRegistrationForm


from django.shortcuts import render, redirect
from django.utils.timezone import now, timedelta
from .forms import PurchaseForm
from .models import Purchase


def subscription_list(request):
    subscriptions = Subscription.objects.all()
    return render(request, 'shop/subscription_list.html', {'subscriptions': subscriptions})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # ساخت کاربر جدید
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'shop/register_done.html', {'new_user': new_user})
    else:
        form = UserRegistrationForm()
    return render(request, 'shop/register.html', {'form': form})




def purchase_subscription(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            subscription = form.cleaned_data['subscription']
            valid_until = now() + timedelta(days=30 * subscription.duration_months)
            Purchase.objects.create(
                user=request.user,
                subscription=subscription,
                valid_until=valid_until
            )
            return redirect('purchase_success')
    else:
        form = PurchaseForm()

    return render(request, 'shop/purchase.html', {'form': form})

def purchase_success(request):
    return render(request, 'shop/purchase_success.html')



from django.contrib.auth.decorators import login_required

@login_required
def user_purchases(request):
    purchases = Purchase.objects.filter(user=request.user)
    return render(request, 'shop/user_purchases.html', {'purchases': purchases})
