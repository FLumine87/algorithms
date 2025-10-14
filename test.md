# 日程管理系统 - 新版接口文档
<!-- 需要修改的是
请求参数中的json代码改为表格
添加请求参数样例：
如有需要，添加请求和响应数据都需要添加对应的参数格式
为响应数据添加参数说明，表格形式
增加子标题，x.x.n,分别为基本信息，请求参数，响应数据
在x..x.1中添加接口描述
强调，如果参数说明的表格出现子类，如data中还包含若干参数，有特殊格式，且需要尽可能列出来
tip，如果参数样例可以用``包裹，不一定要代码块
 -->
## 基础信息

- **基础URL**: `/api/v1`
- **认证方式**: Token认证（请求头需加 `Authorization: Bearer {token}`）
- **日期格式**: YYYY-MM-DD
- **时间格式**: HH:mm (24小时制)
- **时间段格式**: HH:mm-HH:mm
- **完整时间戳**: ISO 8601

---

## 1. 用户认证模块

### 1.1 用户登录

#### 1.1.1 基本信息
- 接口地址: `/auth/login`
- 请求方法: POST
- 接口描述：待定

#### 1.1.2 请求参数
    ```json
    {
      "username": "string, 必填, 用户名",
      "password": "string, 必填, 密码"
    }
    ```
#### 1.1.3 响应数据
- **响应示例**:
    ```json
    {
      "code": 200,
      "message": "登录成功",
      "data": {
        "token": "jwt_token_string",
        "user": {
          "id": 1,
          "username": "user123",
          "nickname": "学生用户",
          "avatar": "https://example.com/avatar.png",
          "gender": "男",
          "school": "XX大学"
        }
      }
    }
    ```

### 1.2 用户注册

- **接口地址**: `/auth/register`
- **请求方法**: POST
- **请求参数**:
    ```json
    {
      "username": "string, 必填, 用户名",
      "password": "string, 必填, 密码",
      "confirmPassword": "string, 必填, 确认密码"
    }
    ```
- **响应示例**:
    ```json
    {
      "code": 200,
      "message": "注册成功",
      "data": null
    }
    ```

### 1.3 退出登录

- **接口地址**: 无（前端清除token即可）
- **请求方法**: 无
- **说明**: 前端调用 `api.auth.logout()`，仅清除本地token，不与后端交互。

---

## 2. 日程管理模块

### 2.1 获取日程列表

- **接口地址**: `/schedules`
- **请求方法**: GET
- **查询参数**:
    - `date`: string, 可选, 查询指定日期的日程 (格式: YYYY-MM-DD)
- **响应示例**:
    ```json
    {
      "code": 200,
      "data": [
        {
          "id": 1,
          "event": "团队会议",
          "date": "2024-01-15",
          "time": "14:00",
          "location": "会议室A",
          "people": "张三、李四",
          "priority": "important-urgent",
          "userId": 1
        }
      ]
    }
    ```

### 2.2 创建日程

- **接口地址**: `/schedules`
- **请求方法**: POST
- **请求参数**:
    ```json
    {
      "event": "string, 必填, 事件名称",
      "date": "string, 必填, 日期 (YYYY-MM-DD)",
      "time": "string, 必填, 时间 (HH:mm)",
      "location": "string, 可选, 地点",
      "people": "string, 可选, 参与人",
      "priority": "string, 必填, 优先级"
    }
    ```
- **优先级枚举值**:
    - `important-urgent`
    - `important-not-urgent`
    - `not-important-urgent`
    - `not-important-not-urgent`

### 2.3 更新日程

- **接口地址**: `/schedules/{id}`
- **请求方法**: PUT
- **请求参数**: 同创建日程

### 2.4 删除日程

- **接口地址**: `/schedules/{id}`
- **请求方法**: DELETE

---

## 3. 课程管理模块

### 3.1 获取课程列表

- **接口地址**: `/courses`
- **请求方法**: GET
- **查询参数**:
    - `date`: string, 可选, 查询指定日期的课程
    - `week`: number, 可选, 查询指定周次的课程
- **响应示例**:
    ```json
    {
      "code": 200,
      "data": [
        {
          "id": 1,
          "name": "高等数学",
          "date": "2024-01-15",
          "time": "08:00-09:40",
          "location": "教学楼A101",
          "teacher": "张教授",
          "weeks": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
          "notes": "期中考试在第8周",
          "userId": 1
        }
      ]
    }
    ```

### 3.2 创建课程

