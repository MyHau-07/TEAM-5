from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import DichVu, GioHang
from django.views.decorators.csrf import csrf_exempt
from .models import Work_Schedule
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
    
    return redirect('giohang')  # Quay lại trang giỏ hàng hoặc trang phù hợp



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
def giohang(request):
    gio_hang_items = GioHang.objects.filter(user=request.user)
    total_price = sum(item.dich_vu.gia * item.so_luong for item in gio_hang_items)
    
    return render(request, 'Pages/giohang.html', {
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
#chu phong kham
def ClicnicOwner (request):
    return render(request, 'Pages/ClicnicOwner.html')
#quan li phong kham
def hosophongkham (request):
    return render(request, 'Pages/ho-so-phong-kham.html') 
#quan li chi nhanh
def quanlichinhanh (request):
    return render(request, 'Pages/quan-li-chi-nhanh.html') 
#quan li nhan vien
def quanlinhanvien (request):
    return render(request, 'Pages/quan-li-nhan-vien.html') 
#quanlidichvu
def quanlidichvu (request):
    return render(request, 'Pages/quan-li-dich-vu.html') 

def dichvu(request):
    dich_vu_list = DichVu.objects.all()
    return render(request, 'Pages/dichvu.html', {'dich_vu_list': dich_vu_list})


def user (request):
    return render(request, 'Users/user.html')

# def giohang (request):
#     return render(request, 'Pages/giohang.html')

def news (request):
    return render(request, 'Pages/news.html')

def booking (request):
    return render(request, 'Pages/booking.html')

def Dentist (request):
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

def myuudai (request):
    return render(request, 'Users/myuudai.html')

#----left menu
# def dichvu (request):
#     return render(request, 'Pages/dichvu.html')

def uudai (request):
    return render(request, 'Pages/uudai.html')

def sukien (request):
    return render(request, 'Pages/sukien.html')  

def kienthuc (request):
    return render(request, 'Pages/kienthuc.html')
#left menu---