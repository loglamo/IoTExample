# Hệ thống Knock Switch và Cathode LED 
## 1. Xây dựng mạch

- Với Knock Switch:

        Chân (-) - GND
        Chân (s) - GPIO0 (hay pin 11)
        Chân (middle) - 5V

- Với Cathode LED:

        Chân (-) - GND
        Chân (s) - GPIO4 (hay pin 16)
        Chân (middle) - GPIO3 (hay pin 15)

## 2. Ý tưởng

- Knock Switch là sensor dùng để phát hiện những cử động (những cử động tác động lên sensor sẽ làm lò xo trên sensor rung và tín hiệu được truyền đi). Có thể lắp đặt sensor này lên cánh cửa, cùng chuông cửa, hoặc đèn LED để báo hiệu. Trong TH này sử dụng đèn LED. Khi có tác động đến sensor Knock, LED sẽ sáng.

## 3. Sử dụng HomeAssistant cho quản lí things

- Cấu hình HomeAssistant để thêm sensor, sửa trong file configuration.yaml
- Cấu hình HomeAssistant, IP để người dùng ngoài có thể truy cập từ xa vào HomeAssistant. Qua các thao tác chính như: Thiết lập static IP cho máy, thiết lập cho cổng 8123 của HomeAssistant external với Internet, sủ dụng Duckdns.org để tạo sub domain. Truy cập địa chỉ "iotla.duckdns.org:8123" để trùy cập từ xa vào HomeAssistant.
- Có thể thay đổi mk để đảm bảo an toàn.
- Chi tiết tại [remote access](https://www.home-assistant.io/docs/ecosystem/certificates/lets_encrypt/)

