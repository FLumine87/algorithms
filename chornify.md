# Chronify 日程管理系统 - 完整部署文档

## 📋 系统要求

### 必需组件及版本
| 组件 | 版本要求 | 下载地址 |
|------|----------|----------|
| Java JDK | **JDK 17** (推荐) 或 JDK 11 | [OpenJDK](https://openjdk.org/) 或 [Oracle JDK](https://www.oracle.com/java/) |
| Maven | **3.6+** | [Maven官网](https://maven.apache.org/) |
| MySQL | **8.0+** | [MySQL官网](https://dev.mysql.com/) |
| Nginx | **1.18+** | [Nginx for Windows](http://nginx.org/) |


---

## 🛠️ 环境准备

### 1. 验证环境安装
```cmd
# 检查Java
java -version
# 应该显示：Java version "17.x.x"

# 检查Maven  
mvn -version
# 应该显示：Apache Maven 3.6.x

# 检查MySQL
mysql --version
# 应该显示：mysql Ver 8.0.x
```

### 2. 环境变量配置（如未自动配置）
```cmd
# 设置Java环境变量（如果需要）
setx JAVA_HOME "C:\Program Files\Java\jdk-17" /M
setx PATH "%PATH%;%JAVA_HOME%\bin" /M

# 设置Maven环境变量（如果需要）
setx M2_HOME "C:\apache-maven-3.8.6" /M
setx PATH "%PATH%;%M2_HOME%\bin" /M
```

---

## 🗄️ 数据库部署

### 1. 启动MySQL服务
```cmd
# 启动MySQL服务
net start mysql

# 如服务不存在，可能需要初始化
mysqld --initialize --console
```

### 2. 创建数据库并导入数据
```cmd
# 连接MySQL（使用UTF8编码避免中文乱码）
mysql -uroot -p123456 --default-character-set=utf8mb4

# 在MySQL中执行以下命令：
source ./final-project/Chronify_back-end-main/database_design.sql; #若路径不同请修改
USE chronify;
#SET NAMES utf8mb4;
exit;
```

上面的内容请与以下配置文件相匹配
```properties
spring:
  application:
    name: Chronify
  datasource:
    url: jdbc:mysql://localhost:3306/${DB_NAME:chronify}
    username: ${DB_USERNAME:root}  #用户名:root
    password: ${DB_PASSWORD:123456} # 密码:123456
```

### 3. 验证数据库导入
```cmd
# 验证数据导入
mysql -uroot -p1234 --default-character-set=utf8mb4 chronify -e "SHOW TABLES; SELECT * FROM users LIMIT 3;"
```

**📝 注意点：**
- 必须使用 `utf8mb4` 字符集，否则中文字符会乱码
- 如果导入时出现表已存在的错误，可以忽略（数据已成功插入）
- 确保数据库连接密码正确（默认为1234）

---

## 🔧 后端部署

### 1. 构建并启动后端
```cmd
# 进入后端项目目录
cd .\final-project\Chronify_back-end-main\Chronify

# 清理并编译项目
mvn clean compile

# 启动后端服务
mvn spring-boot:run
```

### 2. 验证后端运行
**成功标志：**
- 控制台显示：`Tomcat started on port(s): 8080 (http)`
- 访问测试：`http://localhost:8080` 返回成功信息

**📝 注意点：**
- 第一次启动会下载依赖，可能需要较长时间
- 如果端口8080被占用，可在application.properties中修改 `server.port`
- 确保MySQL服务在后台运行

---

## 🌐 前端部署

### 1. 启动Nginx

#### 步骤1：修改配置文件路径

编辑 `nginx.conf`，修改项目根目录路径：

```nginx
# 找到这一行
root .;

# 如果nginx不在项目目录，修改为绝对路径，例如：
# root C:/Users/Administrator/Desktop/2025.11.11修改;
```

#### 步骤2：检查后端API地址

确认后端API服务地址：

```nginx
# 在nginx.conf中找到
upstream backend_api {
    server localhost:8080;  # 确认端口正确
    keepalive 32;
}
```

#### 步骤3：测试配置

运行管理脚本，选择"5. 测试配置文件"：

```batch
nginx-manager.bat
```

或直接运行：

```batch
nginx.exe -t
```

#### 步骤4：启动Nginx

使用管理脚本启动：

```batch
nginx-manager.bat
# 选择 1. 启动 Nginx
```

或直接运行：

```batch
nginx.exe
```

### 4. 访问应用

启动后，在浏览器中访问：

- HTTP: `http://localhost`
- 如果配置了HTTPS: `https://localhost`
**📝 注意点：**
- 确保前端文件包含 `aa.html`
- 如果80端口被占用，可修改nginx.conf中的 `listen` 端口
- Nginx会创建多个进程，这是正常现象

---

## 🚀 启动完整服务

### 手动启动顺序
1. **启动MySQL服务**
2. **启动后端Spring Boot应用** 
3. **启动Nginx服务**
4. **访问前端应用**

---

## ✅ 验证部署

### 服务状态检查
```cmd
# 检查所有服务进程
tasklist | findstr nginx
tasklist | findstr java
tasklist | findstr mysql

# 检查端口监听
netstat -ano | findstr :80
netstat -ano | findstr :8080
netstat -ano | findstr :3306
```

### 功能测试
1. **访问前端**：`http://localhost` - 应该显示应用界面
2. **测试后端API**：`http://localhost:8080/health` - 应该返回健康状态
3. **测试代理**：`http://localhost/api/v1/courses` - 应该返回课程数据

---

## 🐛 故障排除

### 常见问题及解决方案

#### 1. 数据库连接失败
**症状**：后端启动时数据库连接错误
**解决**：
```cmd
# 检查MySQL服务
net start mysql

# 验证数据库连接
mysql -uroot -p1234 -e "SHOW DATABASES;"
```

#### 2. 端口冲突
**症状**：端口已被占用
**解决**：
- 修改后端端口：在application.properties中设置 `server.port=8081`
- 修改Nginx端口：在nginx.conf中设置 `listen 8088`

#### 3. 中文乱码
**症状**：数据库中文显示为乱码
**解决**：确保所有环节使用UTF-8编码
- 数据库：`CHARACTER SET utf8mb4`
- MySQL连接：`--default-character-set=utf8mb4`
- 后端：配置文件中设置字符编码

#### 4. Nginx 403错误
**症状**：访问localhost显示403 Forbidden
**解决**：
```cmd
# 检查html目录是否有index.html
dir C:\nginx\html\

# 如果没有，创建测试页面或复制前端文件
echo ^<html^>^<body^>^<h1^>Chronify^</h1^>^</body^>^</html^> > C:\nginx\html\index.html
```

#### 5. 后端500错误
**症状**：访问后端API返回500错误
**解决**：
- 检查后端日志中的具体错误信息
- 确认数据库表结构正确
- 验证依赖包完整：`mvn dependency:resolve`

---

## 📞 获取帮助

如果遇到问题：
1. 检查本文档中的"注意点"和"故障排除"部分
2. 查看各服务的日志文件：
   - 后端日志：控制台输出
   - Nginx日志：`C:\nginx\logs\error.log`
   - MySQL日志：MySQL错误日志文件
3. 确保所有服务版本符合要求

---

## 🎉 部署完成

当所有步骤完成后，您应该能够：
- ✅ 在浏览器中访问 `http://localhost` 看到前端界面
- ✅ 用户能够注册、登录系统
- ✅ 能够正常使用课程表、日程、笔记等功能
- ✅ 数据能够正确保存到MySQL数据库

祝您使用愉快！