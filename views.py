from django.shortcuts import render

# Create your views here.

from .models import userlogin

from django.db.models import Max



def adminfirst(request):
    return render(request,'./lmsapp/adminfirst.html')
#..........................................................................

def bookdetails(request):
    return render(request, './lmsapp/bookdetails.html')

#............................................................................

def feedback(request):
    return render(request, './lmsapp/feedback.html')

#...............................................................................

def payment(request):
    return render(request, './lmsapp/payment.html')

#...............................................................................

def contactus(request):
    return render(request, './lmsapp/contactus.html')
#.............................................................................

def firstpage(request):
        return render(request, './lmsapp/firstpage.html')
# .............................................................................
def adminlogin(request):
    return render(request, './lmsapp/adminlogin.html')
# ..............................................................................
def register(request):
    return render(request,'./lmsapp/register.html')
#...............................................................................
def addbook(request):
    return render(request,'./lmsapp/addbook.html')
#...............................................................................
def studlogin(request):
    return render(request,'./lmsapp/studlogin.html')
#...............................................................................

def about(request):
    return render(request,'./lmsapp/about.html')
#...............................................................................

def adminviewbook(request):
    return render(request,'./lmsapp/adminviewbook.html')
#...............................................................................

def studentretrive(request):
    return render(request,'./lmsapp/studentretrive.html')
#...............................................................................


#...............................................................................
def update(request):
    return render(request,'./lmsapp/update.html')
#...............................................................................




def all_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = userlogin.objects.filter(username=un, password=pwd, user_type='user')
        ub = userlogin.objects.filter(username=un, password=pwd, user_type='admin')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].username
            request.session['user_id'] = ul[0].id
            context2 = {'uname': request.session['user_name']}
            return render(request,'./lmsapp/studlogin.html',context2)
        elif len(ub) == 1:
            request.session['user_name'] = ub[0].username
            request.session['user_id'] = ub[0].id
            context1={'uname': request.session['user_name']}
            return render(request,'./lmsapp/adminfirst.html',context1)
        else:
            msg = '<h1> Invalid UserName or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './lmsapp/login.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, './lmsapp/login.html',context)
    #............................................................................................................


from.models import student_details
def student_add(request):
    if request.method == 'POST':

        name = request.POST.get('name')

        gender = request.POST.get('gender')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        date = request.POST.get("date")
        username = email
        #status = "new"
        if userlogin.objects.filter(username=email):
            msg = {'msg1': 'username already exist.....'}
            return render(request,'./lmsapp/register.html',msg)
        else:

            ul = userlogin(username=email, password=password, user_type='user')
            ul.save()
            user_id = userlogin.objects.all().aggregate(Max('id'))['id__max']

            ud = student_details(user_id=user_id,stud_name=name, date_of_birth=date, gender=gender,address=address, phn_no=phone, email_id=email )
            ud.save()

            print(user_id)
            context = {'msg': 'User Registered'}
            return render(request, 'lmsapp/register.html',context)

    else:
        return render(request, 'lmsapp/register.html')


def profile(request):
    id = request.session['user_name']
    single = student_details.objects.filter(email_id=id)
    context={'student_details':single}
    return render(request,'./lmsapp/profile.html',context)
#.......................................................................................

from.models import book_details
def book_add(request):
    if request.method == 'POST':


        book_name = request.POST.get('name')
        author_name = request.POST.get('authorname')
        book_copies = request.POST.get('copies')
        date=request.POST.get("date")


        ud = book_details(book_name=book_name, publish_date=date, author_name=author_name,book_copies=book_copies )
        ud.save()


        context = {'msg': 'Book added'}
        return render(request, './lmsapp/addbook.html',context)

    else:
        return render(request, './lmsapp/addbook.html')

#.......................................................................................



def logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return firstpage(request)
    else:
        return firstpage(request)

#.......................................................................................
#retrival

def retrive_book(request):
    details = book_details.objects.all()
    d = { 'book': details }
    return render(request, './lmsapp/bookdetails.html',d)
#............................................................................
#retrival

def retrivestud_book(request):
    details = book_details.objects.all()
    d = { 'books': details }
    return render(request, './lmsapp/adminviewbook.html',d)
#............................................................................

def retrive_student(request):
    stdetails = student_details.objects.all()


    l = userlogin.objects.all()
    d = {'student': stdetails, 'st_login': l}

    return render(request, './lmsapp/studentretrive.html',d)

#............................................................................................
def student_details_update(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        up = student_details.objects.get(id=int(id))

        stud_name = request.POST.get('stud_name')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        date_of_birth = request.POST.get('date_of_birth')
        email_id = request.POST.get('email_id')
        phn_no = request.POST.get('phn_no')

        up.stud_name = stud_name
        up.gender = gender
        up.address  = address
        up.date_of_birth  = date_of_birth
        up.email_id = email_id
        up.phn_no = phn_no
        up.save()


        context = {'msg': 'student Details Updated','up':up}
        return render(request, 'lmsapp/update.html',context)

    else:
        id=request.GET.get('id')
        up = student_details.objects.get(id=int(id))
        context={'up':up}
        return render(request, 'lmsapp/update.html',context)




#..................................................................................................................................

def book_details_update(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        ub = book_details.objects.get(id=int(id))

        book_name = request.POST.get('book_name')
        author_name = request.POST.get('author_name')
        publish_date = request.POST.get('publish_date')
        book_copies = request.POST.get('book_copies')

        ub.book_name = book_name
        ub.author_name  = author_name
        ub.publish_date  = publish_date
        ub.book_copies = book_copies
        ub.save()


        context = {'msg': 'Book Details Updated','ub':ub}
        return render(request, 'lmsapp/bookupdate.html',context)

    else:
        id=request.GET.get('id')
        ub = book_details.objects.get(id=int(id))
        context={'ub':ub}
        return render(request, 'lmsapp/bookupdate.html',context)

#....................................................................................
def delete(request):
    book_id=request.GET.get('d_id')
    deletebook=book_details.objects.get(id=int(book_id))
    deletebook.delete()
    details = book_details.objects.all()
    d = {'book': details}
    return render(request, './lmsapp/bookdetails.html',d)
#....................................................................................

def studdelete(request):
    stud_id=request.GET.get('s_id')

    deletestudent=student_details.objects.get(user_id=int(stud_id))
    deletestudent.delete()
    l = userlogin.objects.get(id=stud_id)
    l.delete()

    stdetails = student_details.objects.all()
    d = {'student': stdetails}
    return render(request, './lmsapp/studentretrive.html', d)







