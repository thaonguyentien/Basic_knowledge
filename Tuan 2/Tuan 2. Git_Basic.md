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

#### Điểm khác biệt giữa Git và các VCS khác

- Các hệ thống VCS khác mỗi khi người sử dụng commit VCS sẽ lưu lại toàn bộ các file. Còn với Git hệ thống sẽ lưu lại một **ảnh chụp(snapshot)** các file. Với những file đã thay đổi git sẽ tạo một phiên bản mới còn với những file không thay đổi git sẽ ánh xạ file đó vào file cũ đã không thay đổi.
- Phần lớn các thao tác trên git diễn ra cục bộ: Điều này có nghĩa là người dùng có thể thay đổi và commit thay đổi của mình ngay cả khi không có kết nối với mạng. Sau khi người dùng kết nối với mạng git sẽ tự đồng bộ với hệ thông. Điều này giúp người dùng có thể làm việc trong điều kiện không có kết nối internet.

#### Ba trạng thái của Git

Mỗi tệp tin trong git được quản lý dựa trên 3 trạng thái:

- Modified: Trạng thái tệp tin đã thay đổi nhưng chưa được commit và cơ sở dữ liệu.
- Staged : Trạng thái bạn đã đánh dấu là sẽ commit phiên bản hiện tại vào lần commit sắp tới.
- Committed: Trạng thái dữ liệu đã được lưu trữ an toàn trong cơ sở dữ liệu

Tương ứng với ba trạng thái là ba phần riêng biệt của một dự án sử dụng Git:

- Thư mục git : Tương ứng với trạng thái commit. Nơi lưu trữ các metadata và cơ sở dữ liệu của dự án. Là phần được sao lưu về khi bản clone một dự án.
- Khu vực tổ chức(staging area): Tương ứng với trạng thái staged. B
- Thư mục làm việc: Tương ứng với trạng thái modified. Bản sao một phiên làm việc của dự án. Những tệp tin được pull về từ cơ sở dữ liệu và lưu trong ổ cứng để có thể sử dụng và chỉnh sủa.

![Ba trạng thái Git](https://raw.githubusercontent.com/NTT-TNN/Basic_knowledge/master/images/Ba%20tr%E1%BA%A1ng%20th%C3%A1i%20Git.PNG)

Tiến trình công việc cơ bản của Git:

- Bạn thay đổi các tệp tin trong thư mục làm việc. Trạng thái modified
- Bạn tổ chức các tệp tin, tạo ảnh mới của tệp tin đó vào thư mục staged. Trạng thái stagad. Tương ứng với câu lênh : "Git add`
- Bạn commit ảnh của các tệp tin trong khu vực staged sẽ được lưu trữ vĩnh viện vào thư mục git. Tương ứng với câu lệnh :`Git commit -m "status"`

## Cơ bản về git

### Tạo một kho chứ git

Có hai cách để tạo một kho chứ git

- Tạo kho chứa từ thư mục cũ
- Sao chép một kho chứa đã tồn tại

#### Tạo kho chứa từ một thư mục cũ

Nếu bạn đang có một thư mục chứa dự án mà bạn muốn theo dõi dự án này trong git. Bạn gõ lệnh sau vào terminal tại thư mục chứa dự án đó.

`$ git init`

Lệnh này tạo ra một thư mục mới có tên `.git` thư mục này chưa tất cả các tệp tin cần thiết cho kho chứa git. Bây giờ chưa hề có gì trong dự án của bạn được theo dõi hết.

Nếu bạn muốn kiểm soát phiên bản cho các tệp tin sẵn có bạn nên thiết lập theo dõi các tệp tin đó và thực hiện commit lần đầu tiên. Để có thể theo dõi tệp tin bạn sử dụng lệnh `git add`
. Để có thể commit những thay đổi bạn có thể sử dụng lệnh : `git commit -m "các thay đổi"`

#### Sao chép một kho chứa đã tồn tại

Nếu như bạn muốn sao chép một bản sao của một kho chứa đã có sẵn ví dụ như dự án bạn muốn đóng gói vào bạn cần sử dụng câu lệnh :`git clone url`
ví dụ:` git clone https://github.com/NTT-TNN/Basic_knowledge.git
`
Sau đó thư mục chứa kho dữ liệu bạn sao chép sẽ được lưu tại thư mục bạn thực hiện câu lệnh.

#### Ghi lại thay đổi vào kho chứa

Bạn đã tạo được một kho chứa và bản sao dữ liệu để làm viêc. Bây giờ bạn sẽ làm việc trên bản sao đó và một khi đạt đến một trạng thái nào mà bạn muốn lưu vào ghi lại bạn sẽ cần commit chúng vào kho chứa.

Mỗi tệp tin trong thư mục làm việc của bạn sẽ có thể ở một trong hai trạng thái:

- Tracked: là tệp tin đã có trong danh sách theo dõi trước. Chúng có thể ở một trong ba trạng thái: Modified, unmodified và staged.
- Untracked: Các file còn lại. Cụ thể là các file trong thư mục làm việc mà không có ảnh(lần commit) trước hoặc các file không thuộc vùng staging. Ban đầu khi bạn clone một kho chứa về tất cả các file sẽ ở trạng thái tracked và unmodified vì bạn mới tải chúng về và chưa thực hiện thay đổi nào.

Khi bạn chỉnh sửa các tệp tin chúng sẽ chuyển sang trạng thái modified sau đó nếu bạn muốn commit các tệp tin đó bạn cần đưa chúng vào khu vực stage và thực hiện commit. Cứ như vậy lặp lại.
