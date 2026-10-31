# nextx-sdk

Thư viện chính thức để gọi NextX API từ Python, hỗ trợ cả đồng bộ và `async`.

Mã trong kho này được sinh tự động từ [OpenAPI của NextX](https://developers.nextx.vn/openapi.json). Vui lòng không sửa trực tiếp, xem [CONTRIBUTING.md](CONTRIBUTING.md).

## Cài đặt

```sh
pip install nextx-sdk
```

Yêu cầu Python 3.11 trở lên.

## Bắt đầu

```python
import os
from nextx_sdk import create_client, SANDBOX_URL
from nextx_sdk.api.crm import contacts_list

# Khoá API của workspace, tạo trong phần mềm NextX, gửi ở header X-Api-Key
nx = create_client(api_key=os.environ["NEXTX_API_KEY"], base_url=SANDBOX_URL)

page = contacts_list.sync(client=nx, page_size=20)
for c in page.items or []:
    print(c.full_name)

# async
page = await contacts_list.asyncio(client=nx, page_size=20)
```

Ứng dụng đối tác dùng OAuth 2.0 thì tạo client bằng `create_client(access_token=token)`.

## Nhận webhook

Kiểm chữ ký theo chuẩn [Standard Webhooks](https://www.standardwebhooks.com). Truyền thân gốc (bytes), không phải JSON đã parse:

```python
from nextx_sdk.webhooks import verify_webhook, WebhookVerificationError

event = verify_webhook(raw_body, request.headers, os.environ["NEXTX_WEBHOOK_SECRET"])
if event["type"] == "call.completed":
    call = event["data"]["object"]          # cùng hình dạng GET /api/v1/call/partner/calls/{id}
```

Sai chữ ký hoặc lệch giờ quá 5 phút thì ném `WebhookVerificationError`. Dùng `event["id"]` để bỏ qua lần giao trùng.

## Ghi chú

- Mỗi endpoint là một mô-đun trong `nextx_sdk.api.<phân hệ>` với 4 hàm: `sync`, `sync_detailed`, `asyncio`, `asyncio_detailed`. Các hàm `*_detailed` trả thêm mã trạng thái và header.
- Mặc định client gọi môi trường production (`PROD_URL`). Khi thử nghiệm, dùng `SANDBOX_URL` với khoá sandbox.
- Mã trạng thái không có trong tài liệu sẽ ném `nextx_sdk.errors.UnexpectedStatus`.

## Tài liệu

- Hướng dẫn: https://developers.nextx.vn/docs/sdk
- Phiên bản và chính sách ngừng hỗ trợ: [VERSIONING.md](VERSIONING.md)
- Nhật ký thay đổi: [CHANGELOG.md](CHANGELOG.md)

Giấy phép MIT.
