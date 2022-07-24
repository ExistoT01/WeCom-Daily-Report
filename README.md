# WeCom-Daily-Report

中国海洋大学企业微信「每日上报」自动脚本

【实现】：抓包企业微信收发的请求，找出上报的api，脚本自动填写信息，python发送request请求，将返回结果以邮件的形式发送本人告之

【局限】：使用脚本之前，需要自己完成一次抓包，获取到相关的位置信息，才能进行填报

## 使用方法

- **建议自己手动抓一遍包**，这样才可以获取到 `headers` 与 `data` 数据

1. 填入自己的 `headers` 数据或覆盖

![image-20220724162825555](https://expicture.oss-cn-beijing.aliyuncs.com/img/202207241633798.png)

2. 填入自己的 `data` 数据或覆盖

![image-20220724162956723](https://expicture.oss-cn-beijing.aliyuncs.com/img/202207241633828.png)

3. 设置邮件收发者与 `「SMTP」token` *(非必要)*

![image-20220724163150910](https://expicture.oss-cn-beijing.aliyuncs.com/img/202207241633441.png)

4. 将脚本部署到服务器，定点执行
