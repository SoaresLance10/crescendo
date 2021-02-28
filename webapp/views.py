from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .decorators import unauthenticated_user
from .models import User, Inter_participant, Intra_participant, Event, Council, Registration, TeamRegistration, Score


# Create your views here.
def index(request):
    return render(request, "webapp/index.html", {"top_message": "Welcome", "title": "Home"})

@unauthenticated_user
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["pw"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)

            return redirect(f"profile/{username}")
        else:
            message="Incorrect Username or Password, Try again."
            return render(request, "webapp/login.html", {"top_message": message, "title": "Login"})
    else:
        return render(request, "webapp/login.html", {"top_message": "Sign In with given Credentials", "title": "Login"})

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def create_council(request):
    if request.method == "POST":
        council = Council()

        name = request.POST["name"]
        username = request.POST["username"]
        pw1 = request.POST["pw1"]
        pw2 = request.POST["pw2"]

        if pw1!=pw2:
            return render(request, "webapp/createcouncil.html", {"top_message": "Passwords do not match, Try again.", "title": "Create Council"})
        
        try:
            user = User.objects.create_user(username, "studentscouncilfrcrce@gmail.com", pw1)
            user.save()
        except IntegrityError:
            return render(request, "webapp/createcouncil.html", {"top_message": "Council already Exists.", "title": "Create Council"})

        council.name = name
        council.username = username
        council.save()

        return redirect('createcouncil')

    else:
        return render(request, "webapp/createcouncil.html",{"title": "Create Council"})

def register(request, event_id):
    if request.method=="POST":
        if Event.objects.filter(event_id=event_id)[0].team == 0:
            parti = Intra_participant()
            register = Registration()
            event_id = request.POST['event_id']
            cap = Event.objects.filter(event_id=event_id)[0].class_cap
            event_name = Event.objects.filter(event_id=event_id)[0].name
            regs = Registration.objects.filter(event_id=event_id)
            class_regs = 0
            for reg in regs:
                if Intra_participant.objects.filter(roll_no = reg.p_id):
                    par = Intra_participant.objects.filter(roll_no = reg.p_id)[0]
                else:
                    par = False
                if par:
                    if par.class_name == request.POST['class']:
                        class_regs += 1
                        
            if class_regs >= cap:
                return render(request, "webapp/register.html", {"title": "Register", "event_name": event_name, "event_id": event_id, "top_message": "Max Participants from class already Registered"})

            parti.name = request.POST['name']
            parti.roll_no = request.POST['rollno']
            parti.class_name = request.POST['class']
            parti.phone = request.POST['phone']
            parti.email = request.POST['email']

            parti.save()

            register.p_id = request.POST['rollno']
            register.p_name = request.POST['name']
            register.event_id = event_id
            register.council_id = Event.objects.filter(event_id=event_id)[0].council_id
            register.phone = request.POST['phone']
            register.email = request.POST['email']
            register.save()

            update = Event.objects.filter(event_id=event_id)[0]
            update.total_reg = Registration.objects.filter(event_id=event_id).count()
            update.save()

            return render(request, "webapp/register.html", {"title": "Register", "event_name": event_name, "event_id": event_id, "top_message": "Registeration Successfull!"})
        
        else:
            parti = Intra_participant()
            register = Registration()
            team_reg = TeamRegistration()
            event_id = request.POST['event_id']
            event_name = Event.objects.filter(event_id=event_id)[0].name
            team_no = Event.objects.filter(event_id=event_id)[0].team

            cap = Event.objects.filter(event_id=event_id)[0].class_cap
            regs = Registration.objects.filter(event_id=event_id)
            class_regs = 0
            for reg in regs:
                if TeamRegistration.objects.filter(team_id = reg.p_id):
                    team = TeamRegistration.objects.filter(team_id = reg.p_id)[0]
                else:
                    team = False
                if team:
                    if team.class_name == request.POST['class']:
                        class_regs += 1
                        
            if class_regs >= cap:
                 return render(request, "webapp/teamregister.html", {"title": "Team Registration", "event_name": event_name, "event_id": event_id, "team": team_no, "top_message": "Max Teams from class already Registered"})

            parti.name = request.POST['p1_name']
            parti.roll_no = request.POST['p1_rollno']
            parti.class_name = request.POST['class']
            parti.phone = request.POST['phone']
            parti.email = request.POST['email']

            parti.save()

            team_reg.p1_id = request.POST['p1_rollno']
            team_reg.p1_name = request.POST['p1_name']
            team_reg.class_name = request.POST['class']
            team_reg.phone = request.POST['phone']
            team_reg.email = request.POST['email']
            if not request.POST['p2_name'] == "empty":
                team_reg.p2_id = request.POST['p2_rollno']
                team_reg.p2_name = request.POST['p2_name']
            else:
                team_reg.p2_name = ""
                team_reg.p2_id = 0
            if not request.POST['p3_name'] == "empty":
                team_reg.p3_id = request.POST['p3_rollno']
                team_reg.p3_name = request.POST['p3_name']
            else:
                team_reg.p3_name = ""
                team_reg.p3_id = 0
                
            team_reg.save()

            team = TeamRegistration.objects.filter(class_name = request.POST['class'], p1_id = request.POST['p1_rollno'], p2_name = request.POST['p2_name'])[0]

            register.p_id = team.team_id
            register.p_name = f"{team.class_name}: {team.p1_name} {team.p2_name} {team.p3_name}"
            register.event_id = event_id
            register.council_id = Event.objects.filter(event_id=event_id)[0].council_id
            register.phone = team.phone
            register.email = team.email
            register.save()

            update = Event.objects.filter(event_id=event_id)[0]
            update.total_reg = Registration.objects.filter(event_id=event_id).count()
            update.save()

            return render(request, "webapp/teamregister.html", {"title": "Team Registration", "event_name": event_name, "event_id": event_id, "team": team_no, "top_message": "Registration Successful"})
    else:
        event_name = Event.objects.filter(event_id=event_id)[0].name
        team = Event.objects.filter(event_id=event_id)[0].team
        if not team == 0:
            return render(request, "webapp/teamregister.html", {"title": "Team Registration", "event_name": event_name, "event_id": event_id, "team": team, "top_message": "Team Registration"})
        return render(request, "webapp/register.html", {"title": "Register", "event_name": event_name, "event_id": event_id, "top_message": "Enter your Details Carefully"})

