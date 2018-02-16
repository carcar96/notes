## 常见问题总结：
### 1. 下拉刷新onPullDownRefresh
- 基础库版本：1.5.4
- 问题："enablePullDownRefresh": "true"中——在模拟机和安卓机上能正常实现，在苹果机不能实现
- 解决方案：字符串"true"改为布尔值的true，即"enablePullDownRefresh": true

### 2. 图片路径
- 解决方案：不能使用相对路径，要使用绝对路径，例如：“/images/icon.png”

### 3.输入组件被弹出的手机键盘挡住
- 解决方案：使用input的属性cursor-spacing，指定光标与键盘的距离，单位 px 。取 input 距离底部的距离和 cursor-spacing 指定的距离的最小值作为光标与键盘的距离。

### 4.地图组件map中marker 上的气泡 label属性(bgColor等)用“#fff”3个字母不能改变颜色
- 解决方案：必须使用“#ffffff”6个字母才行