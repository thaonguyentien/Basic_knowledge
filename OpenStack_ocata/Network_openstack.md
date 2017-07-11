# Openstack Networking(Neutron)

Openstack networking cho phép bạn tạo và quản lý các đối tượng của mạng như networks, subnets và port để cung cấp cho các dịch vụ khác của openstack sử dụng.

Network service(neutron) cung cấp API cho phép bạn định nghĩa cách kết nối các mạng và đánh địa chỉ trong cloud.

## Giới thiệu về linux bridge plugin

Linux bridge là một switch ảo. Tuy nhiên với chức năng của một switch cơ bản, một mình linux bridge là không đủ để xây dựng một hệ thống mạng phức tạp như VLAN, VXLAN. Do đó, khi xây dựng hệ thống mạng trong OpenStack có sử dụng Linux Bridge plugin, Neutron sẽ kết hợp các Linux bridge với các loại thiết bị ảo khác và cả các thiết bị phần cứng để tạo nên hệ thống mạng ảo.

Linux bridge trong openstack hỗ trợ các loại mạng cục bộ là:

- Flat
- VLAN
- VXLAN

### Mạng Flat

Khi triển khai mạng Flat sẽ có một bridge ảo(brqXXXX) được tạo ra trên mỗi node và được kết nối trực tiếp đến card mạng vật lý. Tại mỗi node các máy ảo tạo ra các card mạng ảo(tapN) và kết nối tới bridge ảo để kết nối với mạng Flat. Ta thấy mỗi card mạng vật lý chỉ có thể tạo một mạng Flat do vậy nếu muốn tạo ra bao nhiêu mạng Flat ta cần có bấy nhiêu card vật lý.

