# 使用ArcGIS

ArcGIS是GIS领域最强大的软件，它有很多不同的组成部分，根据[Esri官网](https://www.esri.com/zh-cn/arcgis/about-arcgis/overview)介绍，在ARCGIS栏下包括：ArcGSI Pro，ArcGIS Enterprise，ArcGIS Online，应用程序，ArcGIS for Developers. 这些东西如果不知是什么，那么选择使用和查询资料的时候多少会有点障碍，因此参考一篇post[ArcGIS Pro vs ArcGIS Enterprise vs ArcGIS Online](https://community.esri.com/thread/226220-arcgis-pro-vs-arcgis-enterprise-vs-arcgis-online#)，简单说明下区别：

- **ArcGIS Pro**是在自己本地电脑桌面操作系统里创建，分析，可视化空间数据的基础工具，也是几乎所有人最开始接触Arcgis时使用的产品－－ArcGIS Desktop下的一个系列，之前一直都是使用ArcMap套件的，包括ArcCatalog，Arcgis administrator等，现在官方在大力推广ArcGIS Pro，不过根据群众反映－－[ArcGIS Desktop和ARCGIS PRO有什么区别？](https://www.zhihu.com/question/318599801/answer/641767207)，貌似就主体功能来说，还是老版ArcGIS更好，ArcGIS Pro的优点主要集中在和其他组件融合，使用的是python3等非核心问题上，应该也在持续改进中。
- ArcGIS Enterprise和ArcGIS Desktop不同，ArcGIS Enterprise是一个基于本地或云的单租户WebGIS. 它是面向企业的，一个企业去组织一套ArcGIS服务中心，可以使组织机构在GIS应用方面灵活协作。它将业界领先的映射和分析功能与专用的Web GIS基础设施相结合，在任何时间、任何地点、任何设备上组织和共享个人的工作。总之，是一个企业级的webgis
- *ArcGIS Online*则是一个Esri公司提供的SaaS，可以在其上制作地图，分析数据，share和协作来自全球ArcGIS社区的应用，地图和数据。根据笔记[ArcGIS for Developers简介](arcgis4developers.md)，就目前来看，空间分析等常用功能可能还是不便于在其上开展。

综上所述，作为一个水文水资源ArcGIS重度应用者，基本围绕ArcGIS Desktop使用即可，可以尝试下ArcGIS Pro，Enterprise可以不用care，ArcGIS Online则可以尝尝鲜，看看与其配套使用的ArcGIS for Developers有没有新鲜功能，总之，主要还是在ArcGIS Desktop + 利用python2 脚本自动化流程方面着重留意。因此，本文件夹下的笔记以ArcGIS Desktop实践应用为主。

更多关于ArcGIS使用的教程可以参考：[Advanced Python Programming for GIS - Summer 2020](https://www.e-education.psu.edu/geog489/syllabus)
