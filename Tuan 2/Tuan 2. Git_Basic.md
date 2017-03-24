# Basic Git


## Git là gì

### Version Control

Version Control là một hệ thống để lưu lại thay đổi của các file hoặc hệ thống file theo thời gian để bạn có thể gọi lại ( khôi phục lại) một phiên bản trước đó. Version Control System là một hệ thống cực kỳ thông minh giúp bạn làm việc đó. VCS cho phép bạn khôi phục lại một file về phiên bản trước đó, khôi phục cả dự án về phiên bản trước đó, so sánh sự thay đổi theo thời gian của từng file cũng như cả dự án, theo dõi xem ai là người thay đổi cuối cùng và nhiều hơn thế nữa.

#### Local Version Control System

Đa số mọi người quản lý phiên bản bằng cách copy file vào một thư mục khác để lưu trữ (Có thể đánh dấu theo thời gian). Nó là một cách làm rất thông dụng bởi nó đơn giản nhưng nó dễ gặp lỗi.

Để tránh những lỗi có thể do cách làm trên các lập trình viên đã phát triển Local VCSs, một kho dữ liệu đơn giản để lưu trữ tất cả các thay đổi dưới sự kiểm soát thay đổi.

![Local VCS](https://raw.githubusercontent.com/NTT-TNN/Basic_knowledge/master/images/Local%20VCS.PNG)

##### VCS Tập trung

Một vấn đề mà các lập trình viên thường gặp phải ngoài việc lưu trữ các phiên bản là hợp tác cùng làm việc với lập trình viên trong một dự án. Và VCS tập trung được phát triển để giải quyết vấn đề này. Hệ thống có một server để duy trì các phiên bản của file và một số người dùng để kiểm tra file. Những năm gần đây VCS tập trung đã trở thành chuẩn của VCS.