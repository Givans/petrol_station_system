import datetime
import random

from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import Staff, Sell, Category, Update, About


# Create your views here.
@login_required(login_url='login')
def home(request):
    if request.user.is_superuser and request.user.is_staff:
        return redirect(admin_page)
    elif request.user.is_staff:
        return redirect(staff)
    else:
        messages.error(request, "Unauthorized access")
        return render(request, 'registration/login.html')


@login_required(login_url='login')
def admin_page(request):
    if request.user.is_superuser:
        categories = Category.objects.all().order_by('id').reverse()
        records = Sell.objects.all().order_by('id').reverse()
        updates = Update.objects.all().order_by('id').reverse()
        staffs = Staff.objects.all().order_by('id').reverse()
        try:
            about = About.objects.get(num=1)
        except:
            about = "Write an about"

        categories_no = Category.objects.all().count()
        all_customers = Sell.objects.all().count()
        all_updates = Update.objects.all().count()
        all_staff = Staff.objects.all().count()

        date = datetime.datetime.today()
        this_year = date.year
        this_month = date.month
        this_day = date.day

        about_us = about.details

        year_records = Sell.objects.filter(year=this_year).order_by('id').reverse()
        month_records = Sell.objects.filter(month=this_month).order_by('id').reverse()
        day_records = Sell.objects.filter(day=this_day).order_by('id').reverse()
        year_records_count = Sell.objects.filter(year=this_year).count()
        month_records_count = Sell.objects.filter(month=this_month).count()
        day_records_count = Sell.objects.filter(day=this_day).count()

        # for all records
        litre_total = 0
        amount_total = 0
        for r in records:
            l = r.litres
            a = r.amount
            litres = float(l)
            amount = float(a)
            litre_total += litres
            amount_total += amount

        # year records
        litre_year = 0
        amount_year = 0
        for y in year_records:
            y_l = y.litres
            y_a = y.amount
            y_litres = float(y_l)
            y_amount = float(y_a)
            litre_year += y_litres
            amount_year += y_amount

        # year month
        litre_month = 0
        amount_month = 0
        for m in month_records:
            m_l = m.litres
            m_a = m.amount
            m_litres = float(m_l)
            m_amount = float(m_a)
            litre_month += m_litres
            amount_month += m_amount

        # daily records
        litre_day = 0
        amount_day = 0
        for d in day_records:
            d_l = d.litres
            d_a = d.amount
            d_litres = float(d_l)
            d_amount = float(d_a)
            litre_day += d_litres
            amount_day += d_amount

        all_litres = litre_total
        all_amount = amount_total
        year_litres = litre_year
        year_amount = amount_year
        month_litres = litre_month
        month_amount = amount_month
        day_litres = litre_day
        day_amount = amount_day

        context = {
            'category': categories,
            'records': records,
            'updates': updates,
            'staffs': staffs,
            'about_us': about_us,

            # counts
            'category_no': categories_no,
            'all_updates': all_updates,
            'all_litres': all_litres,
            'all_amount': all_amount,
            'day_amount': day_amount,
            'day_litres': day_litres,
            'month_amount': month_amount,
            'month_litres': month_litres,
            'year_amount': year_amount,
            'year_litres': year_litres,
            'all_customers': all_customers,
            'all_staff': all_staff,
            'year_records_count': year_records_count,
            'month_records_count': month_records_count,
            'day_records_count': day_records_count,
        }
        return render(request, 'admin_user/index.html', context)
    else:
        return redirect(home)


def update(request):
    pass


