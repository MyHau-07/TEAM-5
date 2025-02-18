from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser
from home.forms import CustomUserForm
from home.forms import BookingForm
from .models import Appointment
from .models import GioHang
from .models import Services
from .models import Booking
from .models import HoaDon
from .models import Dentist
from home.forms import DentistForm
from home.forms import DangKiLichNghiForm, ThemDichVuForm, SuaDichVuForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.http import JsonResponse# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Count
from .models import MedicalRecord
from django.views.decorators.csrf import csrf_exempt
from datetime import date
@login_required
def user (request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserForm(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,"Cập nhật thông tin thành công!")
            return redirect('user')  # Reload the profile page after saving the data
        else:
            # Thông báo lỗi nếu form không hợp lệ
            messages.error(request, "Đã có lỗi xảy ra. Vui lòng thử lại.")
    else:
        form = CustomUserForm(instance=user)
    return render(request, 'Users/user.html', {'user': user, 'form': form})

@csrf_exempt
def them_vao_gio_hang(request, dich_vu_id):
    if request.method == 'POST':
        user = request.user
        service = Services.objects.get(id=dich_vu_id)
        
        # Kiểm tra xem dịch vụ đã có trong giỏ hàng chưa
        gio_hang_item, created = GioHang.objects.get_or_create(user=user, dich_vu=service)
        
        if not created:
            gio_hang_item.so_luong += 1
            gio_hang_item.save()
        
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@login_required
def xoa_khoi_gio_hang(request, item_id):
    try:
        item = GioHang.objects.get(id=item_id)
        item.delete()  # Xóa item khỏi giỏ hàng
    except GioHang.DoesNotExist:
        # Nếu không tìm thấy item, có thể thông báo lỗi
        pass
    
    return redirect('GioHang')  # Quay lại trang giỏ hàng hoặc trang phù hợp



def sua_so_luong(request, gio_hang_id):
    gio_hang = get_object_or_404(GioHang, id=gio_hang_id)

    action = request.POST.get('action')
    if action == 'increase':
        gio_hang.so_luong += 1
    elif action == 'decrease' and gio_hang.so_luong > 1:
        gio_hang.so_luong -= 1
    else:
        return JsonResponse({'error': 'Số lượng không hợp lệ!'}, status=400)

    gio_hang.save()
    return JsonResponse({'so_luong': gio_hang.so_luong})

# them dich vu
def add_to_cart(request, dich_vu_id):
    # Lấy dịch vụ từ cơ sở dữ liệu
    dich_vu = Services.objects.get(id=dich_vu_id)
    
    # Tạo đối tượng giỏ hàng mới
    GioHang.objects.create(user=request.user, dich_vu=dich_vu)
    
    # Sau khi thêm dịch vụ vào giỏ hàng, redirect về trang dịch vụ
    return redirect('dichvu_list')  # 'dichvu_list' là tên của URL trang dịch vụ

@login_required
def Gio_Hang(request):
    gio_hang_items = GioHang.objects.filter(user=request.user)
    #total_price = sum(item.dich_vu.gia * item.so_luong for item in gio_hang_items) sai sua thanh
    total_price = sum(float(item.dich_vu.price) * item.so_luong for item in gio_hang_items)
    return render(request, 'Pages/GioHang.html', {
        'gio_hang_items': gio_hang_items,
        'total_price': total_price
    })

@login_required
def thanh_toan(request):
    if request.method == 'POST':
        gio_hang = GioHang.objects.filter(user=request.user)
        
        if not gio_hang.exists():
            messages.error(request, 'Giỏ hàng của bạn đang trống!')
            return redirect('xem_gio_hang')
        
        service_names = []
        tong_tien = 0
        
        for item in gio_hang:
            service_names.append(item.dich_vu.name)
            tong_tien += float(item.dich_vu.price) * item.so_luong
        
        services_str = ", ".join(service_names)
        
        # Tạo hóa đơn kèm user
        hoadon = HoaDon.objects.create(
            user=request.user, 
            dich_vu=services_str, 
            tong_tien=tong_tien
        )
        
        # Xóa giỏ hàng sau khi thanh toán
        gio_hang.delete()
        
        messages.success(request, 'Thanh toán thành công!')
        return redirect('lichsu')  # Chuyển sang trang lichsu
    
    return redirect('xem_gio_hang')


@login_required
def lichsu(request):
    hoadons = HoaDon.objects.filter(user=request.user).order_by('-ngay_thanh_toan')
    return render(request, 'Users/lichsu.html', {'danh_sach_thanh_toan': hoadons})

#quân li thong tin benh nhan
@login_required
def quanlithongtinbenhnhan(request):
    query = request.GET.get('q', '').strip()
    if query:
        try:
            query_id = int(query)
        except ValueError:
            query_id = None

        if query_id is not None:
            # Nếu nhập số, tìm theo ID của hồ sơ (MedicalRecord.id) hoặc theo tên bệnh nhân
            records = MedicalRecord.objects.filter(
                Q(id=query_id) | Q(patient__full_name__icontains=query)
            )
        else:
            records = MedicalRecord.objects.filter(
                patient__full_name__icontains=query
            )
    else:
        records = MedicalRecord.objects.all()

    context = {
        'records': records,
        'query': query,
    }
    return render(request, 'Pages/quanlithongtinbenhnhan.html', context)


@login_required
def hosobenhan_detail(request, record_id):
    record = get_object_or_404(MedicalRecord, id=record_id)
    context = {
        'record': record,
        'appointments': record.appointments.all(),
        'communications': record.communications.all().order_by('timestamp'),
    }
    return render(request, 'Pages/hosobenhan_detail.html', context)

def booking(request):       
    services = Services.objects.filter(is_active=True)
    
    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            appointment_date = request.POST.get('appointment_date')  # Get appointment_date from POST
            form.save()
            messages.success(request, "Đặt lịch thành công! Thông tin đã được gửi đến quản trị viên.")
        else:
            messages.error(request, "Có lỗi xảy ra, vui lòng kiểm tra lại thông tin.")
        selected_date = request.POST.get('appointment_date', date.today().isoformat())
    else:
        form = BookingForm()
        selected_date = request.GET.get('appointment_date', date.today().isoformat())
        
    # If appointment_date is in POST, use it; otherwise, check GET

    all_times = [
        "08:00", "08:45", "09:30", "10:15", "11:00", "11:45",
        "13:15", "14:00", "14:45", "15:30", "16:15"
    ]

    # Fetch all bookings for the selected date at once
    booked_bookings = Booking.objects.filter(appointment_date=selected_date)

    valid_times = []
    for time in all_times:
        # Check if any booking exists for this time with service type 'dieu_tri'
        is_dieu_tri_booked = booked_bookings.filter(
            appointment_time=time,
            dich_vu__type='dieu_tri'  # Accessing type through the ForeignKey relationship
        ).exists()

        # Count how many bookings exist for this time with service type 'kham'
        kham_count = booked_bookings.filter(
            appointment_time=time,
            dich_vu__type='kham'  # Accessing type through the ForeignKey relationship
        ).count()

        if not is_dieu_tri_booked and kham_count < 3:
            valid_times.append(time)

    return render(request, 'Pages/booking.html', {
        'form': form,
        'serv': services,
        'valid_times': valid_times,
        'selected_date': selected_date,
    })
def ClicnicOwner (request):
    return render(request, 'Pages/ClicnicOwner.html')

def quanlichinhanh (request):
    return render(request, 'Pages/quanlichinhanh.html')

def quanlinhanvien (request):
    return render(request, 'Pages/quanlinhanvien.html')

def hosophongkham (request):
    return render(request, 'Pages/hosophongkham.html')

def quanlidichvu (request):
    return render(request, 'Pages/quanlidichvu.html')

def dentist (request):
    return render(request, 'Users/Dentist.html')

def chamcong (request):
    return render(request, 'Users/chamcong.html')

def nghiphep (request):
    return render(request, 'Users/nghiphep.html')

def lichlam (request):
    return render(request, 'Users/lichlam.html')

def lichhen (request):
    return render(request, 'Users/lichhen.html')

# def lichsu (request):
#     return render(request, 'Users/lichsu.html')

def appointment(request):
    appointments = Appointment.objects.all().order_by('date', 'time')
    return render(request, 'Users/appointment.html', {'appointments': appointments})

def submit_dklichnghi(request):
    if request.method == 'POST':
        form = DangKiLichNghiForm(request.POST)
        if form.is_valid():
            form.save()  # Lưu dữ liệu form vào cơ sở dữ liệu
            return redirect('dentist')  # Chuyển hướng đến trang thành công hoặc view khác
    else:
        form = DangKiLichNghiForm()
    
    return render(request, 'home/home/dentist_dashboard.html', {'form': form})



#----left menu
def dichvu(request):
    services = Services.objects.all() 
    return render(request, 'Pages/dichvu.html', {'services': services})

def uudai (request):
    return render(request, 'Pages/uudai.html')

def sukien (request):
    return render(request, 'Pages/sukien.html')  

def kienthuc (request):
    return render(request, 'Pages/kienthuc.html')
#left menu---

@login_required
def quanlidichvu (request):
    services = Services.objects.all()
    if request.method == 'POST':
        form = ThemDichVuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Thêm dịch vụ thành công.")
            return redirect('quanlidichvu')  # Tránh gửi lại form khi reload
        else:
            messages.error(request, "Thêm dịch vụ không thành công.")
    else:
        form = ThemDichVuForm()

    return render(request, 'Pages/quanlidichvu.html', {'services': services, 'form': form})

@login_required
def xoadichvu(request,service_id):
    service = get_object_or_404(Services, id=service_id)
    
    if request.method == "POST":
        service.delete()
        messages.success(request, "Dịch vụ đã được xóa thành công!")
        return redirect('quanlidichvu')  # Điều hướng về trang quản lý dịch vụ

    return redirect('quanlidichvu')

@login_required
def suadichvu(request, service_id):
    service = get_object_or_404(Services, id=service_id)

    if request.method == 'POST':
        form = SuaDichVuForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})  # Trả về JSON khi cập nhật thành công
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)  # Trả về lỗi nếu form không hợp lệ
    else:
        # Trả về dữ liệu dịch vụ dưới dạng JSON
        data = {
            'id': service.id,
            'name': service.name,
            'price': service.price,
            'info': service.info,
            'time': service.time,
        }
        return JsonResponse(data)
    
