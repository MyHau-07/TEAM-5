from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser
from home.forms import CustomUserForm
from home.forms import BookingForm
from .models import Appointment
from .models import GioHang
from .models import Services
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
# Create your views here.

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
    total_price = sum(item.dich_vu.gia * item.so_luong for item in gio_hang_items)
    
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

        # Xóa các mục trong giỏ hàng (giả lập thanh toán thành công)
        gio_hang.delete()
        messages.success(request, 'Thanh toán thành công!')

        return redirect('trang_chu')

    return redirect('xem_gio_hang')

def news (request):
    return render(request, 'Pages/news.html')

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Đặt lịch thành công! Thông tin đã được gửi đến quản trị viên.")
            return redirect('success_page')  # Điều hướng sau khi đặt lịch thành công
        else:
            messages.error(request, "Có lỗi xảy ra, vui lòng kiểm tra lại thông tin.")
    else:
        form = BookingForm()
    return render(request, 'Pages/booking.html', {'form': form})

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

def lichsu (request):
    return render(request, 'Users/lichsu.html')

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