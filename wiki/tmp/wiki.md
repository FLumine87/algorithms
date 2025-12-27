## 主要类型前缀

| 前缀         | 含义      | 示例                   |
| ---------- | ------- | -------------------- |
| `feat`     | 新功能     | `feat: 添加用户登录功能`     |
| `fix`      | 修复bug   | `fix: 修复首页加载错误`      |
| `docs`     | 文档更新    | `docs: 更新API使用说明`    |
| `style`    | 代码格式调整  | `style: 调整缩进格式`      |
| `refactor` | 重构代码    | `refactor: 优化用户验证逻辑` |
| `test`     | 测试相关    | `test: 添加登录功能测试`     |
| `chore`    | 构建/工具更新 | `chore: 更新webpack配置` |
| `perf`     | 性能优化    | `perf: 优化图片加载速度`     |

### 🔧 **实际应用**
```bash
# 新功能
git commit -m "feat: 添加购物车功能"

# 修复bug
git commit -m "fix: 修复支付页面崩溃问题"

# 带范围的提交
git commit -m "feat(auth): 添加第三方登录支持"

# 破坏性变更（BREAKING CHANGE）
git commit -m "feat!: 重构用户API，移除旧方法"
```

```
<type>[optional scope]: <description>

[optional body]
[optional footer]
```