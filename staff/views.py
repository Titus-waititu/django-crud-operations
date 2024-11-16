from django.shortcuts import redirect, render

from staff.models import Staff

# Create your views here.
def home(request):
    staff = Staff.objects.all()
    context = {
        'staff':staff
    }
    return render(request, 'home.html',context)

def insert(request):
    return render(request, 'insert_data.html')

def insert_data(request):
    if request.method == 'POST':
        image = request.FILES['image']
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['age']
        department = request.POST['department']
        salary = request.POST['salary']

        staff = Staff(
            image = image,
            fname = fname,
            lname = lname,
            age = age,
            department = department,
            salary = salary
        )

        staff.save()
        return redirect('/')

def update(request,id):
    staff = Staff.objects.get(id = id)
    if request.method == 'POST':
        image = request.FILES['image']
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['age']
        department = request.POST['department']
        salary = request.POST['salary']
        
        staff.image = image
        staff.fname = fname
        staff.lname = lname
        staff.age = age
        staff.department = department
        staff.salary = salary
        

        staff.save()
        return redirect('/')


    return render(request, 'update_details.html',{'staff':staff})


def delete(request,id):
    staff = Staff.objects.get(id = id)
    staff.delete()
    return redirect('/')