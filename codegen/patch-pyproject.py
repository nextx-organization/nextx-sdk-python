"""Bổ sung siêu dữ liệu chuẩn PyPI vào pyproject.toml do openapi-python-client sinh (mô tả, giấy phép, liên kết, phân loại)."""
import re
import sys

path, sha = sys.argv[1], sys.argv[2]
s = open(path, encoding="utf-8").read()
meta = '''description = "NextX API cho Python — sinh từ OpenAPI công khai, có kiểu đầy đủ"
readme = "README.md"
license = {text = "MIT"}
authors = [{name = "NextX", email = "support@nextx.vn"}]
keywords = ["nextx", "crm", "sales", "api", "sdk", "openapi"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Topic :: Software Development :: Libraries",
    "Typing :: Typed",
]
'''
s = re.sub(r'^description = .*\n', "", s, flags=re.M)
s = re.sub(r'^authors = .*\n', "", s, flags=re.M)
s = re.sub(r'^readme = .*\n', "", s, flags=re.M)
s = re.sub(r'^license = .*\n', "", s, flags=re.M)
s = s.replace("[project]\n", "[project]\n" + meta, 1)
s += f'''
[project.urls]
Homepage = "https://developers.nextx.vn/docs/sdk"
Documentation = "https://developers.nextx.vn"
Source = "https://github.com/nextx-organization/nextx-sdk-python"
Changelog = "https://github.com/nextx-organization/nextx-sdk-python/blob/main/CHANGELOG.md"
Issues = "https://github.com/nextx-organization/nextx-sdk-python/issues"

[tool.nextx]
spec-sha256 = "{sha}"
'''
s = s.replace('requires = ["pdm-backend"]', 'requires = ["pdm-backend==2.4.5"]')  # dựng lặp lại được
open(path, "w", encoding="utf-8").write(s)
