from django.shortcuts import render, redirect
from myapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
from django.db import IntegrityError
from django.db.models import Q 

# Public Content
# -----------------------------------------------------------------------------

def search(req):
    dataa=CourseModel.objects.all()[0:4]
    dataaa=CourseModel.allcategory(CourseModel)[0:4]
    category=Category_model.objects.all().order_by('id')
    total_Course = CourseModel.objects.count()


    
    query = req.GET.get('query')
    
    if query:
        
        data = CourseModel.objects.filter(Q(Course_title__icontains=query) 
                                       |Q(description__icontains=query))
        
    
    else:
        data = CourseModel.objects.none()
        
    context={
        'data':data,
        'dataaa':dataaa,
        'query':query,
        'dataa': dataa,
        'category': category,
        'total_Course': total_Course,
    }
    
    return render(req,"search.html",context)


def base(req,id):
    current_user=req.user

    data=CreatorProfileModel.objects.filter(user=current_user)
    dataa=viewerProfileModel.objects.filter(user=current_user)
    text={
        'data':data,
        'dataa':dataa,
        
    }

    return render (req, 'base.html',text)

def home(req):

    return render (req, 'home.html')

def addform(req):

    return render (req, 'add.html')

def about(req):

    return render (req, 'about.html')

def contact(req):

    return render (req, 'contact.html')

def course_details(req,id):
    vid=CourseModel.objects.filter(id=id)
    video=Video.objects.filter(id=id).order_by('id')
    only=only1.objects.filter(id=id).order_by('id')

    return render (req, 'course-details.html',{'vid':vid,'video':video, 'only':only})

def courses(req):
    data=CourseModel.objects.filter()
    dataa=CourseModel.objects.all()[0:4]
    dataaa=CourseModel.allcategory(CourseModel)[0:4]
    category=Category_model.objects.all().order_by('id')
    total_Course = CourseModel.objects.count()

    context = {
        'data': data,
        'dataa': dataa,
        'dataaa': dataaa,
        'category': category,
        'total_Course': total_Course,
    }
    
    return render (req, 'courses.html',context)

def auther(req,id):
    data=CourseModel.objects.filter(id=id)
    trainer=author.objects.filter(id=id)

    return render (req, 'auther.html',{'data':data, 'trainer':trainer})

def video_courses(req,id):
    data=CourseModel.objects.filter(id=id)
    courses=author_profile.objects.filter(id=id)

    return render (req, 'video_courses.html',{'data':data, 'courses':courses})

def events(req):

    return render (req, 'events.html')

def pricing(req):

    return render (req, 'pricing.html')

def trainers(req):
    data=author_profile.objects.all()
    return render (req, 'trainers.html',{'data':data,'courses':courses})

def starter_page(req):

    return render (req, 'starter-page.html')


def profile(req):
    current_user=req.user

    data=CreatorProfileModel.objects.filter(user=current_user)
    dataa=viewerProfileModel.objects.filter(user=current_user)
    text={
        'data':data,
        'dataa':dataa,
    }

    return render (req, 'profile.html',text)

def update_profile(req,id):
    user = req.user
    profile = None

    # Determine which profile to edit based on user type
    if user.user_type == 'viewer':
        profile = viewerProfileModel.objects.get(user=user)
    elif user.user_type == 'creator':
        profile = CreatorProfileModel.objects.get(user=user)

    if req.method == 'POST':
        # Update user details
        user.email = req.POST.get('email')
        user.first_name = req.POST.get('first_name')
        user.last_name = req.POST.get('last_name')
        user.save()

        # Update profile picture only if a new one is uploaded

        if req.FILES.get('Image'):
            profile.Image = req.FILES['Image']

        profile.save()  
        return redirect("profile")

    return render (req, 'update_profile.html', {'user': user, 'profile': profile})


# Authentication
# -----------------------------------------------------------------------------


def password_change(req):
    current_user=req.user
    if req.method == 'POST':
        currentpassword = req.POST.get("currentpassword")
        newpassword = req.POST.get("newpassword")
        confirmpassword = req.POST.get("confirmpassword")

        if check_password(currentpassword,req.user.password):
            if newpassword==confirmpassword:
                current_user.set_password(newpassword)
                current_user.save()
                update_session_auth_hash(req,current_user)
                return redirect("loginpage")
            
            
            if newpassword != confirmpassword:
                return redirect('password_change')
            else:
                return render(req, "password.html")
            
    return render(req, 'password.html')


def loginpage(req):
    if req.method == 'POST':
        username = req.POST.get("username")
        password = req.POST.get("password")

        # Check if both username and password are provided
        if not username or not password:
            return render(req, "login.html")

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is not None:
            login(req, user)
            return redirect("home")
        else:
            return render(req, "login.html")

    return render(req, "login.html")


def registerpage(req):
    if req.method == 'POST':
        username = req.POST.get("username")
        email = req.POST.get("email")
        user_type = req.POST.get("usertype")
        password = req.POST.get("password")
        confirm_password = req.POST.get("confirm_password")

        # Check if passwords match
        if password != confirm_password:
            return render(req, "signupPage.html")

        # Create user
        try:
            user = Custom_user.objects.create_user(
                username=username,
                email=email,
                user_type=user_type,
                password=password,
            )
            # Create the appropriate user profile based on user_type
            if user_type == 'viewer':
                viewerProfileModel.objects.create(user=user)
            elif user_type == 'creator':
                CreatorProfileModel.objects.create(user=user)

            return redirect("loginpage")
        except IntegrityError:
            return render(req, "signupPage.html")

    return render(req, "signupPage.html")

def logoutpage(req):
    logout(req)
    return redirect('loginpage')