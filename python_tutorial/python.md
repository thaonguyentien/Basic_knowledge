# Python tutorial

## Python là gì?

Python là một ngôn ngữ lập trình hướng đối tượng, ngôn ngữ lập trình bậc cao.

Đặc điểm của ngôn ngữ lập trình python:

- Python là ngôn ngữ thông dịch(interpreferd): Điều này có nghĩa là các đoạn code của python sẽ được xử lý bởi trình thông dịch tại thời điểm chạy. Chương trình không cần được biên dịch trước khi chạy.
- Python là ngôn ngữ lập trình hướng đối tượng
- Python là ngôn ngữ phù hợp cho người mới bắt đầu lập trình. Python hỗ trợ từ phát triển các ứng dụng từ xử lý văn bản đơn giản tới phát triển các ứng dụng web tới phát triển các trò chơi.

## Quy ước định danh trong python

- Định danh trong python bắt đầu bởi một chữ cái thường hoặc in hoa hoặc một dấu gạch dưới(_) và theo sau là các chữ cái, dấu gạch dưới hoặc số. Python không cho phép sử dụng các kỹ tự đặc biệt như: @,$ và % trong định danh. Pyhton phân biệt chữ thường và chữ in hoa trong định danh nên Abc và abc là hai định danh hoàn toàn khác nhau.

- Một số quy ước về định danh trong python:

    - Tên của lớp bắt đầu bằng một chữ cái in hoa các ký tự đi sau là các ký tự viết thường.
    - Một định danh bắt đầu với dấu gạch dưới(_) dùng cho định danh có phạm vi sử dụng là riêng tư.

## Blocks of code

Khác với một số các ngôn ngữ lập trình khác sử dụng dấu ngoặc nhọn({}) để xác định các blocks of code cho các lớp, hàm ,hay các luồng điều khiển. Python sử dụng thụt đầu dòng để xác định blocks of code.

Số lượng các khoảng trắng(spaces) là không cố định nhưng các câu lệnh cùng thuộc một block thì cần có số lượng khoảng trắng như nhau. Ví dụ:

```py
if True:
    print "Answer"
    print "True"
else:
    print "Answer"
```

## Câu lệnh nhiều dọng trong python

Thông thường mỗi câu lệnh trong python được viết trên một dòng nhưng python cũng cho phép viết một câu lệnh trên nhiều dòng và sử dụng ký tự \ để nối câu lệnh như ví dụ sau:

```py
thao = thao1 + \
        thao2
```

 sẽ tương đương với câu lệnh
`thao=thao1 + thao2`

Chú ý: Các câu lệnh có sử dụng [],{} hoặc () không cần sử dụng ký tự \ để có thể viết trên nhiều dòng ví dụ sau vẫn hợp lệ:

```py
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
```

### Quotation in Python

Python cho phép sử dụng dấu nháy đơn('), dấu nháy kép("), và dấu nháy ba(''' hoặc """) để xác định một xâu, miễn là dấu dùng để bắt đầu và kết thúc là cùng loại ví dụ:

```py
'hello world' # Đúng cú pháp
'hello world" # Sai cú pháp
```

### Chú thích trong python

Ta sử dụng ký hiệu # để xác định chú thích trong python. Tất cả các ký tự từ ký tự # cho đến hết dòng đó sẽ trở thành chú thích.

Ví dụ:

```py
print "Hello, Python!" # this is comment
# this is comment

```

### Function trong python

Tham số được truyền vào các function trong python dưới dạng tham chiếu. Có nghĩa là những thay đổi với tham số ở bên trong function sẽ cũng làm thay đổi giá trị của tham số ở bên ngoài function ví dụ:


```py
#!/usr/bin/python

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist
```

Output :

```py
Values inside the function:  [10, 20, 30, [1, 2, 3, 4]]
Values outside the function:  [10, 20, 30, [1, 2, 3, 4]]
```

#### Function argument

- Required arguments: là tham số truyền vào trong function theo đúng thứ tự vị trí. Ví dụ khi hàm printme() được gọi đến nó xác định là phải có một tham số truyền vào nếu ngược lại có lỗi xảy ra như ví dụ sau:

```py
#!/usr/bin/python

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print str
   return;

# Now you can call printme function
printme()

```

Output:

```
Traceback (most recent call last):
  File "test.py", line 11, in <module>
    printme();
TypeError: printme() takes exactly 1 argument (0 given)
```