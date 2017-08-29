from django.shortcuts import render, redirect
from ..users_app.models import *
from models import *
from django.contrib import messages
from ..users_app.views import sessionCheck
from django.core.urlresolvers import reverse
from django.db.models import Count, Sum

def test(request):
    print '>'*20, 'welcome to main_app views'

def dashboard(request):
    if sessionCheck(request)==False:
        return redirect ('/')
    logged_user = User.objects.get(id=request.session['user_id'])
    context = {
        'users' : User.objects.all().exclude(id=request.session['user_id']),
        'numb_my_pokers' : Poke.objects.filter(poke_receiver=request.session['user_id']).count(),
        'all_pokers' : User.objects.filter(pokees=request.session['user_id']),
        # 'history' : all_pokes()
        # 'all_pokes' : User.objects.annotate(all_pokes=Count('poke_receivers'))
        # 'poked_curr' : logged_user.relationships.filter(poke_receivers__poke_giver=logged_user).annotate(dcount=Count('alias')),
        # 'poked_ppl' :  logged_user.relationships.filter(poke_givers__poke_receiver=logged_user).annotate(pcount=Count('alias'))
        }
    context['pokes'] = Poke.objects.filter(poke_receiver__in=context['users']).values('poke_receiver').annotate(sum=Sum('total_pokes'))
    print context['all_pokers']
    # context['these_pokes'] = these_pokes(request)        
    context['these_pokes'] = get_pokers(request)        
    return render(request, 'main_app/dashboard.html', context)

def get_pokers(request):
    incl_pokes = Poke.objects.filter(poke_receiver=request.session['user_id'])
    print incl_pokes
    return incl_pokes


# def these_pokes(request):
#     these_pokers = Poke.objects.filter(poke_receiver__pokees=request.session['user_id'])
#     # these_pokes = Poke.objects.filter(total_pokes__in=these_pokers)
#     # these_pokes = Poke.objects.filter(pokers__in=these_pokers)
#     my_num = request.session['user_id']
#     print my_num
#     print these_pokers
#     return these_pokers

def addPoke(request, victim_id):
    victim = User.objects.get(id=victim_id)
    my_id = request.session['user_id']
    my_user = User.objects.get(id=my_id)
    try:
        p = Poke.objects.get(poke_giver=my_user, poke_receiver=victim)
        p.total_pokes += 1
        p.save()
    except: 
        p = Poke.objects.create(poke_giver=my_user, poke_receiver=victim, total_pokes=1)
        p.save()

    return redirect('/main_app/dashboard')

