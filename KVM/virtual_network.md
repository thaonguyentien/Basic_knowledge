# virtual network

## 1. Virtual network switches

 virtual network switch là một phần mềm hoạt động trên một máy chủ vật lý giúp cho các máy ảo(guests)kết nối.

## 2. Bridged Mode

Khi sử dụng chế độ bridged mode toàn bộ các máy ảo sẽ ở trong cùng một subnet như máy chủ vật lý. Tất cả các máy chủ vật lý khác có thể  biết được sự xuất hiện của các máy ảo đó trong mạng và có thể truy cập vào các máy ảo đó. Chế độ này họat động trên layer2 trong mô hình OSI.

Các trường hợp sử dụng:
- Triển khai các máy ảo trong một mạng với các máy chủ vật lý làm cho sự khác biệt giữa máy vật lý và máy ảo là trong suốt với người dùng.
- Triển khai các máy ảo mà không muốn thực hiện bất kỳ thay đổi cấu hình nào với các máy vật lý hiện có.
  - Triển khai các máy ảo có thể dễ dàng truy cập vào các máy chú vật lý hiện có.
## 3. NAT mode

Đây là chế độ mặc định cho virtual network switches. Chúng sử dụng ip ảo(IP masquerading). Địa chỉ IP này cho phép máy ảo sử dụng địa chỉ IP của máy chủ vật lý để giao tiếp với bất kỳ mạng bên ngoài nào. Mặc định máy tính nào ở bên ngoài máy chủ vật lý sẽ không thể giao tiếp với máy ảo trong chế dộ NAT mode.

### 3.1 DNS và DHCP

Địa chỉ IP có thể được gán cho máy ảo thông qua DHCP. Một tập các địa chỉ IP có thể được gán cho các virtual network switch . Libvirt sử dụng chương trình `dnsmasq` để thực hiện việc này. Chương trình này sẽ tự động cấu hình cho mỗi virtual network switch khi cần.

## 4. Routed mode

Trong chế độ này máy chủ vật lý họat động như một router cho phép các máy bên ngoài giao tiếp với máy ảo thông qua địa chỉ IP. Virtual switch có thể xem xét toàn bộ thông tin đi qua và sử dụng thông tin trong các packet để đưa ra quyết định định tuyến. Trong chế độ này các máy ảo đề thuộc cùng một mạng con và được định tuyến thông qua một virtual switch. Chế độ này không phải lúc nào cũng là lý tưởng vì các máy chủ vật lý khác trong cùng một mạng vật lý sẽ không thể biết về các máy ảo nếu không được cấu hình router bằng tay và do đó không thể giao tiếp với máy ảo. Chế độ routed hoạt động ở trên layer3 trong mô hình OSI.



## 5. Isolated mode

Khi sử dụng chế dộ isolated máy ảo có thể giao tiếp với nhau và giao tiếp với máy chủ vật lý nhưng chúng không thể giao tiếp với các máy chủ bên ngoài máy chủ vật lý(cả vào và ra đều không thể). Sử dụng dnsmasq là bắt buộc cho những chức năng như DHCP. Tuy nhiên ngay cả khi bị cô lập với tất cả các mạng vật lý các tên DNS vẫn được giải quyết(resolved). Do đó một tình huống xảy ra khi các tên DNS được giải quyết nhưng các yêu cầu ICMP (ping) lại bị lỗi.
