from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser
from home.forms import CustomUserForm
from home.forms import BookingForm
from .models import Appointment
from .models import GioHang
from .models import Services
from .models import HoaDon
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.http import JsonResponse# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import MedicalRecord
from .models import  LichHen, LichLamViec, CaLamViec
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from home.forms import LichLamViecForm

#user
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
#GIO HANG
@login_required
def them_vao_gio_hang(request, dich_vu_id):
    dich_vu = get_object_or_404(DichVu, id=dich_vu_id)
    
    # Kiểm tra xem sản phẩm đã có trong giỏ hàng chưa
    gio_hang, created = GioHang.objects.get_or_create(user=request.user, dich_vu=dich_vu)
    
    if not created:
        gio_hang.so_luong += 1  # Nếu đã có thì tăng số lượng
        gio_hang.save()

    messages.success(request, f'Đã thêm {dich_vu.ten_dich_vu} vào giỏ hàng!')

    return redirect('xem_gio_hang')

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
    dich_vu = DichVu.objects.get(id=dich_vu_id)
    
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

#LĨH SU HOA DONN CUA GIO HANG
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
#TRANG BOOKING
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Đặt lịch thành công! Thông tin đã được gửi đến quản trị viên.")
        else:
            messages.error(request, "Có lỗi xảy ra, vui lòng kiểm tra lại thông tin.")
    else:
        form = BookingForm()
    return render(request, 'Pages/booking.html', {'form': form})

#lich henj
def lichhen(request):
    user = request.user  # Lấy thông tin bệnh nhân đang đăng nhập
    medical_record = get_object_or_404(MedicalRecord, patient=user)  # Lấy hồ sơ bệnh án
    appointments = LichHen.objects.filter(medical_record=medical_record)  # Lấy lịch hẹn từ hồ sơ

    return render(request, 'Users/lichhen.html', {
        'medical_record': medical_record,
        'appointments': appointments
    })
@csrf_exempt
def update_appointment_status(request):
    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        status = request.POST.get('status')

        try:
            appointment = LichHen.objects.get(id=appointment_id)
            appointment.status = status
            appointment.save()
            return JsonResponse({"success": True})
        except LichHen.DoesNotExist:
            return JsonResponse({"success": False, "error": "Lịch hẹn không tồn tại!"})

    return JsonResponse({"success": False, "error": "Yêu cầu không hợp lệ!"})
#lichlam
@login_required
def lichlam(request):
    try:
        date_param = request.GET.get("date")

        # Xử lý ngày dựa trên tham số hoặc mặc định là hôm nay
        if date_param:
            try:
                today = datetime.strptime(date_param, "%Y-%m-%d")
            except ValueError:
                today = datetime.now()
        else:
            today = datetime.now()

        # Xác định đầu và cuối tuần
        start_of_week = today - timedelta(days=today.weekday())  # Thứ Hai đầu tuần
        end_of_week = start_of_week + timedelta(days=6)  # Chủ Nhật cuối tuần

        # Lấy danh sách lịch làm việc trong tuần, sắp xếp theo thứ tự từ Thứ Hai → Chủ Nhật
        lich_lam_viec = LichLamViec.objects.filter(
            ngay__range=[start_of_week, end_of_week]
        ).prefetch_related("ca_lam", "bac_si").order_by("thu", "ngay")

        # Danh sách ngày trong tuần
        week_days = [start_of_week + timedelta(days=i) for i in range(7)]

        context = {
            "today": today,
            "week_days": week_days,
            "lich_lam_viec": lich_lam_viec,
            "prev_week": (start_of_week - timedelta(days=7)).strftime("%Y-%m-%d"),
            "next_week": (end_of_week + timedelta(days=7)).strftime("%Y-%m-%d"),
        }

        return render(request, "Users/lichlam.html", context)

    except Exception as e:
        messages.error(request, f"❌ Đã xảy ra lỗi: {e}")
        return redirect("lichlam")






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

# def lichlam (request):
#     return render(request, 'Users/lichlam.html')

# def lichhen (request):
#     return render(request, 'Users/lichhen.html')

# def lichsu (request):
#     return render(request, 'Users/lichsu.html')

def appointment(request):
    appointments = Appointment.objects.all().order_by('date', 'time')
    return render(request, 'Users/appointment.html', {'appointments': appointments})



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