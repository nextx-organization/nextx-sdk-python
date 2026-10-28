# nextx-sdk

> Mã trong kho này được sinh tự động từ [OpenAPI công khai](https://developers.nextx.vn/openapi.json). Đừng sửa tay — xem [CONTRIBUTING.md](CONTRIBUTING.md).

Gọi NextX API từ Python, có kiểu đầy đủ (đồng bộ và `async`). Mã sinh từ [`/openapi.json`](https://developers.nextx.vn/openapi.json)
và chỉ gồm các tuyến đối tác gọi được.

```sh
pip install nextx-sdk
```

```python
import os
from nextx_sdk import create_client, SANDBOX_URL
from nextx_sdk.api.crm import contacts_list

# Khoá API của workspace (tạo trong phần mềm NextX) — gửi ở header X-Api-Key
nx = create_client(api_key=os.environ["NEXTX_API_KEY"], base_url=SANDBOX_URL)

page = contacts_list.sync(client=nx, page_size=20)
for c in page.items or []:
    print(c.full_name)

# async
page = await contacts_list.asyncio(client=nx, page_size=20)
```

Ứng dụng đối tác dùng OAuth 2.0: `create_client(access_token=token)` (gửi `Authorization: Bearer`).

- Python ≥ 3.11. Mỗi thao tác là một mô-đun trong `nextx_sdk.api.<phân hệ>` với 4 hàm: `sync`, `sync_detailed`, `asyncio`, `asyncio_detailed`.
  Bản `*_detailed` trả thêm mã trạng thái và header.
- Mặc định gọi prod (`PROD_URL`). Thử nghiệm thì dùng `SANDBOX_URL` với khoá sandbox.
- Mã trạng thái ngoài tài liệu ném `nextx_sdk.errors.UnexpectedStatus`.

Tài liệu: https://developers.nextx.vn/docs/sdk · Phiên bản và bỏ dần: [VERSIONING.md](https://github.com/nextx-organization/nextx-sdk-python/blob/main/VERSIONING.md) · Giấy phép MIT
