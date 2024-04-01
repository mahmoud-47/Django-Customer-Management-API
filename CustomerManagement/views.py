from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from api.models import Client

def home(request):
    context = {}
    if request.GET.get('search'):
        search = request.GET.get('search')
        clients = Client.objects.filter(nom__icontains=search).order_by('-updated_at')
        context['msg_content'] = f'La recherche avec "{search}" a donné {clients.count()} résultats'
        context['msg_type'] = ""
    else:
        clients = Client.objects.all().order_by('-updated_at')
    
    if 'msg_content' in request.session:
        context['msg_content'] = request.session['msg_content']
        context['msg_type'] = request.session['msg_type']
        del request.session['msg_content']
        del request.session['msg_type']
    context['clients'] = clients
    return render(request, 'home.html', context)

def add(request):
    if(request.method == 'POST'):
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        if not nom:
            request.session['msg_content'] = "Le nom est requis !"
            request.session['msg_type'] = "danger"
        else:
            Client.objects.create(
                nom = nom,
                email = email,
                phone = phone
            )
            request.session['msg_content'] = f"L'utilisateur {nom} a été créé avec succés"
            request.session['msg_type'] = "success"
        return redirect('add')
    else:
        context = {}
        if 'msg_content' in request.session:
            context['msg_content'] = request.session['msg_content']
            context['msg_type'] = request.session['msg_type']
            del request.session['msg_content']
            del request.session['msg_type']
            
    return render(request,"add.html", context)

def edit(request, id):
    client = get_object_or_404(Client, id=id)
    if(request.method == 'POST'):
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        status = request.POST.get('status')
        if not nom:
            request.session['msg_content'] = "Le nom est requis !"
            request.session['msg_type'] = "danger"
        else:
            stat = 1 if status=="on" else 0
            client.nom = nom
            client.email = email
            client.phone = phone
            client.status = stat
            client.save()
            request.session['msg_content'] = f"L'utilisateur {nom} a été modifié avec succés"
            request.session['msg_type'] = "success"
        return redirect('edit', id=id)
    else:
        context = {}
        if 'msg_content' in request.session:
            context['msg_content'] = request.session['msg_content']
            context['msg_type'] = request.session['msg_type']
            del request.session['msg_content']
            del request.session['msg_type']
        context['client'] = client
            
    return render(request,"edit.html", context)

def delete(request, id):
    client = get_object_or_404(Client, id=id)
    client.delete()
    request.session['msg_content'] = "Le client a été supprimé avec succés"
    request.session['msg_type'] = "success"
    return redirect('home')
