# Docker command

## 1. Cài đặt docker

## 2. Các lệnh cơ bản trong docker

### 2.1 Hiển thị help

Để hiển thị help của bất kỳ câu lệnh nào của docker ta chỉ cần thêm --help vào sau câu lệnh đó.

Ví dụ:

thao-nt@thao-nt:~$ docker attach --help

Usage:	docker attach [OPTIONS] CONTAINER

Attach local standard input, output, and error streams to a running container

```sh
thao-nt@thao-nt:~$ docker attach --help

Usage:	docker attach [OPTIONS] CONTAINER

Attach local standard input, output, and error streams to a running container

Options:
      --detach-keys string   Override the key sequence for detaching a container
      --help                 Print usage
      --no-stdin             Do not attach STDIN
      --sig-proxy            Proxy all received signals to the process (default true)

```


Chú ý: Các câu lệnh của docker thường được sử dụng cùng với các tham số khác nhau và các tham số này có thể combined lại với nhau thành một tham số.

Ví dụ:

`thao-nt@thao-nt:~$ docker run -d -i -t --name thao-test weshop_web:latest`

Cũng tương tự với câu lệnh:

`thao-nt@thao-nt:~$ docker run -dit --name thao-test weshop_web:latest `

### 2.2 Build image từ Dockerfile

`docker build [OPTIONS] PATH | URL | -`

Các options thường dùng là:

- --file,-f  : Tên của Dockerfile (Mặc định là 'PATH/Dockerfile')
- --tag,-t   : Name và một tag optionally theo format: 'name:tag'

Ví dụ:

`docker build -t thao-nt:v1 .`

### 2.3 Liệt kê danh sách các images

`docker images [OPTIONS] [REPOSITORY[:TAG]]`

Các options thường dùng là:

- --all,-a: Hiển thị tất cả các images

Ví dụ:

```sh
thao-nt@thao-nt:~$ docker images -a
REPOSITORY                TAG                 IMAGE ID            CREATED             SIZE
weshop_web                latest              46d1bbdd8aff        22 hours ago        726MB
<none>                    <none>              9e0eea4b8479        22 hours ago        717MB
<none>                    <none>              968aa575d81a        22 hours ago        673MB
<none>                    <none>              1c8fddac7655        22 hours ago        673MB
<none>                    <none>              92c96cb12ab4        22 hours ago        673MB
<none>                    <none>              850109f481c9        22 hours ago        673MB
<none>                    <none>              fa8e55b2235d        6 days ago          673MB
ubuntu                    16.04               14f60031763d        10 days ago         120MB
ubuntu                    latest              14f60031763d        10 days ago         120MB
nodered/node-red-docker   latest              435384cc1753        2 weeks ago         716MB
python                    3                   955d0c3b1bb2        3 weeks ago         684MB
postgres                  latest              f8d91fbcfa35        4 weeks ago         269MB

```

### 2.4. Liệt kê danh sách các containers

`docker ps [OPTIONS]`

Các options thường dùng là:

- --all,-a      : Hiển thị tất cả các containers
- --last,-n     : Hiển thi n containers được tạo gần nhất`
- --lastest,-l  : Hiện thị container cuối cùng được tạo

Ví dụ:

```sh
thao-nt@thao-nt:~$ docker ps -a
CONTAINER ID        IMAGE                     COMMAND                  CREATED              STATUS                          PORTS               NAMES
6fd807d26fa4        nodered/node-red-docker   "npm start -- --us..."   42 seconds ago       Up 41 seconds                   1880/tcp            angry_mclean
06796fd4f5f1        weshop_web:latest         "python2"                About a minute ago   Exited (0) About a minute ago                       festive_jang
```

```sh
thao-nt@thao-nt:~$ docker ps -n 1
CONTAINER ID        IMAGE                     COMMAND                  CREATED              STATUS              PORTS               NAMES
6fd807d26fa4        nodered/node-red-docker   "npm start -- --us..."   About a minute ago   Up About a minute   1880/tcp            angry_mclean

```

### 2.5 Docker attach

`docker attach [OPTIONS] CONTAINER`

Truy cập vào container.

Ví dụ: `thao-nt@thao-nt:~$ docker attach angry_mclean` 

### 2.6  Docker restart

Restart lại một hoặc nhiều containers

`docker restart [OPTIONS] CONTAINER [CONTAINER...]`

### 2.7 Docker login

Login vào một Docker registry

`docker login [OPTIONS] [SERVER]`

Các options là :

- --password,-p      Password
- --username,-u      Username

### 2.8 Docker logs

Hiển thị logs của một container.

`docker logs [OPTIONS] CONTAINER`

Các options thường dùng là:

- --details       : Hiển thị thêm chi tiết cho logs
- --since         : Hiển thị logs từ thời điểm(ví dụ:2013-01-02T13:23:37)
- --tail          : Tùy chọn số dòng hiển thị
- --timestamps,-t	: Hiển thị ra nhãn thời gian

Ví dụ:

```s
thao-nt@thao-nt:~⟫ docker logs --details nifty_euler 
 npm info it worked if it ends with ok
 npm info using npm@3.10.10
 npm info using node@v6.11.0
 npm info lifecycle node-red-docker@1.0.0~prestart: node-red-docker@1.0.0
 npm info lifecycle node-red-docker@1.0.0~start: node-red-docker@1.0.0
 
 > node-red-docker@1.0.0 start /usr/src/node-red
 > node $NODE_OPTIONS node_modules/node-red/red.js -v $FLOWS "--userDir" "/data"
 
 31 Jul 04:22:05 - [info] 
 
 Welcome to Node-RED