- **接口地址**: `/courses`
- **请求方法**: POST
- **请求参数**:
    ```json
    {
      "name": "string, 必填, 课程名称",
      "date": "string, 必填, 日期",
      "time": "string, 必填, 时间段",
      "location": "string, 必填, 地点",
      "teacher": "string, 必填, 教师",
      "weeks": "array, 必填, 周次数组",
      "notes": "string, 可选, 备注"
    }
    ```
- **时间段枚举值**:
    - `08:00-09:40`
    - `10:00-11:40`
    - `14:00-15:40`
    - `16:00-17:40`
    - `19:00-20:40`

### 3.3 更新课程

- **接口地址**: `/courses/{id}`
- **请求方法**: PUT
- **请求参数**: 同创建课程

### 3.4 删除课程

- **接口地址**: `/courses/{id}`
- **请求方法**: DELETE

---

## 4. 笔记管理模块

### 4.1 获取笔记列表

- **接口地址**: `/notes`
- **请求方法**: GET
- **响应示例**:
    ```json
    {
      "code": 200,
      "data": [
        {
          "id": 1,
          "title": "项目会议记录",
          "content": "讨论了项目进度和下一步计划...",
          "createdAt": "2024-01-15T10:00:00Z",
          "updatedAt": "2024-01-15T10:00:00Z",
          "userId": 1
        }
      ]
    }
    ```

### 4.2 创建笔记

- **接口地址**: `/notes`
- **请求方法**: POST
- **请求参数**:
    ```json
    {
      "title": "string, 必填, 笔记标题",
      "content": "string, 必填, 笔记内容"
    }
    ```

### 4.3 更新笔记

- **接口地址**: `/notes/{id}`
- **请求方法**: PUT
- **请求参数**: 同创建笔记

### 4.4 删除笔记

- **接口地址**: `/notes/{id}`
- **请求方法**: DELETE

---

## 5. 提醒管理模块

### 5.1 获取活跃提醒

- **接口地址**: `/reminders/active`
- **请求方法**: GET
- **响应示例**:
    ```json
    {
      "code": 200,
      "data": [
        {
          "id": 1,
          "event": "团队会议",
          "reminderTime": "2024-01-15T13:50:00Z",
          "scheduleId": 1,
          "userId": 1
        }
      ]
    }
    ```

### 5.2 创建提醒

- **接口地址**: `/reminders`
- **请求方法**: POST
- **请求参数**:
    ```json
    {
      "event": "string, 必填, 事件名称",
      "reminderTime": "string, 必填, 提醒时间 (ISO 8601)",
      "scheduleId": "number, 可选, 关联的日程ID"
    }
    ```

### 5.3 取消提醒

- **接口地址**: `/reminders/{id}`
- **请求方法**: DELETE

---

## 6. 用户信息模块

### 6.1 获取用户信息

- **接口地址**: `/user/profile`
- **请求方法**: GET
- **响应示例**:
    ```json
    {
      "code": 200,
      "data": {
        "id": 1,
        "username": "user123",
        "nickname": "学生用户",
        "avatar": "https://example.com/avatar.png",
        "gender": "男",
        "school": "XX大学"
      }
    }
    ```

### 6.2 更新用户信息

- **接口地址**: `/user/profile`
- **请求方法**: PUT
- **请求参数**:
    ```json
    {
      "nickname": "string, 可选, 昵称",
      "gender": "string, 可选, 性别",
      "school": "string, 可选, 学校"
    }
    ```

### 6.3 上传头像

- **接口地址**: `/user/avatar`
- **请求方法**: POST
- **请求类型**: multipart/form-data
- **请求参数**:
    - `avatar`: file, 必填, 头像文件
- **响应示例**:
    ```json
    {
      "code": 200,
      "data": {
        "avatarUrl": "https://example.com/upload/avatar_123.png"
      }
    }
    ```

---

## 7. 其它说明

- **错误码说明**:  
  |错误码|说明|
  |---|---|
  |200|成功|
  |400|请求参数错误|
  |401|未授权|
  |403|禁止访问|
  |404|资源不存在|
  |500|服务器内部错误|

- **分页与排序**:  
  列表接口建议支持 `page`、`pageSize`、`sortBy`、`sortOrder` 参数。

- **安全要求**:  
  1. 除登录、注册外所有接口需Token认证  
  2. 密码加密传输和存储  
  3. 用户只能访问自己的数据  
  4. 文件上传需验证类型和大小  
  5. 敏感操作需日志记录

- **文件上传限制**:  
  最大2MB，支持JPG/PNG，建议头像100x100像素

---

**本接口文档适用于新版前端（aa.html）和新版API服务（api.js），与原接口文档保持兼容。**