![Flat](https://raw.githubusercontent.com/NTT-TNN/Basic_knowledge/master/images/neutron/linuxbridge_flat.png)

### Mạng VLAN

Để triển khai mạng VLAN bằng Linux Bridge plugin, Linux Bridge sẽ kết hợp với thiết bị VLAN-interface ảo có tên là ethx.VLAN_ID trong đó VLAN_ID là ID của mạng VLAN. Mỗi một mạng VLAN sẽ có một Linux bridge và một VLAN-Device. Các máy ảo thuộc cùng một mạng VLAN trên cùng một node sẽ kết nối card mạng ảo của máy mình với Linux bridge quản lý VLAN đó và linux bridge sẽ được kết nối tới VLAN-Device để thực hiện chức năng như một switch vật lý trong mạng VLAN.

Linux bridge + VLAN-Devide = Switch VLAN trong mạng vật lý.

Luồng của các L2 frame sẽ như sau:

- Khi cần chuyển tiếp một gói tin L2 Frame từ một máy ảo qua một máy khác cùng thuộc VLAN nhưng thuộc node khác, Linux bridge sẽ chuyển tiếp gói tin đó qua VLAN-Device. VLAN-Device sẽ đóng thêm VLAN Header với ID là ID của mạng VLAN rồi chuyển tiếp ra mạng vật lý qua card vật lý eth1

- Khi tiếp nhận một gói tin L2 Frame từ mạng vật lý bên ngoài, gói tin này sẽ đi qua card eth1 vào các VLAN-Device. Các VLAN-Device sẽ kiểm tra VLAN ID của gói tin này, nếu gói tin này có VLAN ID hợp lệ, VLAN-Device sẽ loại bỏ phần VLAN header và chuyển L2 Frame tới Linux Bridge. Linux Bridge sẽ kiểm tra địa chỉ MAC đích rồi forward gói tin L2 Frame tới cổng kết nối với máy có MAC đích.

- Khi chuyển tiếp giữa các máy VLAN cùng nằm trong 1 node, Linux bridge hoạt động như một switch bình thường (không cần các hoạt động gắn-bỏ VLAN Header).

![vlan](https://raw.githubusercontent.com/NTT-TNN/Basic_knowledge/master/images/neutron/neutron_vlan.png)

### Mạng VXLAN

Để triển khai mạng VXLAN bằng Linux Bridge plugin, các linux bridge sẽ kết hợp với VXLAN-Device để thực hiện các chức năng của một thiết bị VTEP. VXLAN-Device được đặt tên tương ứng với ID của mạng VXLAN mà nó được triển khai.

## Các kịch bản thường dụng với linuxbridge

### Provider Network

Kiến trúc mạng provider network cung cấp kết nối layer-2 giữa các instance và physical network.

![linux_provider](https://raw.githubusercontent.com/NTT-TNN/Basic_knowledge/master/images/neutron/linux_bridge_provide.png)

### Network traffic flow trong provider network

Giả sử cấu hình các instance và các network như sau:

- Provider network 1 (VLAN)
    -  VLAN ID 101 (tagged)
    - IP address ranges 203.0.113.0/24 and fd00:203:0:113::/64
    - Gateway (via physical network infrastructure)
        - IP addresses 203.0.113.1 and fd00:203:0:113:0::1
- Provider network 2 (VLAN)
    - VLAN ID 102 (tagged)
    - IP address range 192.0.2.0/24 and fd00:192:0:2::/64
    - Gateway
        - IP addresses 192.0.2.1 and fd00:192:0:2::1
- Instance 1
    - IP addresses 203.0.113.101 and fd00:203:0:113:0::101
- Instance 2
    - IP addresses 192.0.2.101 and fd00:192:0:2:0::101

#### Thường hợp 1: Instance gửi packet ra internet

- B1. Instance interface(1) chuyển đến provider instance port(2)
- B2. Security group rules (3) trên the provider bridge
 xử lý firewalling and theo dõi kết nối cho gói tin.
- B3. The VLAN sub-interface port (4) trên the provider bridge chuyển gói tin tới the physical network interface (5).
- B4. The physical network interface (5) thêm vào VLAN tag 101 cho packet và chuyển nó tới physical network infrastructure switch (6).
- B5. The switch loại bỏ VLAN tag 101 trong goi gin và chuyển nó tới router(7).
- B6. The router  định tuyến gói tin từ provider network(8) tới external network(9) và chuyển gói tin tới switch(10).
- B7. The switch chuyển tiếp gói tin tới external network (11).
- B8. The external network (12)  nhận được packet.

![provider_us1](https://raw.githubusercontent.com/NTT-TNN/Basic_knowledge/master/images/neutron/provider_us1.png)

#### Thường hợp 2: Instance packet tới instance khác thuộc cùng một network

Cụ thể:

- Instance 1 đặt otại  compute node 1 và sử dụng provider network 1
- Instance 2 đặt tại on compute node 2 và sử dụng provider network 1.
- Instance 1 gửi packet tới instance 2.

- B1. The instance 1 interface (1) chuyển gói tin tới provider bridge instance port (2).
- B2. Security group rules (3) treen the provider bridge xử lý firewalling và theo dõi kết nối cho gói tin.
- B3.The VLAN sub-interface port (4) trên provider bridge chuyển gói tin tới the physical network interface (5).
- B4. The physical network interface (5) thêm VLAN tag 101 vào gói tin và chuyển tiếp tới  physical network infrastructure switch (6).
- B5. The switch chuyển tiếp gói tin từ compute node 1 tới compute node 2 (7).
- B6. The physical network interface (8) loại bỏ VLAN tag 101 khỏi gói tin và chuyển tiếp tới VLAN sub-interface port (9) trên the provider bridge.
- B7. Security group rules (10) trên the provider bridge xử lý firewalling và theo dõi kết nối cho gói tin.
- B8. The provider bridge instance port (11) chuyển tiếp gói tin tới the instance 2 interface (12).

![provider_us2](https://raw.githubusercontent.com/NTT-TNN/Basic_knowledge/master/images/neutron/provider_us2.png)

#### Thường hợp 3: Instance packet tới instance khác thuộc hai network

Cụ thể:

- Instance 1 đặt tại on compute node 1 và sử dụng provider network 1.
- Instance 2 đặt tại on compute node 1 và sử dụng provider network 2.
- Instance 1 gửi a packet tới instance 2.

- B1. The instance 1 interface (1) chuyển gói tin tới provider bridge instance port (2).
- B2. Security group rules (3) treen the provider bridge xử lý firewalling và theo dõi kết nối cho gói tin.
- B3.The VLAN sub-interface port (4) trên provider bridge chuyển gói tin tới the physical network interface (5).
- B4. The physical network interface (5) thêm VLAN tag 101 vào gói tin và chuyển tiếp tới  physical network infrastructure switch (6).
- B5. The switch lọa bỏ VLAN tag 101 khỏi gói tin và chuyển tiếp gói tin tới router (7).
- B6. The router định tuyến gói tin từ provider network 1 (8) tới provider network 2 (9).
- B7. The router chuyển tiếp gói tin tới switch (10).
- B8. The switch thêm VLAN tag 102 vào gói tin và chuyển tiếp gói tin tới compute node 1 (11).
- B9. The physical network interface (12) lọa bỏ VLAN tag 102 khỏi gói tin và chuyển gói tin đó tới  VLAN sub-interface port (13) trên the provider bridge.
- B10.Security group rules (14) trên the provider bridge xử lý firewalling và theo dõi kết nối cho gói tin.
- B11. The provider bridge instance port (15) chuyển tiếp gói tin tới instance 2 interface (16).

![provider_us3](https://raw.githubusercontent.com/NTT-TNN/Basic_knowledge/master/images/neutron/provider_us3.png)