```

### 2.9 Docker pull

Pull một image hoặc một repository từ một registry.

`docker pull [OPTIONS] NAME[:TAG|@DIGEST]`

Các options là:

- --all-tags, -a        : Download tất cả các nhãn của image trong repository

Ví dụ:

`docker pull ubuntu:14.04`

### 2.10 Docker push

Push một image hoặc một repository tới một registry.

`docker push [OPTIONS] NAME[:TAG]`

### 2.11 Docker rm

Loại bỏ một hoặc nhiều containers.

`docker rm [OPTIONS] CONTAINER [CONTAINER...]`

Các options thường dùng là:

- --force,-f      : Cưỡng đoạt loại bỏ container kể cả khi container đó đang chạy.

Thường dùng:

- `docker rm $(docker ps -a -q)`: Loại bỏ container đang stop
- `docker rm $(docker ps -a -f status=exited -q)`: Loại bỏ tất cả các containers đã exit.

### 2.12 Docker rmi

Loại bỏ một hoặc nhiều images.

docker rmi [OPTIONS] IMAGE [IMAGE...]

Các options thường dùng là:

- --force, -f           :Cưỡng đoạt loại bỏ images

Ví dụ:
`thao-nt@thao-nt:~⟫ docker rmi ubuntu`

### 2.13 Docker start

Start một hoặc nhiều containers đã stop.

`docker start [OPTIONS] CONTAINER [CONTAINER...]`

Các options thường dùng là:

- --attach, -a: Attach vào STDOUT/STDERR

ví dụ: `thao-nt@thao-nt:~⟫ docker start nifty_euler`

### 2.14 Docker stats

Hiển thị dữ liệu thống kê trực tiếp của container.

`docker stats [OPTIONS] [CONTAINER...]`

Các optins thường dùng là:

- --all,-a: Hiển thị tất cả các container(mặc định chỉ hiển thị các container đang chạy)

ví dụ: `docker stats -a`

### 2.15 Docker stop

Stop một hoặc nhiều containers

`docker stop [OPTIONS] CONTAINER [CONTAINER...]`

Ví dụ: `docker stop ubuntu1`

## Tạo image cho web bán hàng sử dụng django

B1: Tạo một file có tên là `Dockerfile` tại thư mục gốc của ứng dụng django. Khi đó thư mục gốc sẽ có các file như sau:

```s
├── cart # ứng dụng của django
├── db.sqlite3   # cở sở dữ liệu
├── Dockerfile   # File Dockerfile vừa tạo
├── home         # Ứng dụng của django
├── manage.py    
├── templates     
└── we_shop

```

B2. Thêm nội dung sau vào file `Dockerfile`

```s
FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

B3. Tạo file `requirements.txt` cũng tại thư mục ứng dụng khi đó thư mục ứng dụng sẽ có các file là:

```s
├── cart
├── db.sqlite3
├── Dockerfile
├── home
├── manage.py
├── requirements.txt
├── templates
└── we_shop
```

File `requirements.txt` sẻ được sử dụng bởi câu lệnh `RUN pip install -r requirements.txt` trong Dockerfile để cài các gói cần thiết cho ứng dụng khi build image.

B4. Thêm nội dung sau vào file `requirements.txt`

```s
Django>=1.8,<2.0
psycopg2
django-dajaxice
django-dajax
```

B5. Taoj file `docker-compose.yml` cũng tại thư mục ứng dụng khi đó thư mục ứng dụng sẽ có các file là:

```s
├── cart
├── db.sqlite3
├── docker-compose.yml
├── Dockerfile
├── home
├── manage.py
├── requirements.txt
├── templates
└── we_shop

```

B6. Thêm nội dung sau vào file `docker-compose.yml`

```s
version: '2'

services:
  web:
    build: .
    volumes:
      - .:/code
    ports:
      - "8000:8000"

```

B7. Build image bằng câu lệnh

`docker build  -t web_shop_docker:v0 .`

B8. Run image bằng câu lệnh:

`docker run -dit -p 8000:8000 --name web_shop_docker web_shop_docker:v0`

Sau đó truy cập vào trình duyệt tại địa chỉ `http://127.0.0.1:8000/` để truy cập vào trang web