@login_required(login_url='login')
def staff(request):
    if request.user.is_superuser and request.user.is_staff:
        return redirect(admin_page)
    elif request.user.is_staff:
        categories = Category.objects.all().order_by('id').reverse()
        records = Sell.objects.all().order_by('id').reverse()
        updates = Update.objects.all().order_by('id').reverse()

        categories_no = Category.objects.all().count()
        all_customers = Sell.objects.all().count()
        all_updates = Update.objects.all().count()

        date = datetime.datetime.today()
        this_year = date.year
        this_month = date.month
        this_day = date.day

        year_records = Sell.objects.filter(year=this_year).order_by('id').reverse()
        month_records = Sell.objects.filter(month=this_month).order_by('id').reverse()
        day_records = Sell.objects.filter(day=this_day).order_by('id').reverse()
        year_records_count = Sell.objects.filter(year=this_year).count()
        month_records_count = Sell.objects.filter(month=this_month).count()
        day_records_count = Sell.objects.filter(day=this_day).count()

        # for all records
        litre_total = 0
        amount_total = 0
        for r in records:
            l = r.litres
            a = r.amount
            litres = float(l)
            amount = float(a)
            litre_total += litres
            amount_total += amount

        # year records
        litre_year = 0
        amount_year = 0
        for y in year_records:
            y_l = y.litres
            y_a = y.amount
            y_litres = float(y_l)
            y_amount = float(y_a)
            litre_year += y_litres
            amount_year += y_amount

        # year month
        litre_month = 0
        amount_month = 0
        for m in month_records:
            m_l = m.litres
            m_a = m.amount
            m_litres = float(m_l)
            m_amount = float(m_a)
            litre_month += m_litres
            amount_month += m_amount

        # daily records
        litre_day = 0
        amount_day = 0
        for d in day_records:
            d_l = d.litres
            d_a = d.amount
            d_litres = float(d_l)
            d_amount = float(d_a)
            litre_day += d_litres
            amount_day += d_amount

        all_litres = litre_total
        all_amount = amount_total
        year_litres = litre_year
        year_amount = amount_year
        month_litres = litre_month
        month_amount = amount_month
        day_litres = litre_day
        day_amount = amount_day

        context = {
            'category': categories,
            'records': records,
            'updates': updates,

            # counts
            'category_no': categories_no,
            'all_updates': all_updates,
            'all_litres': all_litres,
            'all_amount': all_amount,
            'day_amount': day_amount,
            'day_litres': day_litres,
            'month_amount': month_amount,
            'month_litres': month_litres,
            'year_amount': year_amount,
            'year_litres': year_litres,
            'all_customers': all_customers,
            'year_records_count': year_records_count,
            'month_records_count': month_records_count,
            'day_records_count': day_records_count,
        }
        return render(request, 'users/index.html', context)
    else:
        return redirect(home)


