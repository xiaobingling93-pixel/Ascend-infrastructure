# Ascend社区会议指南

## 一、介绍

Ascend社区在官网 [社区会议平台](https://meeting.osinfra.cn/ascend) 提供会议预定功能。

![1761617400166](assets/1761617400166.png)

## 二、如何使用

### 1.申请权限

通过向本仓库提交PR的方式来申请权限：

fork本仓库，在fork的仓库中修改`meeting/meeting.yaml`文件，添加会议创建权限申请信息，然后提交PR。

~~~bash
- sig_name: infrastructure        # SIG组
  etherpad: https://etherpad-ascend.osinfra.cn/p/infrastructure  # 显示会议纪要
  meeting_creators:               # 会议申请人列表
    - account: tom_toworld        # 申请人的华为账号名，用于绑定创建会议的权限。
    - account: XXX
- sig_name: XXX2
  etherpad: https://etherpad-ascend.osinfra.cn/p/XXX2  # 显示会议纪要
  meeting_creators:
    - account: XXX
~~~

注意：

（1）您可以通过点击[账号信息链接](https://id1.cloud.huawei.com/AMW/portal/userCenter/index.html#/security)进行查询申请人华为账号名。

![1761718318252](assets/1761718318252.png)

   (2) 你可以通过点击[community仓库](https://gitcode.com/Ascend/community)查询SIG组名称，示例：下面SIG组名称为：AscendNPU-IR。

![1761718562010](assets/1761718562010.png)

（3）有权限时如下图所示：

![1761718833861](C:\Users\Administrator\Desktop\backup\infrastructure_5620\meeting\assets\1761718833861.png)

### 2.创建会议

当后台管理员审批通过后，我们的申请人即拥有会议创建权限，

![1761618330494](assets/1761618330494.png)

填写会议内容：

+ 会议名称： 这场会议的主题
+ 所属SIG组：选择所需要开会议的SIG组
+ 会议时间：选择对应的会议时间
+ 会议平台：社区的会议能力由第三方提供的，目前只支持WeLink会议（蓝版）
  + WeLink会议：详细内容见：https://www.huaweicloud.com/product/welink-download.html
+ 会议内容：请输入会议的议题或者大概内容，详细的议题内容后续可以在etherpad里面填写。
+ 会议录制：开启此选项，会议会自动录制，会议结束后会自动保存在第三方会议平台中；如果后期增加会议回访，会在官网中显示已开启录制的视频。
+ 邮件地址：填写需要通知参加会议的核心人员和邮件列表，以“；”间隔，最多填写20个邮箱地址。发送成功后可以在对应的邮件列表归档中查看此通知邮件，如果没有则存储拦截情况，请联系基础设施@drizzlezyk [zhongyuanke@huawei.com](mailto:zhongyuanke@huawei.com)处理。

创建的会议会在官网上进行公开。

### 3.修改会议

如果你的会议时间需要调整，你可以进行修改会议，请根据下面截图进行操作：

![1761622636789](assets/1761622636789.png)

![1761622683924](assets/1761622683924.png)

![1761622822289](assets/1761622822289.png)

+ 注意：<font color="red">修改会议暂不支持修改邮件地址</font>

### 3.删除会议

如果你的会议时间需要取消，你可以进行取消会议，请根据下面截图进行操作：

+ 限制：在会议过期或者在半个小时之内即将开始的会议，比如昨天的会议会无法删除；比如半个小时之内即将开始的会议无法删除，这是系统默认半个小时为会议准备时间，大家都准备参加会议，此时取消会议，会对用户造成一定的影响。

![1761622636789](assets/1761622636789.png)

![1761623221236](assets/1761623221236.png)

![1761623278428](assets/1761623278428.png)



### 4.我如何参加会议？

当会议创建后，并进入会议开始时间，我该通过什么方式参加会议？

![1761623420066](assets/1761623420066.png)

![1761623476228](assets/1761623476228.png)

注意：你也可以下载蓝版welink后通过客户端入会，入会的时候输入会议 ID， 比如截图的会议ID: 987098521

进会后请修改你的个人信息，<font color="red">请不要使用工号。</font>

![1761623603989](assets/1761623603989.png)

你可以使用在线会议文档记录会议纪要

![1761623784599](assets/1761623784599.png)

![1761623871001](assets/1761623871001.png)



## 三、FAQ

1.创建会议的时候显示“会议时间冲突，请调整会议时间”？

A:  这是因为会议时间已经存在会议，以你创建会议的起始和结束时间的半个小时内无会议来判断，如果您遇到该提示，请尝试更换一个会议时间，如果一直出现该提示，请联系 [@drizzlezyk](https://gitcode.com/drizzlezyk) [zhongyuanke@huawei.com](mailto:zhongyuanke@huawei.com) 处理。

2.WeLink会议出现“云会议室资源正在召开另外一场会议”？

A:  可能是因为上一场的会议没有结束，或有人没有退出导致，请稍等再重试一下，如果长时间出现该提示，请联系 [@drizzlezyk](https://gitcode.com/drizzlezyk) [zhongyuanke@huawei.com](mailto:zhongyuanke@huawei.com) 进行处理。

