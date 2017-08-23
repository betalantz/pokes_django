from django.shortcuts import render, redirect
from ..users_app.models import *
from models import *
from django.contrib import messages
from ..users_app.views import sessionCheck
from django.core.urlresolvers import reverse
from django.db.models import Count

def test(request):
    print '>'*20, 'welcome to heroes_app views'

def dashboard(request):
    if sessionCheck(request)==False:
        return redirect ('/')
    logged_user = User.objects.get(id=request.session['user_id'])
    context = {
        'users' : User.objects.all().exclude(id=request.session['user_id']),
        'poked_curr' : logged_user.relationships.filter(poke_receivers__poke_giver=logged_user).annotate(dcount=Count('alias')),
        'poked_ppl' :  logged_user.relationships.filter(poke_givers__poke_receiver=logged_user).annotate(pcount=Count('alias'))
        }
    return render(request, 'main_app/dashboard.html', context)

def get_pokers(request):
    logged_user = User.objects.get(id=request.session['user_id'])
    query1 = logged_user.relationships.filter(
        poke_receivers__poke_giver=logged_user
    )


def addPoke(request, victim_id):
    victim = User.objects.get(id=victim_id)
    victim.all_pokes += 1
    victim.save()

    my_id = request.session['user_id']
    my_user = User.objects.get(id=my_id)
    
    p = Pokes.objects.create(poke_giver=poke_stat, poke_receiver=victim, total_this_rel = 1)
    p.save()
    
    return redirect('/main_app/dashboard')