@login_required
def manage_dentists(request):
    if request.method == 'POST':
        form = DentistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quanlinhanvien')  # Tải lại trang để cập nhật danh sách
    else:
        form = DentistForm()

    dentists = Dentist.objects.all()
    return render(request, 'Pages/quanlinhanvien.html', {'form': form, 'dentists': dentists})

@login_required
def delete_dentist(request, dentist_id):
    dentist = get_object_or_404(Dentist, id=dentist_id)
    dentist.delete()
    messages.success(request, "Nhân viên đã được xóa thành công.")
    return redirect('quanlinhanvien')

@login_required
def edit_dentist(request, dentist_id):
    dentist = get_object_or_404(Dentist, id=dentist_id)

    if request.method == 'POST':
        dentist.FullName = request.POST.get("FullName", dentist.FullName)
        dentist.Specialization = request.POST.get("Specialization", dentist.Specialization)
        dentist.Dental_branch = request.POST.get("Dental_branch", dentist.Dental_branch)
        dentist.License_number = request.POST.get("License_number", dentist.License_number)
        dentist.Phone_Number = request.POST.get("Phone_Number", dentist.Phone_Number)
        dentist.Email = request.POST.get("Email", dentist.Email)
        dentist.Birthday = request.POST.get("Birthday", dentist.Birthday)
        
        # Chuyển đổi Gender từ chuỗi sang Boolean
        gender_value = request.POST.get("Gender", "").lower()
        if gender_value in ["true", "1", "yes"]:
            dentist.Gender = True
        elif gender_value in ["false", "0", "no"]:
            dentist.Gender = False

        dentist.save()
        return redirect('quanlinhanvien')  # Quay về trang danh sách nhân viên

    return render(request, 'quanlinhanvien.html', {'dentist': dentist})