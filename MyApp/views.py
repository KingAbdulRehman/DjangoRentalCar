from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse,redirect
from MyApp.models import user_member, Brand, Testimonial, ContactUs, Vehicle, Subscriber, BookingInfo


def index(request):
    testimonial = Testimonial.objects.filter(t_isActive=True)
    brands = Brand.objects.all()
    cars = Vehicle.objects.all().order_by('v_id').reverse()[:9]
    return render(request, "index.html", {"Testimonial": testimonial, "brand": brands, "car": cars})


def register(request):
    Message = ""
    args = {}
    if request.method == "POST":
        varid = request.POST.get("tid")
        varGetFullname = request.POST.get("tname")
        varGetEmail = request.POST.get("temail")
        varGetPassword = request.POST.get("tpass")
        varGetCity = request.POST.get("tcity")
        varGetNumber = request.POST.get("tnum")
        if CheckUserName(varGetEmail) and varid == None:
            Message = "6"
        elif varGetFullname == "":
            Message = "0"
        elif varGetEmail == "":
            Message = "1"
        elif varGetPassword == "":
            Message = "2"
        elif varGetCity == "":
            Message = "3"
        elif varGetNumber == "":
            Message = "4"
        else:
            if varid != None and int(varid) > 0:
                user = user_member.objects.get(id=varid)
                user.username = varGetFullname
                user.email = varGetEmail
                user.passwrd = varGetPassword
                user.city = varGetCity
                user.phoneNumber = varGetNumber
                user.save()
                request.session['Name'] = varGetFullname
                return index(request)
            else:
                myUser = user_member(username=varGetFullname, email=varGetEmail, passwrd=varGetPassword,city=varGetCity, phoneNumber=varGetNumber)
                myUser.save()
                Message = "5"

        args['myMsg'] = Message
        args['FN'] = varGetFullname
        args['Email'] = varGetEmail
        args['City'] = varGetCity
        args['Phone'] = varGetNumber
    return render(request, 'Register.html', args)


def CheckUserName(email):
    Result = False
    User = user_member.objects.filter(email=email).values()
    if User.count() == 0:
        Result = False
    else:
        Result = True
    return Result


def login(request):
    return render(request, "login.html")


def verifyUser(request):
    Message = ""
    args = {}
    if request.method == "POST":
        varGetUserName = request.POST.get("tUser")
        varGetPassword = request.POST.get("tPass")
        User = user_member.objects.filter(email=varGetUserName, passwrd=varGetPassword).values()
        if varGetUserName == "":
            Message = "0"
        elif varGetPassword == "":
            Message = "1"
        elif User.count() == 0:
            Message = "2"

        if Message == "":
                request.session['id'] = User.get()['id']
                request.session['Name'] = User.get()['username']
                return redirect('/')

        else:
            args['myMsg'] = Message
            return render(request, "login.html", args)


def logout(request):
    request.session['id'] = ""
    request.session['Name'] = ""
    return login(request)


def about(request):
    return render(request, "About.html")


def contact(request):
    return render(request, "Contact.html")


def InsertContactUs(request):
    ErrorMsg = ""
    args = {}
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        desc = request.POST.get("desc")

        if name == "":
            ErrorMsg = "0"
        elif email == "":
            ErrorMsg = "1"
        elif desc == "":
            ErrorMsg = "2"
        else:
            contactForm = ContactUs(c_name=name, c_email=email, c_desc=desc)
            contactForm.save()
            ErrorMsg = "3"

        args['myMsg'] = ErrorMsg

    return render(request, 'Contact.html', args)


def cars(request):
    cars = Vehicle.objects.all()
    return render(request, "cars.html", {"cars": cars})


def InsertSubscriber(request):
    referring_url = request.META.get('HTTP_REFERER')

    if request.method == "POST":
        email = request.POST.get("subEmail")

        if email != "" and email != " " and CheckUserName(email) == True:
            data = Subscriber(s_email=email)
            data.save()

        return HttpResponseRedirect(referring_url)


def UpdateProfile(request):
    id = request.GET.get("id")
    print("check "+id+" check")
    if int(id) > 0:
        userData = user_member.objects.get(id=id)
        return render(request, "Register.html", {"data": userData})

    else:
        return render(request, "Register.html")


def CarDetails(request):
    id = request.GET.get("id")
    if int(id) > 0:
        vehicleData = Vehicle.objects.get(v_id=id)
        return render(request, "carDetails.html", {"data": vehicleData})
    else:
        return index(request)


def Booking(request):
    bookDate = request.POST.get("bookDate")
    returnDate = request.POST.get("retDate")
    vId = request.POST.get("vId")
    vehicle = Vehicle.objects.get(v_id=vId)
    uId = request.session['id']
    user = user_member.objects.get(id=uId)

    myUser = BookingInfo(b_bookdate=bookDate, b_returndate=returnDate, b_vehicle=vehicle, b_user=user)
    myUser.save()

    return index(request)


def BookingHistory(request):
    bookInfo = BookingInfo.objects.all().order_by('b_id').reverse()
    return render(request, "booking.html", {'book': bookInfo})
# Create your views here.
