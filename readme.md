# Sơ đồ triển khai

![sơ đồ](https://i.imgur.com/Ivn6cXt.png)

Trong đó:
- Sensor kết nối với Raspberry Pi thông qua bộ GPIO Extension.

- Raspberry Pi là một VNC server, đồng thời Laptop cài đặt VNC Viewer, để có thể truy cập từ xa vào Raspberry Pi ( Có thể sử dụng ssh).

- Trên Raspberry Pi cài đặt Docker, dựng container Home Assistant.

- Github lưu trữ source code, Raspberry Pi kết nối mạng, có thể pull code về sử dụng. 

- Home Assistant quản lí things tại tầng Fog.

# Cấu hình Home Assistant

- Dựa trên Docs [Home Assistant](https://www.home-assistant.io/docs/configuration/)

- Cụ thể: Thêm sensor hiển thị trên Home Assistant bằng cách thay đổi file configuration.yaml, cấu hình tương tự [adding devices to HA](https://www.home-assistant.io/docs/configuration/devices/)

- Đồng thời sử dụng message queue để truyền dữ liệu nhận được tới hiển thị tại Home Assistant, bằng cách sử dụng một Broker là Mosquitto, nơi lưu giữ các topic dữ liệu. Một chương trình Publish dữ liệu tới 1 topic của Broker. Home Assistant Subcribe tại topic đó.

- Như mô hình dưới đây:

![message queue](https://i.imgur.com/TK24SPC.png)

