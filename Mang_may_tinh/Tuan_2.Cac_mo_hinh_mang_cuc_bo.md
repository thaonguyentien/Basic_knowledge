# Các mô hình mạng cục bộ

Báo cáo sẽ đi tìm hiểu chi tiết về bốn loại mạng cục bộ được sử dụng trong thực tế là:

1. Flat
1. VLAN
1. VXLAN
1. GRE

## Flat

Mạng flat là một mạng không cung cấp bất kỳ một tùy chọn thêm nào. Nó là mạng truyền thống được sử dụng ở Layer2. Mạng flat không phân đoạn và tách làm các khu vực quảng bá khác nhau bằng cách sử dụng router. Nói chung là tất cả các thiết bị trong một mạng flat có cùng một miền quảng bá.


## VLAN(virtual LAN)

VLAN là một kỹ thuật cho phép tạo các mạng LAN độc lập một cách login trên cơ sở cùng một kiến trúc hạ tầng vật lý. Việc sử dụng VLAN giúp tạo ra nhiều miền quảng bá độc lập.

Có 3 Loại VLAN:

- VLAN dựa trên cổng: Mỗi cổng được gắn với một VLAN xác định. Có nghĩa là thiết bị nào kết nối tới cổng đó sẽ thuộc một VLAN xác định. Đây là loại VLAN đơn giản và phổ biến nhất.
- VLAN dựa trên địa chỉ MAC: Mỗi địa chỉ MAC được gắn vào một VLAN nhất định cách này khó khăn trong việc quản lý.
- VLAN dựa trên giao thức: Tương tự như dựa trên địa chỉ MAC nhưng sử dụng địa chỉ IP thay cho MAC. Loại này không được thông dụng.

Vậy tại sao đã có mạng flat lại cần thêm mạng VLAN. Mạng VLAN có ưu nhược điểm là gì?

- Tiết kiệm băng thông mạng: Do VLAN chia mạng LAN thành các mạng quảng bá nhỏ nên khi một gói tin quảng bá được gửi đi nó chi được gửi trong một mạng VLAN duy nhất, không truyền đến các VLAN khác nên tiết kiệm được băng thông đường truyền.
- Tăng tính bảo mật: Các VLAN có các mạng quảng bá khác nhau không truy cập được vào nhau trừ khi có khai báo định tuyến.
- Dễ dàng thêm bớt các máy vào VLAN

Sự khác nhau giữa gói tin của LAN và VLAN

tiếp theo wiki