def inter_register(request):
    if request.method=='POST':
        parti = Inter_participant()
        register = Registration()
        event_id = request.POST['event_id']

        parti.name = request.POST['name']
        parti.college_name = request.POST['college_name']
        parti.phone = request.POST['phone']
        parti.email = request.POST['email']

        parti.save()

        p=Inter_participant.objects.filter(name=request.POST['name'], college_name=request.POST['college_name'], phone=request.POST['phone'])[0]

        register.p_id = p.paticipants_id
        register.p_name = p.name
        register.event_id = event_id
        register.council_id = Event.objects.filter(event_id=event_id)[0].council_id
        register.phone = request.POST['phone']
        register.email = request.POST['email']
        register.save()
        
        update = Event.objects.filter(event_id=event_id)[0]
        update.total_reg = Registration.objects.filter(event_id=event_id).count()
        update.save()

        event_name = Event.objects.filter(event_id=event_id)[0].name
        return render(request, "webapp/register.html", {"title": "Register", "event_name": event_name, "event_id": event_id, "top_message": "Registeration Successfull!"})
        
    else:
        return HttpResponseRedirect(reverse("index"))

def events(request):
    message = "Events of Crescendo 2k21"
    events = {}
    councils = Council.objects.all()
    for council in councils:
        events[council.name]=Event.objects.filter(council_id=council.council_id)
    return render(request, "webapp/events.html", {"top_message": message, "title": "Events", "events": events, "councils": councils})

@login_required(login_url='login')
def profile(request, username):
    council=Council.objects.get(username=username)
    all_parti = {}
    event=Event.objects.all().filter(council_id=council.council_id)
    for eve in event:
        all_parti[eve] = Registration.objects.filter(event_id=eve.event_id)

    return render(request, "webapp/profile.html", {"council": council,"event": event, "all_parti": all_parti,"top_message": f"Welcome, {council.name}", "title": "Council Profile"})

def standings(request):
    scores = Score.objects.all().order_by('-score')
    return render(request, "webapp/standings.html", {"top_message": "Scores may not be up to date", "scores": scores})