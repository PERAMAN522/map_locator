from django.shortcuts import render,redirect
from .models import Country,State,City,Userdetails
from django.contrib import messages
from .forms import UserdetailForm

# Create your views here.


def index(request):
    user_details = Userdetails.objects.all()
    return render(request, 'map.html', {'user_details':user_details})
def user(request):
    country = Country.objects.all()
    c = Country()
    state = State.objects.all()
    user_details = Userdetails.objects.all()
    form = UserdetailForm
    print(user_details)
    if country != None:
        return render(request, 'userdetail.html', {'country': country, 'state':state, 'user_details': user_details, 'form':form})


def list_country(request):
    country=Country.objects.all()
    content = {'content': country}
    print(content)
    return render(request, 'userdetail.html', {'content':content})

def load_state(request):
    country_id=request.GET.get('country')
    states=State.objects.filter(country_id=country_id).order_by('name')
    return render(request,'userdetail.html',{'states':states})


def addData(request):
    if request.method == 'POST' and request.FILES['image']:
        email = request.POST['email']
        mobile = request.POST['mobile']
        if Userdetails.objects.filter(email=email).exists():
            messages.error(request, 'Email Already Exist')
            return redirect("home")
        elif Userdetails.objects.filter(mobile=mobile).exists():
            messages.error(request, 'Mobile Number Already Exist')
            return redirect("home")
        else:
            name = request.POST['name']
            email = request.POST['email']
            age = request.POST['age']
            gender = request.POST['gender']
            mobile = request.POST['mobile']
            country = request.POST['country']
            state = request.POST['state']
            city = request.POST['city']
            address = request.POST['address']
            image = request.FILES['image']
            location = request.POST['lang']

            l1 = location.split("(")
            l2 = l1[1].split(")")
            l3 = l2[0].split(",")
            lan = l3[0]
            lat = l3[1]

            print(location, "test")
            obj = Userdetails(name=name, email=email,gender=gender, age=age,address=address,mobile=mobile,country=country,state=state,city=city
                   ,image=image, lang=lan, lat=lat )
            obj.save()
            return redirect('/')
    return render(request, 'userdetail.html')