@login_required(login_url='login')
def register_staff(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            idno = request.POST['idno']
            email = request.POST['email']
            age = request.POST['age']
            address = request.POST['address']
            username = request.POST['username']
            password = request.POST['password']
            password2 = request.POST['password2']

            if int(age) >= 18:

                if password == password2:
                    if User.objects.filter(email=email).exists():
                        messages.info(request, 'Email already in use')
                        return redirect(admin_page)
                    elif User.objects.filter(username=username).exists():
                        messages.info(request, 'Username already in use')
                        return redirect(admin_page)
                    else:
                        user = User.objects.create_user(first_name=firstname, last_name=lastname, is_staff=True,
                                                        username=username,
                                                        email=email, password=password)

                        # generating a serial number
                        def serial_number():
                            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                                       'q',
                                       'r',
                                       's', 't', 'u', 'v',
                                       'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                                       'M',
                                       'N',
                                       'O', 'P', 'Q', 'R',
                                       'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

                            let = 3
                            num = 2

                            sequence = random.sample(letters, let)
                            sym = random.sample(numbers, num)
                            sequence.extend(sym)
                            random.shuffle(sequence)
                            serial_num = ''.join([str(elem) for elem in sequence])  # listToStr
                            check = Staff.objects.filter(serial=serial_num).exists()
                            if check:
                                return serial_number()
                            else:

                                return serial_num

                        serial = serial_number()
                        member = User.objects.get(username=username)
                        staff = Staff.objects.create(serial=serial, member=member, first_name=firstname,
                                                     last_name=lastname,
                                                     username=username, email=email, idno=idno, age=age,
                                                     address=address)
                        staff.save()
                        user.save()

                        messages.info(request, 'staff added successfully')
                        return redirect('/')
                else:
                    messages.error(request, 'password mismatch')
                    return redirect(admin_page)
            else:
                messages.warning(request, 'age restricted')
                return redirect(admin_page)
        messages.warning(request, 'no staff added')
        return redirect(admin_page)
    messages.error(request, 'Unauthorized access')
    return redirect(home)


@login_required(login_url='login')
def new_sell(request, username):
    if request.user.is_staff:
        if request.method == 'POST':
            plate = request.POST['number_plate']
            fuel = request.POST['fuel']
            litres = request.POST['litres']
            if plate == '' or fuel == '' or litres == '':
                messages.error(request, 'empty empty fields')
                return redirect(staff)

            elif plate != '' and fuel != '' or litres != '':
                number_plate = plate.upper().strip().replace(" ", "")
                if Sell.objects.filter(number_plate=number_plate).exists():
                    initial_frequency = 0
                    frequencies = Sell.objects.filter(number_plate=number_plate)
                    for frequency in frequencies:
                        initial_frequency = frequency.f
                else:
                    initial_frequency = 0
                f = int(initial_frequency) + 1

                f_type = Category.objects.get(name=fuel)
                price = float(f_type.price)
                amount = float(litres) * price
                customer = Sell.objects.create(staff=username, number_plate=number_plate, fuel=fuel, litres=litres, f=f,
                                               amount=amount)
                customer.save()
                messages.info(request, 'process success')
                return redirect(staff)
            else:
                messages.error(request, 'something went wrong, refresh the page')
                return redirect(staff)
        else:
            messages.warning(request, 'Try again')
            return redirect(staff)
    messages.error(request, 'Unauthorized access')
    return redirect('/')


@login_required(login_url='login')
def new_category(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            name = request.POST['name']
            price = request.POST['price']
            if name == '' or price == '':
                messages.error(request, 'empty empty fields')
                return redirect(admin_page)

            elif name != '' and price != '':
                category = name.upper().strip().replace(" ", "_")
                check = Category.objects.filter(name=category).exists()
                if check:
                    messages.error(request, "Category already exists")
                    return redirect(admin_page)
                else:
                    instance = Category.objects.create(name=category, price=price)
                    instance.save()
                    messages.info(request, 'category added success')
                    return redirect(admin_page)
            else:
                messages.error(request, "error adding category")
                return redirect(admin_page)
        else:
            return redirect(admin_page)
    else:
        messages.error(request, "unauthorized access")
        return redirect('/')


@login_required(login_url='login')
def new_update(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            to = request.POST['to']
            subject = request.POST['subject']
            message = request.POST['message']
            if to == '' or subject == '' or message == '':
                messages.error(request, 'empty empty fields')
                return redirect(admin_page)

            elif to != '' and subject != '' and message != '':
                instance = Update.objects.create(to=to, subject=subject, message=message)
                instance.save()
                messages.info(request, 'notification sent successfully')
                return redirect(admin_page)
            else:
                messages.error(request, "error sending notification")
                return redirect(admin_page)
        else:
            return redirect(admin_page)
    else:
        messages.error(request, "unauthorized access")
        return redirect('/')


# delete staff
@login_required(login_url='login')
def delete_staff(request, username):
    if request.user.is_superuser:
        instance = User.objects.get(username=username)
        instance.delete()
        messages.success(request, username + ' deleted successfully')
        return redirect(admin_page)
    else:
        messages.warning(request, 'unauthorized access')
        return redirect(home)


# delete category
@login_required(login_url='login')
def delete_category(request, category):
    if request.user.is_superuser:
        instance = Category.objects.get(name=category)
        instance.delete()
        messages.success(request, category + ' deleted successfully')
        return redirect(admin_page)
    else:
        messages.warning(request, 'unauthorized access')
        return redirect(home)


@login_required(login_url='login')
def post_about(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            about = request.POST['about']
            try:
                ab = About.objects.get(num=1)
                ab.details = about
                ab.save()
            except:
                instance = About.objects.create(details=about)
                instance.save()
            messages.success(request, about + ' added successfully')
            return redirect(admin_page)
        else:
            return redirect(admin_page)
    else:
        messages.warning(request, 'unauthorized access')
        return redirect(home)


# # deleting parking
# def delete_parking(request, serial):
#     instance = SerialNumber.objects.get(s_num=serial)
#     instance.delete()
#     messages.success(request, 'parking deleted successfully')
#     return redirect(clerk)
#
#
# def admin_pages(request, page):
#     pages = page + '.html'
#     print(pages)
#     tmp = 'admin_page/admin_pages/' + pages
#     if request.user.is_superuser:
#         user = get_user_model()
#         users = user.objects.values()
#         # if users.username == 'Teicy':
#         #     context = {
#         #         'clerks': users
#         #     }
#         print(users.username)
#         return render(request, tmp)
#
#
# def customer_contact(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             c_form = ContactForm(request.POST)
#             if c_form.is_valid():
#                 name = request.POST['name']
#                 email = request.POST['email']
#                 message = c_form.save(commit=False)
#                 message.name = name
#                 message.customer = request.user
#                 message.email = email
#                 message.save()
#                 messages.success(request, 'email sent successfully')
#                 return redirect('/')
#             else:
#                 messages.error(request, 'invalid data!! try again')
#                 return redirect('/')
#         else:
#             return redirect('/')
#     else:
#         messages.warning(request, 'Kindly login')
#         return redirect('/')
#
#
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Success!! logout..')
    return redirect('/')
