
# Chronify Schedule Management System - Complete Deployment Documentation

## 📋 System Requirements

### Required Components & Versions
| Component | Version Requirement | Download Link |
|-----------|---------------------|---------------|
| Java JDK | **JDK 17** (Recommended) or JDK 11 | [OpenJDK](https://openjdk.org/) or [Oracle JDK](https://www.oracle.com/java/) |
| Maven | **3.6+** | [Maven Official Site](https://maven.apache.org/) |
| MySQL | **8.0+** | [MySQL Official Site](https://dev.mysql.com/) |
| Nginx | **1.18+** | [Nginx for Windows](http://nginx.org/) |

---

## 🛠️ Environment Preparation

### 1. Verify Environment Installation
```cmd
# Check Java
java -version
# Should display: Java version "17.x.x"

# Check Maven
mvn -version
# Should display: Apache Maven 3.6.x

# Check MySQL
mysql --version
# Should display: mysql Ver 8.0.x
```

### 2. Environment Variable Configuration (If not automatically configured)
```cmd
# Set Java environment variables (if needed)
setx JAVA_HOME "C:\Program Files\Java\jdk-17" /M
setx PATH "%PATH%;%JAVA_HOME%\bin" /M

# Set Maven environment variables (if needed)
setx M2_HOME "C:\apache-maven-3.8.6" /M
setx PATH "%PATH%;%M2_HOME%\bin" /M
```

---

## 🗄️ Database Deployment

### 1. Start MySQL Service
```cmd
# Start MySQL service
net start mysql

# If service doesn't exist, may need initialization
mysqld --initialize --console

# Connect to MySQL (using UTF8 encoding to avoid Chinese character issues)
mysql -uroot -p123456 --default-character-set=utf8mb4

# Execute the following commands in MySQL:(Modify if path is different)
source ./final-project/Chronify_back-end-main/database_design.sql; 
USE chronify;
exit;
```

### 2. Create Database and Import Data
```cmd
# Connect to MySQL (using UTF8 encoding to avoid Chinese character issues)
mysql -uroot -p123456 --default-character-set=utf8mb4

# Execute the following commands in MySQL:
source ./final-project/Chronify_back-end-main/database_design.sql; # Modify if path is different
USE chronify;
#SET NAMES utf8mb4;
exit;
```

The above content should match the following configuration file:
```properties
spring:
  application:
    name: Chronify
  datasource:
    url: jdbc:mysql://localhost:3306/${DB_NAME:chronify}
    username: ${DB_USERNAME:root}  # Username: root
    password: ${DB_PASSWORD:123456} # Password: 123456
```

### 3. Verify Database Import
```cmd
# Verify data import
mysql -uroot -p1234 --default-character-set=utf8mb4 chronify -e "SHOW TABLES; SELECT * FROM users LIMIT 3;"
```

**📝 Important Notes:**
- Must use `utf8mb4` character set, otherwise Chinese characters will display incorrectly
- If "table already exists" error occurs during import, it can be ignored (data successfully inserted)
- Ensure database connection password is correct (default: 1234)

---

## 🔧 Backend Deployment

### 1. Build and Start Backend
```cmd
# Navigate to backend project directory
cd .\final-project\Chronify_back-end-main\Chronify

# Clean and compile project
mvn clean compile

# Start backend service
mvn spring-boot:run
```

### 2. Verify Backend Operation
**Success Indicators:**
- Console displays: `Tomcat started on port(s): 8080 (http)`
- Access test: `http://localhost:8080` returns success message

**📝 Important Notes:**
- First startup will download dependencies and may take longer
- If port 8080 is occupied, modify `server.port` in application.properties
- Ensure MySQL service is running in background

---

## 🌐 Frontend Deployment

### 1. Start Nginx

#### Step 1: Modify Configuration File Path

Edit `nginx.conf`, modify project root directory path:

```nginx
# Find this line
root .;

# If nginx is not in project directory, modify to absolute path, for example:
# root C:/Users/Administrator/Desktop/2025.11.11修改;
```

#### Step 2: Check Backend API Address

Confirm backend API service address:

```nginx
# Find in nginx.conf
upstream backend_api {
    server localhost:8080;  # Confirm port is correct
    keepalive 32;
}
```

#### Step 3: Test Configuration

Run management script, select "5. Test Configuration File":

```batch
nginx-manager.bat
```

Or run directly:

```batch
nginx.exe -t
```

#### Step 4: Start Nginx

Start using management script:

```batch
nginx-manager.bat
# Select 1. Start Nginx
```

Or run directly:

```batch
nginx.exe
```

### 4. Access Application

After starting, access in browser:

- HTTP: `http://localhost`
- If HTTPS configured: `https://localhost`

**📝 Important Notes:**
- Ensure frontend files include `aa.html`
- If port 80 is occupied, modify `listen` port in nginx.conf
- Nginx creates multiple processes, which is normal

---

## 🚀 Start Complete Service

### Manual Startup Sequence
1. **Start MySQL Service**
2. **Start Backend Spring Boot Application**
3. **Start Nginx Service**
4. **Access Frontend Application**

---

## ✅ Verify Deployment

### Service Status Check
```cmd
# Check all service processes
tasklist | findstr nginx
tasklist | findstr java
tasklist | findstr mysql

# Check port listening
netstat -ano | findstr :80
netstat -ano | findstr :8080
netstat -ano | findstr :3306
```

### Functionality Testing
1. **Access Frontend**: `http://localhost` - Should display application interface
2. **Test Backend API**: `http://localhost:8080/health` - Should return health status
3. **Test Proxy**: `http://localhost/api/v1/courses` - Should return course data

---

## 🐛 Troubleshooting

### Common Issues & Solutions

#### 1. Database Connection Failure
**Symptoms**: Database connection error during backend startup
**Solution**:
```cmd
# Check MySQL service
net start mysql

# Verify database connection
mysql -uroot -p1234 -e "SHOW DATABASES;"
```

#### 2. Port Conflict
**Symptoms**: Port already in use
**Solution**:
- Modify backend port: Set `server.port=8081` in application.properties
- Modify Nginx port: Set `listen 8088` in nginx.conf

#### 3. Chinese Character Encoding Issues
**Symptoms**: Chinese characters display incorrectly in database
**Solution**: Ensure UTF-8 encoding used in all steps
- Database: `CHARACTER SET utf8mb4`
- MySQL connection: `--default-character-set=utf8mb4`
- Backend: Set character encoding in configuration file

#### 4. Nginx 403 Error
**Symptoms**: Accessing localhost shows 403 Forbidden
**Solution**:
```cmd
# Check if html directory has index.html
dir C:\nginx\html\

# If not, create test page or copy frontend files
echo ^<html^>^<body^>^<h1^>Chronify^</h1^>^</body^>^</html^> > C:\nginx\html\index.html
```

#### 5. Backend 500 Error
**Symptoms**: Accessing backend API returns 500 error
**Solution**:
- Check specific error information in backend logs
- Confirm database table structure is correct
- Verify dependency packages are complete: `mvn dependency:resolve`

---

## 📞 Get Help

If encountering problems:
1. Check "Important Notes" and "Troubleshooting" sections in this document
2. Check logs for each service:
   - Backend logs: Console output
   - Nginx logs: `C:\nginx\logs\error.log`
   - MySQL logs: MySQL error log file
3. Ensure all service versions meet requirements

---

## 🎉 Deployment Complete

When all steps are completed, you should be able to:
- ✅ Access frontend interface at `http://localhost` in browser
- ✅ Users can register and login to system
- ✅ Normal use of timetable, schedule, notes and other functions
- ✅ Data correctly saved to MySQL database

Wish you a pleasant experience!
