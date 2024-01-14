运行环境：python
运行框架：Django
IDE：PyCharm
======================================
django常用命令:
步骤1：
--创建一个Django项目myDjango：django-admin startproject myDjango
步骤2：
--创建一个应用程序boards：django-admin startapp boards
步骤3：
--运行项目：python manage.py runserver

其它命令：
--加载项目启动Python shell：python manage.py shell
--执行测试套件：python manage.py test
```bash
pip install -r requirements.txt
pip uninstall -r requirements.txt
```
======================================
myDjango框架目录结构：
manage.py：django-admin 是命令行工具的快捷方式。它用于运行与我们项目相关的管理命令。我们将使用它来运行开发服务器，运行测试，创建迁移等等。
init.py：这个空文件告诉 Python 这个文件夹是一个 Python 包。
settings.py：这个文件包含了所有的项目配置。我们会一直使用到这个文件。
urls.py：这个文件负责映射我们项目中的路由和路径。例如，如果您想在 URL /about/ 中显示某些内容，则必须先将其映射到此处。
wsgi.py：该文件是用于部署简单的网关接口。

boards项目目录结构：
migrations/：在这个文件夹中，Django 会存储一些文件以跟踪您在 models.py 文件中创建的更改，目的是为了保持数据库和 models.py 同步。
admin.py：这是 Django应用程序一个名为 Django Admin 的内置配置文件。
apps.py：这是应用程序本身的配置文件。
models.py：这里是我们定义 Web 应用程序实体的地方。models 由 Django 自动转换为数据库表。
tests.py：该文件用于为应用程序编写单元测试。
views.py：这是我们处理Web应用程序请求(request)/响应(resopnse)周期的文件。
.env：配置文件
requirements.txt:依赖组件
其它：
templates/：静态文件
static/：静态文件
venv/：是Python 3.3的新特性，虚拟环境主要是为不同 Python 项目创建一个隔离的环境，每个项目都可以拥有独立的依赖包环境，而项目间的依赖包互不影响
===============
常用组件和功能:
--Bootstrap
是一个用 HTML，CSS 和JavaScript 开发的开源工具包。
--Django Admin
网站管理员实施一个管理界面来管理它。http://127.0.0.1:8000/admin
运行效果.png
============
模型（Models）
--迁移模型（Migrating the Models）
python manage.py makemigrations
--迁移文件被翻译成 SQL 语句
python manage.py sqlmigrate boards 0001
--迁移文件应用到数据库中
python manage.py migrate</code>
