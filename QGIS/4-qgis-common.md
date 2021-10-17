# 积累一些常用的QGIS操作

## 导入数据

一般的layer数据直接导入即可，MDB格式的文件相对特殊一点，这里简单记录下。主要参考：

- [How to Open Personal Geodatabase in QGIS](https://www.youtube.com/watch?v=RTtn0TA1fYM)
- [Opening Esri Personal Geodatabase (*.mdb) using QGIS?](https://gis.stackexchange.com/questions/129514/opening-esri-personal-geodatabase-mdb-using-qgis)

首先，下载一个示例数据，从[这里](https://www.cger.nies.go.jp/db/gdbd/gdbd_index_e.html)下载，选择“Asia”下载即可。

这是Esri的格式文件，必须在windows下打开，需要安装access数据库的引擎，我是安装的 office 365，所以已经自带了，就不再重复安装了，需要安装的请在[这里](http://www.microsoft.com/en-gb/download/details.aspx?id=13255)下载。

在windows搜索栏搜索 ODBC，打开给出的 “ODBC 数据源（64位）”，点击“添加”，选择“Microsoft Access Driver ...”，然后起名字，我起了“PersonalMDB”，然后如下图所示“选择”好数据库对应到刚刚下载的mdb文件，然后点击“确定”。

![](img/QQ截图20211017183555.jpg)

接下来，打开QGIS，Settings -> Options | System | Environment，添加下面两个变量：

```Path
variable name: OGR_SKIP
value: ODBC

variable name: PGEO_DRIVER_TEMPLATE
value: DRIVER=Microsoft Access Driver (*.mdb, *.accdb);DBQ=%s
```

如下图所示：

![](img/QQ截图20211017182314.jpg)

然后最好重启下QGIS。

选择“Add Vector Layer …”->"Database"->"New"，然后配置如下，点击Test connection，应该会看到下图中的提示

![](img/QQ截图20211017183937.jpg)

然后点击“Add”键，会提示输入密码，因为我们没加密码，所以直接点击“OK”即可。这时候就会出现如下所示的对话框：

![](img/QQ截图20211017184236.jpg)

选择自己想要加入的项目即可。最后会得到如下所示的结果：

![](img/QQ截图20211017184334.jpg)

稍微介绍下，这个图，其中包括划分的流域及河网，可以看到流域是按照河流交汇点来划分的。

我们可以尝试把图层导出为shapefile，方便后续的处理，右键想要导出的图层，"Export"->"Save Feature As ..."：

![](img/QQ截图20211017185005.jpg)


