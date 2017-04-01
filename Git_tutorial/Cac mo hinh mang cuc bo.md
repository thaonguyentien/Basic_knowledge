# Các mô hình mạng cục bộ

## VLANs

VLAN(virtual LAN) là một kỹ thuật cho phép chia một miền quảng bá vật lỳ thành các mạng cục bộ độc lập nhau. Mỗi mạng VLAN được đặc trưng bởi một định danh là VLAN ID.

Cụ thể xét hình bên dưới:

![VLAN1](https://raw.githubusercontent.com/NTT-TNN/Basic_knowledge/master/images/VLAN2.png)

Cả 6 máy A,B,C,D,E,F cùng kết nối vào một switch nhưng nằm ở hai mạng VLAN khác nhau. Nếu máy A gửi gói tin quảng bá thì chỉ những máy trong cùng một mạng VLAN (B,C) nhận được gói tin đó.

Để các máy D,E,F có thể nhận được gói tin quảng bá từ máy A(khác VLAN) cần có một router. Máy A sẽ gửi gói tin lên router và router sẽ gửi gói tin xuống cho các máy D,E,F qua switch.

## Flat

## VXLAN
