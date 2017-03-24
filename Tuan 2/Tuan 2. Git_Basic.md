# Basic Git


## Git là gì

### Version Control

Version Control là một hệ thống để lưu lại thay đổi của các file hoặc hệ thống file theo thời gian để bạn có thể gọi lại ( khôi phục lại) một phiên bản trước đó. Version Control System là một hệ thống cực kỳ thông minh giúp bạn làm việc đó. VCS cho phép bạn khôi phục lại một file về phiên bản trước đó, khôi phục cả dự án về phiên bản trước đó, so sánh sự thay đổi theo thời gian của từng file cũng như cả dự án, theo dõi xem ai là người thay đổi cuối cùng và nhiều hơn thế nữa.
Sử dụng VCS đồng nghĩa với việc bạn có thể thay đổi các file một các thoải mái và dễ dàng có thể quay trở lại phiên bản trước đã commit một cách dễ dàng.

#### Local Version Control System

Đa số mọi người quản lý phiên bản bằng cách copy file vào một thư mục khác để lưu trữ (Có thể đánh dấu theo thời gian). Nó là một cách làm rất thông dụng bởi nó đơn giản nhưng nó dễ gặp lỗi. Bạn sẽ rất dễ quên rằng mình đang ở trong thư mục nào hay vô tính chỉnh sửa file hoặc chép nhầm file mà bạn không mong muốn.

Để tránh những lỗi có thể do cách làm trên các lập trình viên đã phát triển Local VCSs, một kho dữ liệu đơn giản để lưu trữ tất cả các thay đổi dưới sự kiểm soát thay đổi.

![Local VCS](https://raw.githubusercontent.com/NTT-TNN/Basic_knowledge/master/images/Local%20VCS.PNG)

##### VCS Tập trung

Một vấn đề mà các lập trình viên thường gặp phải ngoài việc lưu trữ các phiên bản là hợp tác cùng làm việc với lập trình viên trong một dự án. Và VCS tập trung được phát triển để giải quyết vấn đề này. Hệ thống có một server để duy trì các phiên bản của file và danh sách các người dùng có quyền thay đổi các file trên hệ thống tập trung đó. Những năm gần đây VCS tập trung đã trở thành chuẩn của VCS.
![VCS tập trung](https://raw.githubusercontent.com/NTT-TNN/Basic_knowledge/master/images/VCS%20t%E1%BA%ADp%20trung.PNG)

Mô hình này cung cấp rất nhiều lợi thế so với việc quản lý cục bộ. Cụ thể là người dùng có thể biết một phần nào đó của những việc người khác đang làm trong dự án. Người quản lý dự án có quyền quản lý ai có thể làm gì theo ý muốn.

Bên cạnh đó hệ thống cũng có những bất cập nhất định. Cụ thể như sự cố khi máy chủ tập trung gặp phải. Ví dụ như nếu máy chỉ bị sập thì các người dùng không thể cộng tác với những người dùng khác. Nếu ổ cứng chưa dữ liệu tập trung bị hỏng và các sao lưu dự phòng chưa được thực hiện tới thời điểm đó và người dùng sẽ mất toàn bộ dữ liệu của dự án đó ngoại trừ các phiên bản đã được lưu cục bộ trên máy của mỗi người.

#### VCS Phân tán (Distributed Version Control Systems DVCS)

Trong các DVCS các máy khách không chỉ sao chép về máy cục bộ các phiên bản mới nhất của các tệp tin mà sao chép toàn bộ repository. Điều này giúp cho khi máy chủ quản lý phiên bản bị sập thì bất kỳ máy khách nào cũng có thể dùng để sap chép ngược lại để khôi phục lại hệ thống.

![DVCS](https://raw.githubusercontent.com/NTT-TNN/Basic_knowledge/master/images/DVCS.PNG)

### Git cơ bản

#### Điểm khác biệt giữa Git và các VCS khác :

- Các hệ thống VCS khác mỗi khi người sử dụng commit VCS sẽ lưu lại toàn bộ các file. Còn với Git hệ thống sẽ lưu lại một **ảnh chụp(snapshot)** các file. Với những file đã thay đổi git sẽ tạo một phiên bản mới còn với những file không thay đổi git sẽ ánh xạ file đó vào file cũ đã không thay đổi.
- Phần lớn các thao tác trên git diễn ra cục bộ: Điều này có nghĩa là người dùng có thể thay đổi và commit thay đổi của mình ngay cả khi không có kết nối với mạng. Sau khi người dùng kết nối với mạng git sẽ tự đồng bộ với hệ thông. Điều này giúp người dùng có thể làm việc trong điều kiện không có kết nối internet.

#### Ba trạng thái của Git

Mỗi tệp tin trong git được quản lý dựa trên 3 trạng thái:

- Modified: Trạng thái tệp tin đã thay đổi nhưng chưa được commit và cơ sở dữ liệu.
- Staged : Trạng thái bạn đã đánh dấu là sẽ commit phiên bản hiện tại vào lần commit sắp tới.
- Committed: Trạng thái dữ liệu đã được lưu trữ an toàn trong cơ sở dữ liệu