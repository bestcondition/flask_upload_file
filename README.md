# flask文件上传例子

## 安装依赖

```shell
pip install -r requirements.txt
```

## 运行参数

- --host 绑定地址 默认127.0.0.1
- --port 监听端口 默认3502，没啥意思随机数字罢了
- --folder 上传地址 默认用户目录下的Downloads

## 已知问题

如果计算机名是中文，绑定地址host=0.0.0.0，可能会报错

解决办法：把计算机名改成中文