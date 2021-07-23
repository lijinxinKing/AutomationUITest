# AutomationUITest
https://zhuanlan.zhihu.com/p/141350141
Selenium 是一套完整的 web 应用程序测试系统 ，它包含了测试录制(Selenium IDE)、编写及运行(Selenium Remote Control) 和测试的并行处理(Selenium Grid)。
Selenium的核心 Selenium Core基于 JsUnit，完全由 JavaScript 编写，因此可以运行于任何支持 JavaScript 的浏览器上。

二、Selenium之-PO模型
PO 模型：将测试的每个页面看作一个对象，将这些对象抽象成类，完成页面元素和业务操作；将测试类和 page 类区分开来，需要调用什么类去取即可，降低耦合。
    当页面元素发生变化时，只需修改对应页面类部分，其他部分极可能做到最小修改。

PO 模型的分层结构（以注册页面作为page对象）：

（1）register_page(页面元素查找类) --->
（2）register_handle(操作层：将查找到的元素上传递数据) --->
（3）register_business(业务层：调用操作层，根据操作层传递的数据进行测试业务场景判断，如验证码输入错误场景等)
（4）register_cases(测试模块：封装业务层，进行测试用例业务组装)。
### Google Chrome 已是最新版本
### 版本 92.0.4515.107（正式版本） （64 位）