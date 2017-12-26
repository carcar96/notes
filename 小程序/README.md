## 常见问题总结：
### 1. 下拉刷新onPullDownRefresh
- 基础库版本：1.5.4
- 问题："enablePullDownRefresh": "true"中——在模拟机和安卓机上能正常实现，在苹果机不能实现
- 解决方案：字符串"true"改为布尔值的true，即"enablePullDownRefresh": true

### 2. 图片路径
- 解决方案：不能使用相对路径，要使用绝对路径，例如：“/images/icon.png”