# An toàn và bảo mật thông tin

## Chương 1. Các khái niệm cơ sở và hệ mã cổ điển

Câu 1: Phân biệt các thuật ngữ cryptography, cryptanalysis, cryptology. "Khoa học mật mã" tương ứng với từ tiếng anh nào?

Trả lời:

- cryptography(sinh, chế mật mã): nghiên cứu các kỹ thuật toán học nhằm cung cấp các công cụ hay dịch vụ đảm bảo an toàn thông tin.
- cryptanalysis(phá giải mã): nghiên cứu các ký thuật toán học nhằm phục vụ phân tích mật mã và tạo ra các đoạn mã giả nhằm đánh lừa bên nhận.
- cryptology(ngành mật mã): thường được quan niệm là sự kết hợp của hai ngành cryptography và cryptanalysis.

Khoa học mật mã tương ứng với từ :cryptography

Câu 2: Trong thời kỹ nào kỹ thuật mật mã chưa được coi là ngành khoa học? tại sao?

Trả lời: Thời kỳ tính từ thượng cổ cho đến năm 1949 kỹ thuật mật mã chưa được coi là ngành khoa học. Vì trong thời kỹ này ngành này còn mang nhiều tính thủ công, kỹ thuật hơn là tính khoa học.

Câu 3: Hãy phân biệt các hệ mã thông thường(Morse Code, ASCII code) với các hệ mật mã?

Trả lời:

Đối với các hệ mã thông thương(Morse Code, ASCII code) một đoạn văn bản sau A sau khi mã hóa thành văn bản B thì bất kỳ một người nào iết văn bản đó được mã hóa bằng thuật toán nào(ví dụ: Morse Code, ASCII code) đều có thể từ văn bản B mà tìm ra văn bản A. Còn đối với hệ mật mã một người mặc dù có văn bản B và biết thuật toán mã hóa nhưng nếu không biết khóa sẽ không thể suy ra được văn bản A.

Ví dụ:

- Đối với hệ mã ASCII Code: Nếu một người nhận được đoạn văn bản `97 110 32 116 111 97 110 32 98 97 111 32 109 97 116 32 116 104 111 110 103 32 116 105 110` người đó dễ dàng giải mã được chuỗi thông tin `an toan bao mat thong tin`.
- Đối vơi hệ mật mã afine cipher: Nếu một người nhận được đoạn văn bản `wj pkwj xwk iwp pdkjc pej` nếu người đó không biết khóa là (1,4) thì người đó sẽ không thể giải mã ra chuỗi tin ban đầu là `an toan bao mat thong tin` mặc dù người đó biết đoạn mã được mã hóa bằng hệ mã afine cipher.

Câu 4: 


